"""Module Scorie — calculs officiels de l'équipe Scorie.

Ce fichier contient le calcul « final » du module. Les notebooks de
`scorie/notebooks/` servent à explorer ; quand un calcul est validé,
on le déplace ici pour que l'équipe Intégration puisse l'utiliser.

NE PAS changer la signature de `dimensionner` ni les clés retournées
sans en parler à l'équipe Intégration (voir scorie/README.md).
"""


def dimensionner(debit_m3_j: float, eau_entree: dict, params: dict) -> dict:
    """Dimensionne l'étape Scorie.

    Entrées
    -------
    debit_m3_j : débit de conception (m3/jour), vient de parametres/communs.yaml
    eau_entree : qualité de l'eau qui ENTRE dans l'étape, mêmes clés que
                 `eau_brute` dans parametres/communs.yaml (ex. "PO4_mg_L")
    params     : tout le contenu de parametres/communs.yaml

    Sortie (dict)
    -------------
    eau_sortie : dict, qualité de l'eau qui SORT (mêmes clés que eau_entree)
    volume_L   : volume de média / de l'unité (L)
    dimensions_cm : dict, ex. {"diametre": ..., "hauteur": ...}
    cout_cad   : coût estimé ($ CAD)
    notes      : str, hypothèses importantes
    """
    raise NotImplementedError("Module Scorie pas encore implémenté")
