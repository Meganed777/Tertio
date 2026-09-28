# Équipe Biochar

**Responsables :** *(noms à compléter)*
**État :** exploration

## Rôle dans le système

*(Une ou deux phrases : quel contaminant cette étape retire, et comment.)*

## Contenu du dossier

- `biochar.py` — calcul officiel du module (fonction `dimensionner`), utilisé par l'Intégration
- `notebooks/` — exploration, essais, figures
- `donnees/` — données de laboratoire, fiches techniques, articles de référence

## Interface (le « contrat » avec l'Intégration)

| | Clé | Unité | Description |
|---|---|---|---|
| Entrée | `debit_m3_j` | m³/j | débit de conception |
| Entrée | `eau_entree[...]` | voir `parametres/communs.yaml` | qualité de l'eau à l'entrée |
| Sortie | `eau_sortie[...]` | mêmes clés et unités | qualité de l'eau à la sortie |
| Sortie | `volume_L` | L | volume de l'unité |
| Sortie | `dimensions_cm` | cm | dimensions principales |
| Sortie | `cout_cad` | $ CAD | coût estimé |

*(Ajouter ici les paramètres propres au module — ex. temps de contact, granulométrie, capacité d'adsorption — avec leurs unités et sources.)*

## Hypothèses et sources

1. *(à compléter)*
