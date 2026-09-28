# Tertio — HydroBioX

Système de traitement d'eau résidentiel passif et décentralisé. Projet de fin de bacc en génie biotechnologique (Université de Sherbrooke), en partenariat avec DBO International.

Quatre équipes travaillent en parallèle ; leurs modules seront ensuite enchaînés en un seul train de traitement :

```
eau brute ──► Scorie ──► Biochar ──► Sable ──► eau traitée
                    (enchaînés par l'équipe Intégration)
```

## Structure

| Dossier | Contenu | Qui modifie |
|---|---|---|
| `scorie/` | module Scorie : `scorie.py`, notebooks, données | équipe Scorie |
| `biochar/` | module Biochar | équipe Biochar |
| `sable/` | module Sable | équipe Sable |
| `integration/` | `integration.py` (enchaînement), carnet `calcul_design.ipynb` (cuve, chauffage, isolation) | équipe Intégration |
| `parametres/communs.yaml` | débit, qualité d'eau brute, objectifs : **source unique** | par Pull Request |
| `commun/` | fonctions et données partagées | par Pull Request |
| `rapports/` | livrables pour DBO International, figures finales | tous |

Chaque dossier d'équipe a un `README.md` qui décrit son **interface** : ce que le module reçoit et ce qu'il retourne. C'est ce contrat qui permet de tout assembler à la fin.

## Comment ça s'assemble

Chaque équipe expose une fonction dans `<equipe>/<equipe>.py` :

```python
def dimensionner(debit_m3_j, eau_entree, params) -> dict:
    ...
    return {"eau_sortie": {...}, "volume_L": ..., "dimensions_cm": {...}, "cout_cad": ..., "notes": "..."}
```

`integration/integration.py` fait passer l'eau d'une étape à l'autre : la sortie de Scorie devient l'entrée de Biochar, et ainsi de suite. Les notebooks servent à explorer ; le calcul validé va dans le `.py`.

## Démarrer

Voir **[CONTRIBUTING.md](CONTRIBUTING.md)** : installation, branches, Pull Requests et règles de l'équipe.

```
pip install -r requirements.txt
nbstripout --install
```

## Conventions

- L'unité est dans le nom de la variable : `debit_m3_j`, `PO4_mg_L`, `hauteur_cm`.
- Les valeurs partagées ne sont jamais recopiées : on les lit avec `charger_parametres()` (voir `commun/outils.py`).
- Chaque section de notebook a sa théorie, sa démarche et ses sources numérotées, avant le code.
- Un changement de variable doit se propager dans tout le carnet (Kernel → Restart & Run All).
