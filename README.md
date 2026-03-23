# OpenDotURL - Extension Nemo

Extension pour le gestionnaire de fichiers **Nemo** (Linux Mint / Cinnamon) qui permet d'ouvrir les fichiers de raccourcis `.url` (format Windows) directement dans votre navigateur.

## Fonctionnement

Un clic droit sur un fichier `.url` dans Nemo affiche l'option **"Ouvrir Raccourci Windows"** qui ouvre l'URL dans votre navigateur par defaut.

Le script accepte trois formats de fichier `.url` :

- Format INI Windows : `[InternetShortcut]` suivi de `URL=https://...`
- Ligne `url=https://...` ou `URL=https://...` (sans section)
- URL brute : `https://...` seule sur une ligne

## Installation

### 1. Copier le script

```bash
mkdir -p ~/.local/bin
cp ouvrir-url.py ~/.local/bin/
chmod +x ~/.local/bin/ouvrir-url.py
```

### 2. Installer l'action Nemo

```bash
mkdir -p ~/.local/share/nemo/actions
cp ouvrir-url.nemo_action ~/.local/share/nemo/actions/
```

### 3. Recharger Nemo

```bash
nemo -q
```

## Resultat

Un **clic droit sur un fichier `.url`** dans Nemo propose l'option **"Ouvrir Raccourci Windows"** qui ouvre le lien dans votre navigateur.

## Nautilus (non teste)

Pour Nautilus (GNOME), modifiez le chemin dans `ouvrir-url.desktop` si necessaire, puis :

```bash
mkdir -p ~/.local/share/file-manager/actions
cp ouvrir-url.desktop ~/.local/share/file-manager/actions/
nautilus -q
```
