#!/usr/bin/env python3
"""
generate_webtoon.py — Pipeline de production Webtoon IA (style manhwa).

Étapes :
  1. Lit /output/json/chapitre_XX.json
  2. Génère chaque case via Fal.ai (Flux schnell / dev / PuLID)
  3. Assemble des bandes verticales de 800px (Pillow), découpées tous les 10000px max
  4. Exporte planche_texte.txt (dialogues case par case, avec position Y pour le lettrage)

Exemples :
  python scripts/generate_webtoon.py --chapitre 1 --mode draft
  python scripts/generate_webtoon.py --chapitre 1 --mode final
  python scripts/generate_webtoon.py --chapitre 1 --mode final --case case_05 --case case_06
  python scripts/generate_webtoon.py --chapitre 1 --assemble-only
  python scripts/generate_webtoon.py --chapitre 1 --dry-run        # aucune requête API (images factices)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.request
from base64 import b64decode
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --------------------------------------------------------------------------- #
# Constantes
# --------------------------------------------------------------------------- #
ROOT = Path(__file__).resolve().parent.parent
CODEX_DIR = ROOT / "codex"
REF_DIR = CODEX_DIR / "references"
JSON_DIR = ROOT / "output" / "json"
PANELS_DIR = ROOT / "output" / "panels"
STRIPS_DIR = ROOT / "output" / "strips"

STRIP_WIDTH = 800
DEFAULT_MAX_STRIP_HEIGHT = 10_000
MAX_WORDS_PER_BUBBLE = 15

MODELS = {
    "draft": "fal-ai/flux/schnell",
    "final": "fal-ai/flux/dev",
    "final_ref": "fal-ai/flux-pulid",
}
# Coût indicatif par image (USD), à ajuster selon la grille Fal.ai en vigueur.
COST_ESTIMATE = {"draft": 0.003, "final": 0.025, "final_ref": 0.033}

COLORS = {"noir": (0, 0, 0), "blanc": (255, 255, 255)}
VALID_TRANSITIONS = {"noir", "blanc", "degrade_noir", "degrade_blanc"}
VALID_DIALOGUE_TYPES = {"dialogue", "pensee", "cri", "sfx", "narration"}
# Tournures « robot » détectables (règles d'or des dialogues, CLAUDE.md § 3.C)
ANTI_ROBOT = [
    (r"\bje (ressens|me sens)\b|\bprofonde? (colère|tristesse|peur|haine|joie)\b", "émotion nommée"),
    (r"\b(colère|tristesse|désespoir|rancœur|jalousie) (face|envers)\b", "émotion nommée"),
    (r"\bje vais \w+ .{0,40}\bpour\b", "explicatif (le personnage raconte son action)"),
    (r"\bje ne m'attendais pas\b|\bque viens-tu\b|\bdans ce lieu\b", "théâtral"),
    (r"\b(putain|fous|foutre|genre|grave|pisse[rz]?|ok)\b|\bsérieux ?\?|\bj'(vous|te|vais)\b|\bt'(as|es|étais)\b|(?<!il )\by a\b",
     "anachronisme / argot moderne (registre La Lame-Grise)"),
]


def log(msg: str) -> None:
    print(msg, flush=True)


# --------------------------------------------------------------------------- #
# Chargement & validation du JSON
# --------------------------------------------------------------------------- #
def resolve_json_path(args: argparse.Namespace) -> Path:
    if args.json:
        return Path(args.json).resolve()
    return JSON_DIR / f"chapitre_{int(args.chapitre):02d}.json"


def load_chapter(path: Path) -> dict:
    if not path.exists():
        sys.exit(f"[ERREUR] JSON introuvable : {path}")
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data.get("cases"), list) or not data["cases"]:
        sys.exit(f"[ERREUR] {path.name} : la clé 'cases' est vide ou absente.")
    return data


SOURCE_TXT = ROOT / "source" / "livre_source.txt"


def _norm(t: str) -> str:
    t = t.replace("’", "'").replace("\u00a0", " ").replace("*", "")
    return re.sub(r"\s+", " ", t).strip()


def validate_chapter(data: dict) -> list[str]:
    """Vérifie le schéma + les règles manhwa. Retourne la liste des avertissements."""
    warnings: list[str] = []
    livre = _norm(SOURCE_TXT.read_text(encoding="utf-8")) if SOURCE_TXT.exists() else ""
    seen: set[str] = set()
    for i, case in enumerate(data["cases"]):
        cid = case.get("id") or f"<case #{i + 1}>"
        if "id" not in case:
            warnings.append(f"{cid} : champ 'id' manquant.")
        if cid in seen:
            warnings.append(f"{cid} : id dupliqué.")
        seen.add(cid)
        if not case.get("image_prompt"):
            warnings.append(f"{cid} : 'image_prompt' vide (impossible de (re)générer cette case).")
        try:
            parse_ratio(case.get("format", "9:16"))
        except ValueError as e:
            warnings.append(f"{cid} : {e}")
        tr = case.get("transition_fond", "blanc")
        if tr not in VALID_TRANSITIONS:
            warnings.append(f"{cid} : transition_fond '{tr}' inconnue ({', '.join(sorted(VALID_TRANSITIONS))}).")
        gap = case.get("espace_apres_px", 200)
        if not isinstance(gap, int) or gap < 0:
            warnings.append(f"{cid} : espace_apres_px doit être un entier >= 0.")
        src = case.get("source")
        if not src:
            warnings.append(f"{cid} : pas de 'source' (extrait du livre ou 'invention').")
        elif isinstance(src, dict) and src.get("extrait") and livre:
            for ext in (src["extrait"] if isinstance(src["extrait"], list) else [src["extrait"]]):
                if _norm(ext) not in livre:
                    warnings.append(f"{cid} : extrait introuvable mot pour mot dans le livre — « {ext[:40]}… »")
        ref = case.get("reference_image")
        if ref and not (REF_DIR / ref).exists():
            warnings.append(f"{cid} : image de référence absente ({REF_DIR / ref}).")
        for d in case.get("dialogues", []) or []:
            if d.get("type") not in VALID_DIALOGUE_TYPES:
                warnings.append(f"{cid} : type de dialogue '{d.get('type')}' inconnu.")
            txt = str(d.get("texte", ""))
            if d.get("type") != "narration":
                for pat, why in ANTI_ROBOT:
                    if re.search(pat, txt, re.I):
                        warnings.append(f"{cid} : dialogue « {txt[:40]}… » — {why}.")
                        break
            n = len(txt.split())
            if n > MAX_WORDS_PER_BUBBLE and d.get("type") != "narration":
                warnings.append(
                    f"{cid} : bulle de {n} mots (> {MAX_WORDS_PER_BUBBLE}) — "
                    f"« {str(d.get('texte'))[:50]}… »"
                )
    last = data["cases"][-1]
    if last.get("format") != "9:16":
        warnings.append(f"{last.get('id')} : la dernière case (cliffhanger) devrait être en 9:16.")
    return warnings


# --------------------------------------------------------------------------- #
# Formats d'image
# --------------------------------------------------------------------------- #
def parse_ratio(fmt: str) -> tuple[int, int]:
    m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*:\s*(\d+(?:\.\d+)?)\s*", str(fmt))
    if not m:
        raise ValueError(f"format '{fmt}' invalide (attendu 'L:H', ex. '9:16').")
    w, h = float(m.group(1)), float(m.group(2))
    if w <= 0 or h <= 0:
        raise ValueError(f"format '{fmt}' invalide.")
    return w, h


def image_size_for(fmt: str, megapixels: float = 1.0) -> dict:
    """Calcule une taille ~1 MP, multiple de 16, respectant le ratio demandé."""
    w, h = parse_ratio(fmt)
    area = megapixels * 1024 * 1024
    width = (area * w / h) ** 0.5
    height = width * h / w
    rnd = lambda v: max(256, min(2048, int(round(v / 16)) * 16))
    return {"width": rnd(width), "height": rnd(height)}


# --------------------------------------------------------------------------- #
# Génération Fal.ai
# --------------------------------------------------------------------------- #
_ref_url_cache: dict[str, str] = {}


def upload_reference(fal_client, filename: str) -> str:
    if filename not in _ref_url_cache:
        path = REF_DIR / filename
        log(f"    ↑ upload référence {filename}")
        _ref_url_cache[filename] = fal_client.upload_file(str(path))
    return _ref_url_cache[filename]


def build_request(case: dict, mode: str, fal_client, seed: int | None) -> tuple[str, dict, str]:
    size = image_size_for(case.get("format", "9:16"))
    prompt = case["image_prompt"]
    ref = case.get("reference_image")
    use_ref = mode == "final" and ref and (REF_DIR / ref).exists()

    if mode == "draft":
        key = "draft"
        args = {"prompt": prompt, "image_size": size, "num_inference_steps": 4,
                "num_images": 1, "enable_safety_checker": False}
    elif use_ref:
        key = "final_ref"
        args = {"prompt": prompt, "image_size": size, "num_inference_steps": 20,
                "guidance_scale": 4, "id_weight": 1.0, "true_cfg": 1.0,
                "reference_image_url": upload_reference(fal_client, ref)}
    else:
        key = "final"
        args = {"prompt": prompt, "image_size": size, "num_inference_steps": 28,
                "guidance_scale": 3.5, "num_images": 1, "enable_safety_checker": False}
    if seed is not None:
        args["seed"] = seed
    return MODELS[key], args, key


def fetch_image(url: str) -> Image.Image:
    if url.startswith("data:"):
        return Image.open(BytesIO(b64decode(url.split(",", 1)[1]))).convert("RGB")
    with urllib.request.urlopen(url, timeout=120) as r:
        return Image.open(BytesIO(r.read())).convert("RGB")


def generate_case(case: dict, mode: str, fal_client, seed: int | None, retries: int = 3) -> tuple[Image.Image, str]:
    model, arguments, key = build_request(case, mode, fal_client, seed)
    log(f"    → {model} {arguments['image_size']['width']}x{arguments['image_size']['height']}")
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            result = fal_client.subscribe(model, arguments=arguments, with_logs=False)
            images = result.get("images") or []
            if not images:
                raise RuntimeError(f"réponse sans image : {str(result)[:200]}")
            if (result.get("has_nsfw_concepts") or [False])[0]:
                log("    ⚠ image signalée NSFW par le modèle (vérifier la case).")
            return fetch_image(images[0]["url"]), key
        except Exception as e:  # noqa: BLE001 — on veut retenter sur toute erreur réseau/API
            last_err = e
            wait = 2 ** attempt
            log(f"    ✗ tentative {attempt}/{retries} échouée : {e} — nouvel essai dans {wait}s")
            time.sleep(wait)
    raise RuntimeError(f"échec définitif pour {case['id']} : {last_err}")


def placeholder_image(case: dict) -> Image.Image:
    """Image factice (mode --dry-run) pour valider le rythme sans payer d'API."""
    size = image_size_for(case.get("format", "9:16"))
    img = Image.new("RGB", (size["width"], size["height"]), (205, 210, 220))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, size["width"] - 1, size["height"] - 1], outline=(40, 40, 40), width=8)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 42)
        small = ImageFont.truetype("DejaVuSans.ttf", 22)
    except OSError:
        font = small = ImageFont.load_default()
    draw.text((30, 30), f"{case['id']}  [{case.get('format', '9:16')}]", fill=(20, 20, 20), font=font)
    words, line, y = case.get("image_prompt", "").split(), "", 110
    for w in words:
        if len(line) + len(w) > 60:
            draw.text((30, y), line, fill=(60, 60, 60), font=small)
            y, line = y + 30, ""
        line += w + " "
    draw.text((30, y), line, fill=(60, 60, 60), font=small)
    return img


