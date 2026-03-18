# Global Retail Performance Dashboard

Ce projet vise à construire un dashboard interactif pour analyser la performance d’un retailer mondial à partir du dataset Superstore.

## Structure du projet

- `data/raw/` : Données brutes (ex: superstore.csv)
- `data/processed/` : Données nettoyées et prêtes à l’analyse
- `notebooks/` : Analyses exploratoires et visualisations (Jupyter)
- `scripts/` : Scripts Python pour le nettoyage et la préparation des données
- `reports/` : Screenshots du dashboard et synthèse des insights
- `sas_va/` : Documentation sur le dashboard SAS Visual Analytics

## Objectifs business
- Où fait-on le plus de chiffre ?
- Quels produits sont rentables ?
- Les remises sont-elles dangereuses ?
- Quels clients rapportent le plus ?

## Démarrage rapide
1. Créer un environnement virtuel Python :
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Placer le fichier `superstore.csv` dans `data/raw/`
4. Lancer le script de nettoyage : `python scripts/data_cleaning.py`
5. Explorer les analyses dans `notebooks/data_analysis.ipynb`
6. Importer les données propres dans SAS Visual Analytics

## Auteurs
- Fouad MOUTAIROU
