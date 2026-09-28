# Comment travailler dans Tertio

## Première fois (chaque membre)

1. **Cloner le dépôt ailleurs que dans Bureau ou Documents** (iCloud/OneDrive abîment le dossier `.git`) :
   ```
   mkdir -p ~/Projets && cd ~/Projets
   git clone https://github.com/Meganed777/Tertio.git
   cd Tertio
   ```
2. Se présenter à Git (courriel du compte GitHub) :
   ```
   git config --global user.name "Prénom Nom"
   git config --global user.email "courriel@exemple.com"
   ```
3. Installer les outils et activer le nettoyage automatique des notebooks :
   ```
   pip install -r requirements.txt
   nbstripout --install
   ```

## Chaque fois qu'on travaille

```
git switch main
git pull                              # récupérer le travail des autres
git switch -c scorie/isotherme-P      # une branche par tâche : equipe/sujet
# ... travailler dans SON dossier d'équipe ...
git add scorie/
git commit -m "Scorie : isotherme de Langmuir pour le P"
git push -u origin scorie/isotherme-P
```

Puis sur GitHub : bouton **Compare & pull request** → décrire le changement → demander une relecture → **Merge** une fois approuvé.
Ensuite : `git switch main && git pull`.

## Règles

1. **Personne ne pousse directement sur `main`.** Tout passe par une Pull Request.
2. **Chaque équipe travaille dans son dossier** (`scorie/`, `biochar/`, `sable/`, `integration/`). Toucher `commun/` ou `parametres/` → Pull Request relue par une autre équipe.
3. **Un notebook = un propriétaire.** On ne modifie pas le notebook de quelqu'un d'autre ; on en fait une copie ou on déplace le code dans le `.py`.
4. **Pas de `_v2`, `_v3`, `_final`, `_final2`.** Un seul fichier, Git garde l'historique (`git log -- fichier`).
5. **Aucune valeur partagée copiée à la main.** Débit, qualité d'eau, objectifs : on les lit dans `parametres/communs.yaml`.
6. **Le calcul validé va dans `<equipe>/<equipe>.py`** (fonction `dimensionner`). Ne pas changer ses entrées/sorties sans prévenir l'Intégration.
7. **Commits petits et fréquents**, message qui dit quoi : `Biochar : ajout du temps de contact` plutôt que `update`.
8. **Pas de gros fichiers** (> 50 Mo) ni de données confidentielles de DBO International sans accord.

## En cas de problème

- `git status` — voir où on en est (toujours commencer par ça).
- Conflit après un `git pull` : ouvrir le fichier, garder la bonne version entre les marqueurs `<<<<<<<` / `>>>>>>>`, puis `git add` et `git commit`. Si c'est un notebook, demander de l'aide avant de forcer quoi que ce soit.
- **Jamais de `git push --force` sur `main`.**