# --------------------------------------------------------------------------- #
# Gestion des fichiers de cases
# --------------------------------------------------------------------------- #
def chapter_slug(data: dict, json_path: Path) -> str:
    if "chapitre" in data:
        return f"chapitre_{int(data['chapitre']):02d}"
    return json_path.stem


def panel_path(slug: str, mode: str, case_id: str) -> Path:
    return PANELS_DIR / slug / mode / f"{case_id}.png"


def best_panel(slug: str, case_id: str) -> Path | None:
    """Pour l'assemblage : prend la meilleure version disponible (final > draft > factice)."""
    for m in ("final", "draft", "dryrun"):
        p = panel_path(slug, m, case_id)
        for cand in (p, p.with_suffix(".jpg"), p.with_suffix(".jpeg"), p.with_suffix(".webp")):
            if cand.exists():
                return cand
    return None


# --------------------------------------------------------------------------- #
# Assemblage vertical
# --------------------------------------------------------------------------- #
def resize_to_width(img: Image.Image, width: int = STRIP_WIDTH) -> Image.Image:
    if img.width == width:
        return img
    h = max(1, round(img.height * width / img.width))
    return img.resize((width, h), Image.LANCZOS)


def make_gap(height: int, transition: str) -> Image.Image:
    """Espace vide : 'noir', 'blanc', 'degrade_noir' (blanc→noir) ou 'degrade_blanc' (noir→blanc)."""
    if transition in COLORS:
        return Image.new("RGB", (STRIP_WIDTH, height), COLORS[transition])
    if transition not in VALID_TRANSITIONS:
        return Image.new("RGB", (STRIP_WIDTH, height), COLORS["blanc"])
    start = COLORS["blanc"] if transition == "degrade_noir" else COLORS["noir"]
    end = COLORS["noir"] if transition == "degrade_noir" else COLORS["blanc"]
    grad = Image.new("RGB", (1, height))
    for y in range(height):
        t = y / max(1, height - 1)
        grad.putpixel((0, y), tuple(round(s + (e - s) * t) for s, e in zip(start, end)))
    return grad.resize((STRIP_WIDTH, height))


