# OpenDotURL

opens windows .url files

Right clic in ubuntu nemo on a file.url windows shortcut: 
it proposes a menu to open the internet URL.


## Le script Python

Rends-le exécutable :

```bash
chmod +x ouvrir-url.py
mkdir -p ~/.local/bin
cp  ouvrir-url.py ~/.local/bin/
nemo ~/.local/bin/
```
## Pour Nemo

Nemo lit les fichiers .nemo_action dans :

```bash
nemo ~/.local/share/nemo/actions/ &
```

```bash
cp ouvrir-url.nemo_action ~/.local/share/nemo/actions
```
Puis recharge Nemo :

```bash
nemo -q
```

## Pour Nautilus (pas testé, j'ai pas)

Dans ouvrir-url.desktop: change `nis` par ton vrai login Linux

```bash
mkdir -p ~/.local/share/file-manager/actions
cp ouvrir-url.desktop ~/.local/share/file-manager/actions
```

Recharge Nautilus

```bash
nautilus -q
```


### Résultat

Maintenant, un **clic droit sur un fichier `.url`** te proposera directement l’option :
👉 **“Ouvrir fichier .url”**


Tu veux que je t’ajoute aussi une **icône personnalisée** (genre une petite icône de navigateur) pour que l’entrée ressorte mieux dans le menu ?
