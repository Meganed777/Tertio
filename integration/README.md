# Équipe Intégration

**Responsables :** *(noms à compléter)*

## Rôle

- Tenir à jour `parametres/communs.yaml` (débit, qualité d'eau brute, objectifs de rejet).
- Enchaîner les modules dans `integration.py` et vérifier que l'eau finale respecte les objectifs.
- Dimensionner les éléments du système global (cuve, chauffage, isolation, hydraulique).
- Relire les Pull Requests des autres équipes qui touchent à une interface.

## Contenu

- `integration.py` — train de traitement complet (Scorie → Biochar → Sable)
- `notebooks/calcul_design.ipynb` — carnet de calcul du design (cuve, chauffage, régulateur, isolant)
- `donnees/` — fiches techniques et prix fournisseurs

## Lancer la simulation complète

Depuis la racine du dépôt :

```
python -m integration.integration
```

(Fonctionne une fois que les trois modules ont implémenté `dimensionner`.)
