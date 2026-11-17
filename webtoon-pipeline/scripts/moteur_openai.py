#!/usr/bin/env python3
"""Moteur d'images OpenAI (le moteur de ChatGPT) pour La Lame-Grise.

Génère une PAGE de webtoon (plusieurs cases empilées) à partir d'un prompt et de plusieurs
images de référence (planches de personnages, page de style), comme dans ChatGPT.

La clé API n'est jamais lue ici : dans la session cloud, le proxy l'injecte dans l'en-tête
Authorization. Sur un autre ordinateur, définir OPENAI_API_KEY.

Exemple :
  python scripts/moteur_openai.py --prompt-file p18.txt \
      --ref codex/references/c3_ref.jpg --ref codex/references/moustache_ref.jpg \
      --out output/pages/ep02_p18.png --quality high
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import uuid
import urllib.request
import urllib.error
from pathlib import Path

API = "https://api.openai.com/v1/images"
DEFAULT_MODEL = "chatgpt-image-latest"


def _multipart(fields: dict, files: list[tuple[str, Path]]) -> tuple[bytes, str]:
    boundary = uuid.uuid4().hex
    out = bytearray()
    for k, v in fields.items():
        out += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    for name, path in files:
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        out += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"; filename=\"{path.name}\"\r\n"
                f"Content-Type: {mime}\r\n\r\n").encode()
        out += path.read_bytes() + b"\r\n"
    out += f"--{boundary}--\r\n".encode()
    return bytes(out), f"multipart/form-data; boundary={boundary}"


def generer(prompt: str, refs: list[Path], out: Path, model: str = DEFAULT_MODEL,
            size: str = "1024x1536", quality: str = "high", retries: int = 3) -> dict:
    """Appelle /images/edits (avec références) ou /images/generations (sans). Retourne la réponse (sans l'image)."""
    key = os.getenv("OPENAI_API_KEY") or "proxy-injected"
    fields = {"model": model, "prompt": prompt, "size": size, "quality": quality, "n": "1"}
    if refs:
        body, ctype = _multipart(fields, [("image[]", r) for r in refs])
        url = f"{API}/edits"
    else:
        body, ctype = json.dumps(fields | {"n": 1}).encode(), "application/json"
        url = f"{API}/generations"
    last = None
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": ctype})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                data = json.loads(r.read())
            img = data["data"][0]
            raw = base64.b64decode(img["b64_json"]) if img.get("b64_json") else urllib.request.urlopen(img["url"]).read()
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(raw)
            meta = {k: v for k, v in data.items() if k != "data"}
            meta.update(model=model, size=size, quality=quality, refs=[str(r) for r in refs],
                        secondes=round(time.time() - t0, 1), fichier=str(out))
            out.with_suffix(".json").write_text(json.dumps(meta | {"prompt": prompt}, ensure_ascii=False, indent=2),
                                                encoding="utf-8")
            return meta
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="ignore")
            last = f"HTTP {e.code} : {msg[:400]}"
            if e.code in (400, 401, 403) or "insufficient_quota" in msg or "credit_balance" in msg:
                break  # requête, clé ou crédits : inutile de réessayer
        except Exception as e:  # noqa: BLE001
            last = str(e)
        time.sleep(2 ** attempt)
    raise RuntimeError(last)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--ref", action="append", default=[])
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--size", default="1024x1536")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    a = ap.parse_args()
    meta = generer(Path(a.prompt_file).read_text(encoding="utf-8"), [Path(r) for r in a.ref], Path(a.out),
                   a.model, a.size, a.quality)
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.exit(main())