def assemble(data: dict, slug: str, max_height: int, out_format: str) -> list[dict]:
    """Assemble les bandes et retourne la position (bande, y) de chaque case."""
    blocks: list[tuple[str, Image.Image]] = []   # (case_id | "", image)
    missing: list[str] = []
    for case in data["cases"]:
        p = best_panel(slug, case["id"])
        if p is None:
            missing.append(case["id"])
            continue
        blocks.append((case["id"], resize_to_width(Image.open(p).convert("RGB"))))
        gap_h = int(case.get("espace_apres_px", 200))
        if gap_h > 0:
            blocks.append(("", make_gap(gap_h, case.get("transition_fond", "blanc"))))
    if missing:
        log(f"  ⚠ cases sans image (ignorées dans l'assemblage) : {', '.join(missing)}")
    if not blocks:
        log("  ✗ aucune image à assembler.")
        return []

    # Découpe en bandes : on évite de couper une case en deux. Une case plus haute que
    # max_height (rare) est découpée en tranches ; un espace vide peut être coupé librement.
    strips: list[list[tuple[str, Image.Image]]] = [[]]
    heights = [0]
    for cid, img in blocks:
        remaining = img
        while remaining is not None:
            room = max_height - heights[-1]
            if remaining.height <= room:
                strips[-1].append((cid, remaining))
                heights[-1] += remaining.height
                remaining = None
            elif cid and heights[-1] > 0:  # case entière → nouvelle bande
                strips.append([]); heights.append(0)
            else:  # espace vide, ou case trop haute pour une bande : on coupe
                if room > 0:
                    strips[-1].append((cid, remaining.crop((0, 0, STRIP_WIDTH, room))))
                    heights[-1] += room
                remaining = remaining.crop((0, room, STRIP_WIDTH, remaining.height))
                strips.append([]); heights.append(0)
    if not strips[-1]:
        strips.pop(); heights.pop()

    out_dir = STRIPS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("planche_*.*"):
        if old.suffix.lower() in (".png", ".jpg"):
            old.unlink()

    positions: list[dict] = []
    ext = "jpg" if out_format == "jpg" else "png"
    for n, (parts, h) in enumerate(zip(strips, heights), start=1):
        canvas = Image.new("RGB", (STRIP_WIDTH, h), COLORS["blanc"])
        y = 0
        for cid, img in parts:
            canvas.paste(img, (0, y))
            if cid and not any(pos["id"] == cid for pos in positions):
                positions.append({"id": cid, "planche": n, "y": y, "h": img.height})
            y += img.height
        name = out_dir / f"planche_{n:02d}.{ext}"
        if ext == "jpg":
            canvas.save(name, quality=92, optimize=True)
        else:
            canvas.save(name, optimize=True)
        log(f"  ✓ {name.relative_to(ROOT)}  ({STRIP_WIDTH}x{h}px)")
    return positions


