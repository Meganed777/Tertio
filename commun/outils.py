"""Outils partagés par toutes les équipes."""
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parents[1]


def charger_parametres(chemin: str | Path | None = None) -> dict:
    """Lit parametres/communs.yaml et retourne un dict.

    Usage dans un notebook (placé dans <equipe>/notebooks/) :

        import sys; sys.path.insert(0, "../..")
        from commun.outils import charger_parametres
        P = charger_parametres()
        Q = P["debit_conception_m3_j"]
    """
    chemin = Path(chemin) if chemin else RACINE / "parametres" / "communs.yaml"
    with open(chemin, encoding="utf-8") as f:
        return yaml.safe_load(f)
