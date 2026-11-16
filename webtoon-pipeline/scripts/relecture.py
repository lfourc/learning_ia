#!/usr/bin/env python3
"""Rend un chapitre JSON lisible (Markdown) pour relecture avant génération.

    python scripts/relecture.py -c 3        →  output/json/chapitre_03_relecture.md
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABEL = {"dialogue": "Bulle", "pensee": "Pensée", "cri": "Cri", "sfx": "SFX", "narration": "Encadré"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--chapitre", type=int, required=True)
    n = ap.parse_args().chapitre
    path = ROOT / "output" / "json" / f"chapitre_{n:02d}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    out = [f"# Épisode {data['chapitre']} — {data.get('titre', '')}", ""]
    if data.get("statut"):
        out += [f"*{data['statut']}*", ""]
    cases = data["cases"]
    n_src = sum(1 for c in cases if isinstance(c.get("source"), dict) and c["source"].get("extrait"))
    n_inv = sum(1 for c in cases if isinstance(c.get("source"), dict) and c["source"].get("invention"))
    out += [f"{len(cases)} cases : **{n_src} appuyées sur un extrait du livre**, **{n_inv} inventées**, "
            f"{len(cases) - n_src - n_inv} sans source.", "",
            "Pour chaque case : la source (extrait exact du livre, ou invention), puis le texte lettré "
            "(*passe 1* = ce que le personnage veut dire, « passe 2 » = la réplique finale), puis le prompt.", ""]
    seq, prev_src = None, [None]
    for c in data["cases"]:
        if c.get("sequence") and c["sequence"] != seq:
            seq = c["sequence"]
            out += [f"## {seq}", ""]
        ref = f" · réf. `{c['reference_image']}`" if c.get("reference_image") else ""
        out.append(f"**{c['id']}** · {c.get('format', '?')}{ref} · espace après {c.get('espace_apres_px')}px "
                   f"({c.get('transition_fond', 'blanc')})")
        src = c.get("source")
        if src and src != prev_src[0]:
            if src.get("invention"):
                out.append(f"> 🆕 **Invention** — {src['invention']}")
            else:
                out.append(f"> 📖 **{src.get('ref', 'Livre')}**")
                ext = src.get("extrait")
                for e in (ext if isinstance(ext, list) else [ext]):
                    out.append(f"> « {e.strip()} »")
                if src.get("note"):
                    out.append(f"> *Note : {src['note']}*")
            out.append("")
        elif src:
            out.append("> *(même source que la case précédente)*")
            out.append("")
        prev_src[0] = src
        for d in c.get("dialogues", []):
            who = f"{d['personnage']} " if d.get("personnage") else ""
            if d.get("intention"):
                out.append(f"- *passe 1 : {d['intention']}*")
            out.append(f"- {LABEL.get(d.get('type'), d.get('type'))} {who}: « {d['texte']} »")
        if c.get("sfx"):
            out.append(f"- SFX : *{c['sfx']}*")
        out += [f"- Prompt : `{c.get('image_prompt', '')}`", ""]
    dst = path.with_name(f"chapitre_{n:02d}_relecture.md")
    dst.write_text("\n".join(out), encoding="utf-8")
    print(dst.relative_to(ROOT))


if __name__ == "__main__":
    main()
