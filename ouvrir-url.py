#!/usr/bin/env python3
import sys, configparser, subprocess

for fichier in sys.argv[1:]:
    parser = configparser.ConfigParser()
    parser.read(fichier)
    url = parser.get("InternetShortcut", "URL", fallback=None)
    if url:
        subprocess.run(["xdg-open", url])
