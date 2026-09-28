"""Intégration — enchaîne les modules Scorie -> Biochar -> Sable.

L'eau qui sort d'une étape devient l'eau qui entre dans la suivante.
L'ordre du train de traitement est défini ici (à confirmer en équipe).
"""
from commun.outils import charger_parametres
import scorie.scorie as scorie
import biochar.biochar as biochar
import sable.sable as sable

TRAIN = [("Scorie", scorie), ("Biochar", biochar), ("Sable", sable)]


def simuler(params: dict | None = None) -> list[dict]:
    """Fait passer l'eau brute à travers toutes les étapes.

    Retourne une liste de résultats, un par étape.
    """
    params = params or charger_parametres()
    debit = params["debit_conception_m3_j"]
    eau = dict(params["eau_brute"])
    resultats = []
    for nom, module in TRAIN:
        res = module.dimensionner(debit, eau, params)
        res["etape"] = nom
        resultats.append(res)
        eau = res["eau_sortie"]
    return resultats


if __name__ == "__main__":
    for r in simuler():
        print(r["etape"], "->", r["eau_sortie"])
