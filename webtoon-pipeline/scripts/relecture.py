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
    src = ROOT / "output" / "json" / f"chapitre_{n:02d}.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    out = [f"# Épisode {data['chapitre']} — {data.get('titre', '')}", ""]
    if data.get("statut"):
        out += [f"*{data['statut']}*", ""]
    out += [f"{len(data['cases'])} cases. Le texte entre « » est ce qui sera lettré ; le prompt anglais sert à générer l'image.", ""]
    seq = None
    for c in data["cases"]:
        if c.get("sequence") and c["sequence"] != seq:
            seq = c["sequence"]
            out += [f"## {seq}", ""]
        ref = f" · réf. `{c['reference_image']}`" if c.get("reference_image") else ""
        out.append(f"**{c['id']}** · {c.get('format', '?')}{ref} · espace après {c.get('espace_apres_px')}px "
                   f"({c.get('transition_fond', 'blanc')})")
        for d in c.get("dialogues", []):
            who = f"{d['personnage']} " if d.get("personnage") else ""
            out.append(f"- {LABEL.get(d.get('type'), d.get('type'))} {who}: « {d['texte']} »")
        if c.get("sfx"):
            out.append(f"- SFX : *{c['sfx']}*")
        out += [f"- Prompt : `{c.get('image_prompt', '')}`", ""]
    dst = src.with_name(f"chapitre_{n:02d}_relecture.md")
    dst.write_text("\n".join(out), encoding="utf-8")
    print(dst.relative_to(ROOT))


if __name__ == "__main__":
    main()
