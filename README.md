# HydroBioX — carnet de calcul

Système de traitement d'eau résidentiel passif et décentralisé — projet de fin de bacc, génie biotechnologique (Université de Sherbrooke), en partenariat avec DBO International.

## Structure

- `notebooks/carnet_calcul_design.ipynb` — carnet de calcul principal (dimensionnement, hydraulique, chauffage). Un seul fichier, son historique complet vit maintenant dans Git plutôt que dans des copies `_v1`, `_v2`, etc.
- `donnees/` — fiches techniques, données de référence (CSV, PDF de fournisseurs, etc.)
- `figures/` — graphiques exportés
- `rapports/` — livrables (Word/PDF) pour DBO International

## Installation

```
pip install -r requirements.txt
```

## Travailler avec le carnet (Git + Jupyter)

Les notebooks Jupyter stockent les résultats de chaque cellule (graphiques, texte) dans le fichier `.ipynb` lui-même. Sans précaution, chaque `git commit` inclut ces sorties et les diffs deviennent illisibles. Pour éviter ça, ce repo utilise **nbstripout**, qui retire automatiquement les sorties avant chaque commit.

Après avoir cloné le repo, chaque personne doit lancer une fois :

```
pip install -r requirements.txt
nbstripout --install
```

Ensuite, tout se fait normalement :

```
git pull                          # récupérer les changements de l'équipe
# ... travailler dans notebooks/carnet_calcul_design.ipynb ...
git add notebooks/carnet_calcul_design.ipynb
git commit -m "Description du changement"
git push
```

Pour voir un diff propre d'un notebook (cellule par cellule plutôt que du JSON brut) :

```
pip install nbdime
nbdiff notebooks/carnet_calcul_design.ipynb
```

## Conventions du carnet

- Tout en mm, sauf indication contraire.
- Section 0 = variables/constantes seulement (numérotées 0.1, 0.2, ...).
- Chaque section 1.x a sa théorie, sa démarche et ses sources numérotées, avant le code.
- Un changement de variable doit se propager automatiquement dans tout le carnet (ré-exécuter avec Kernel → Restart & Run All, ou `jupyter nbconvert --to notebook --execute`).
