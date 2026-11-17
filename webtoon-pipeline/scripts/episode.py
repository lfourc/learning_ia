#!/usr/bin/env python3
"""Production d'un épisode complet à partir d'un fichier de spécification (episode.json).

  python scripts/episode.py generer output/episodes/ep03/episode.json [--case 3.01] [--force] [--quality high]
  python scripts/episode.py monter  output/episodes/ep03/episode.json

episode.json reprend la structure des pages d'épisode publiées (séquences, cases, bulles en %).
Une case avec un bloc "gen" est générée par le moteur OpenAI (scripts/moteur_openai.py) :
  "gen": {"prompt": "...", "refs": ["codex/references/c3_ref.jpg", ...], "taille": "1536x1024"}
Une case sans "gen" réutilise une image existante (img/<img>.jpg).
Les images sont recadrées au format de la case (LARGE 16:9, VERT 9:16, CASE 4:3, INSERT 1:1, BANDE 3:1)
puis réduites à 800 px de large. Le cache évite de payer deux fois la même case.
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from moteur_openai import generer  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RATIO = {"LARGE": 16 / 9, "VERT": 9 / 16, "CASE": 4 / 3, "INSERT": 1.0, "BANDE": 3.0}
TAILLE = {"LARGE": "1536x1024", "BANDE": "1536x1024", "CASE": "1536x1024", "VERT": "1024x1536", "INSERT": "1024x1024"}

STYLE = ("Korean action-fantasy webtoon panel, semi-realistic proportions, clean sharp ink lineart, hard-edged cel "
         "shading with two or three flat tones and crisp shadows on faces, strong rim light and backlight, high contrast, "
         "cinematic dynamic camera angle, expressive detailed eyes, detail only on faces and the key object, simplified "
         "or softly blurred background, muted desaturated palette, magic and light sources as the only saturated glowing "
         "color, empty calm area for speech bubbles, no text, single panel, no panel borders")
NEG = ("oil painting, painterly brushstrokes, photorealism, soft airbrushed gradients, pastel shoujo style, western "
       "cartoon style, thick outlines, busy textures, ornate embroidery detail, cluttered foliage, overly detailed "
       "background, grain, christian cross, crucifix, fleur-de-lis, text, letters, watermark, speech bubbles, extra fingers")


def cases(spec: dict):
    for s in spec["seq"]:
        for e in s["items"]:
            if e.get("t") == "P":
                yield e


def recadrer(src: Path, dst: Path, fmt: str) -> None:
    im = Image.open(src).convert("RGB")
    r = RATIO.get(fmt, im.width / im.height)
    w, h = im.size
    if w / h > r:  # trop large : on rogne les côtés
        nw = int(h * r)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:  # trop haut : on rogne haut et bas
        nh = int(w / r)
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((800, int(800 * im.height / im.width)), Image.LANCZOS)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, quality=90)


def cmd_generer(spec_path: Path, only: list[str], force: bool, quality: str, workers: int) -> None:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    base = spec_path.parent
    todo = []
    for e in cases(spec):
        if "gen" not in e or (only and e["id"] not in only):
            continue
        dst = base / "img" / f"{e['img']}.jpg"
        if dst.exists() and not force and not only:
            continue
        todo.append(e)
    print(f"{len(todo)} case(s) à générer (qualité {quality}).", flush=True)

    def un(e):
        g = e["gen"]
        refs = [ROOT / r for r in g.get("refs", [])]
        prompt = (f"{g['prompt']}. {STYLE}. Avoid: {NEG}.")
        if refs:
            prompt = ("Use the attached images as exact references for the characters' faces, hair and clothing, "
                      "and for the drawing style, colors and lighting. " + prompt)
        brut = base / "brut" / f"{e['img']}.png"
        meta = generer(prompt, refs, brut, size=g.get("taille", TAILLE.get(e["f"], "1536x1024")), quality=quality)
        recadrer(brut, base / "img" / f"{e['img']}.jpg", e["f"])
        return e["id"], meta

    total = 0
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(un, e): e["id"] for e in todo}
        for f in as_completed(futs):
            try:
                cid, meta = f.result()
                tok = (meta.get("usage") or {}).get("output_tokens_details", {}).get("image_tokens", 0)
                total += tok
                print(f"  ✓ {cid}  {meta['secondes']} s  {tok} jetons image", flush=True)
            except Exception as ex2:  # noqa: BLE001
                print(f"  ✗ {futs[f]} : {ex2}", flush=True)
    print(f"Jetons image produits : {total}", flush=True)


def cmd_monter(spec_path: Path) -> None:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    tpl = (ROOT / "scripts" / "modele_episode.html").read_text(encoding="utf-8")
    manquantes = [e["id"] for e in cases(spec) if not (spec_path.parent / "img" / f"{e['img']}.jpg").exists()]
    seq = json.dumps(spec["seq"], ensure_ascii=False)
    html = (tpl.replace("__TITRE__", spec["titre_page"]).replace("__LEGENDE__", spec.get("legende", ""))
               .replace("__SEQ__", seq).replace("__FIN__", spec.get("fin", ""))
               .replace("__TITRE_SERIE__", spec.get("titre_case", {}).get("a", "La Lame-Grise"))
               .replace("__TITRE_EP__", spec.get("titre_case", {}).get("b", ""))
               .replace("__NUM_EP__", spec.get("titre_case", {}).get("c", "")))
    out = spec_path.parent / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"{out.relative_to(ROOT)}  ({len(list(cases(spec)))} cases ; images manquantes : {manquantes or 'aucune'})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["generer", "monter"])
    ap.add_argument("spec")
    ap.add_argument("--case", action="append", default=[])
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    ap.add_argument("--workers", type=int, default=5)
    a = ap.parse_args()
    p = Path(a.spec).resolve()
    if a.action == "generer":
        cmd_generer(p, a.case, a.force, a.quality, a.workers)
    else:
        cmd_monter(p)


if __name__ == "__main__":
    main()
