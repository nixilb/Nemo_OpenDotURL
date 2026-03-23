#!/usr/bin/env python3
import sys, re, subprocess

for fichier in sys.argv[1:]:
    url = None
    with open(fichier, encoding="utf-8", errors="ignore") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("[") or ligne.startswith("#") or ligne.startswith(";"):
                continue
            m = re.match(r"(?i)url\s*=\s*(.+)", ligne)
            if m:
                url = m.group(1).strip()
                break
            if re.match(r"https?://", ligne, re.IGNORECASE):
                url = ligne
                break
    if url:
        subprocess.run(["xdg-open", url])
