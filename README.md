# FAB Life Counter

Petit compteur de vie pour Flesh and Blood, pensé pour un écran noir et blanc en mode lecture, avec deux compteurs côte à côte.

## Ce qu'il fait

- Deux joueurs avec compteur séparé
- Zone gauche pour décrémenter et zone droite pour incrémenter
- Palette minimaliste noir/blanc, lisible sur écran e-ink
- Décor médiéval sur les bords seulement pour garder le centre clair
- Reset rapide par joueur
- Compatible avec un simple serveur local ou un affichage depuis le navigateur

## Lancer localement

### Option 1 : ouvrir directement dans le navigateur

- Ouvrir le fichier `index.html` dans un navigateur moderne.

### Option 2 : lancer un petit serveur local

Depuis le dossier du projet :

```bash
python -m http.server 8000
```

Puis ouvrir :

```text
http://localhost:8000
```

## Kindle

Pour un Kindle, le plus fiable est de l'utiliser via le navigateur du Kindle sur le réseau local, ou de lancer un petit serveur sur un ordinateur connecté au même réseau.

L'EPUB n'est pas adapté à un compteur interactif en temps réel. Ce projet est donc optimisé pour un usage web local, qui reste le plus pratique sur un appareil Kindle.

## Personnalisation

- Modifie la valeur initiale dans `script.js` via `STARTING_LIFE`
- Ajuste le style dans `styles.css` pour l'esthétique e-ink ou le format de l'écran
- Ajoute un fond plus ancien ou plus minimal selon le rendu souhaité
