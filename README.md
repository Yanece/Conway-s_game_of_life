
# Conway's Game of Life in Python

## Objectif
Simuler le Jeu de la Vie de Conway sur une grille 7x7 en Python.
Chaque cellule peut être vivante (`1`) ou morte (`0`) et évolue selon ses 8 voisins en suivant les règles classiques :

- Une cellule morte avec exactement 3 voisins vivants devient vivante (naissance).
- Une cellule vivante avec 2 ou 3 voisins vivants reste vivante, sinon elle meurt.


## Installation
1. Installer Python 3.
2. Créer un environnement virtuel (optionnel) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