# --------------------------------------------------------------------------- #
# Export texte pour le lettrage
# --------------------------------------------------------------------------- #
TYPE_LABEL = {"dialogue": "BULLE", "pensee": "PENSÉE", "cri": "CRI", "sfx": "SFX", "narration": "NARRATION"}


def export_lettering(data: dict, slug: str, positions: list[dict]) -> Path:
    pos = {p["id"]: p for p in positions}
    out = STRIPS_DIR / slug / "planche_texte.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"CHAPITRE {data.get('chapitre', '?')} — {data.get('titre', '')}".strip(),
        "=" * 60,
        "",
    ]
    for case in data["cases"]:
        p = pos.get(case["id"])
        where = f"planche_{p['planche']:02d}, y={p['y']}px → {p['y'] + p['h']}px" if p else "(image manquante)"
        lines.append(f"[{case['id']}]  format {case.get('format', '?')}  |  {where}")
        for d in case.get("dialogues", []) or []:
            label = TYPE_LABEL.get(d.get("type", ""), str(d.get("type", "?")).upper())
            who = d.get("personnage") or "—"
            lines.append(f"   {label:<9} {who} : {d.get('texte', '')}")
            if d.get("position"):
                pos_txt = ", ".join(f"{k}={v}%" for k, v in d["position"].items())
                lines.append(f"   {'':<9} ↳ position dans la case : {pos_txt}")
        if case.get("sfx"):
            lines.append(f"   {'SFX':<9} « {case['sfx']} »")
        if not (case.get("dialogues") or case.get("sfx")):
            lines.append("   (case muette)")
        lines.append(f"   ↓ espace {case.get('espace_apres_px', 200)}px ({case.get('transition_fond', 'blanc')})")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    log(f"  ✓ {out.relative_to(ROOT)}")
    return out


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Génère et assemble un chapitre de webtoon via Fal.ai.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--chapitre", "-c", type=int, help="Numéro du chapitre (lit output/json/chapitre_XX.json)")
    src.add_argument("--json", help="Chemin explicite vers un JSON de chapitre")
    ap.add_argument("--mode", choices=["draft", "final"], default="draft",
                    help="draft = flux/schnell (rapide, ~0.003$) ; final = flux/dev ou flux-pulid si reference_image")
    ap.add_argument("--case", action="append", default=[], metavar="CASE_ID",
                    help="Ne (re)génère que cette case (répétable : --case case_05 --case case_06)")
    ap.add_argument("--force", action="store_true", help="Régénère même si l'image existe déjà")
    ap.add_argument("--seed", type=int, default=None, help="Seed fixe (reproductibilité)")
    ap.add_argument("--assemble-only", action="store_true", help="N'appelle pas l'API, assemble seulement")
    ap.add_argument("--no-assemble", action="store_true", help="Génère sans assembler")
    ap.add_argument("--dry-run", action="store_true", help="Images factices locales, aucun appel API (gratuit)")
    ap.add_argument("--max-height", type=int, default=DEFAULT_MAX_STRIP_HEIGHT, help="Hauteur max d'une bande (px)")
    ap.add_argument("--format", choices=["png", "jpg"], default="png", help="Format des bandes exportées")
    ap.add_argument("--yes", "-y", action="store_true", help="Ne pas demander de confirmation avant de payer")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    json_path = resolve_json_path(args)
    data = load_chapter(json_path)
    slug = chapter_slug(data, json_path)
    log(f"📖 {slug} — {data.get('titre', '(sans titre)')} — {len(data['cases'])} cases")

    warnings = validate_chapter(data)
    for w in warnings:
        log(f"  ⚠ {w}")

    all_ids = [c["id"] for c in data["cases"]]
    unknown = [c for c in args.case if c not in all_ids]
    if unknown:
        sys.exit(f"[ERREUR] case(s) inconnue(s) : {', '.join(unknown)}")

    gen_mode = "dryrun" if args.dry_run else args.mode

    if not args.assemble_only:
        targets = [c for c in data["cases"] if not args.case or c["id"] in args.case]
        force = args.force or bool(args.case)  # --case implique une régénération
        todo = [c for c in targets
                if force or not any(panel_path(slug, gen_mode, c["id"]).with_suffix(x).exists()
                                    for x in (".png", ".jpg", ".jpeg", ".webp"))]
        skipped = len(targets) - len(todo)
        if skipped:
            log(f"  ↷ {skipped} case(s) déjà générée(s) en mode {gen_mode} (utiliser --force pour refaire)")

        fal_client = None
        if todo and not args.dry_run:
            try:
                from dotenv import load_dotenv
                load_dotenv(ROOT / ".env")
            except ImportError:
                pass
            if not os.getenv("FAL_KEY"):
                sys.exit("[ERREUR] FAL_KEY absente. Renseigne-la dans webtoon-pipeline/.env (voir .env.example).")
            import fal_client as _fal
            fal_client = _fal

            est = sum(
                COST_ESTIMATE["final_ref" if args.mode == "final" and c.get("reference_image")
                              and (REF_DIR / c["reference_image"]).exists() else args.mode]
                for c in todo
            )
            log(f"💰 {len(todo)} image(s) à générer — coût estimé ≈ {est:.3f} $")
            if not args.yes and sys.stdin.isatty():
                if input("   Continuer ? [o/N] ").strip().lower() not in ("o", "oui", "y", "yes"):
                    sys.exit("Annulé.")

        failures = []
        for i, case in enumerate(todo, start=1):
            log(f"  [{i}/{len(todo)}] {case['id']}")
            out = panel_path(slug, gen_mode, case["id"])
            out.parent.mkdir(parents=True, exist_ok=True)
            try:
                if args.dry_run:
                    img = placeholder_image(case)
                else:
                    img, _ = generate_case(case, args.mode, fal_client, args.seed)
                img.save(out)
                log(f"    ✓ {out.relative_to(ROOT)}")
            except Exception as e:  # noqa: BLE001
                failures.append(case["id"])
                log(f"    ✗ {e}")
        if failures:
            log(f"⚠ Échecs : {', '.join(failures)} — relancer avec --case pour chacune.")

    if not args.no_assemble:
        log("🧩 Assemblage des bandes verticales")
        positions = assemble(data, slug, args.max_height, args.format)
        export_lettering(data, slug, positions)
    log("✅ Terminé.")


if __name__ == "__main__":
    main()
