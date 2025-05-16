# Product Analysis Project

Ce projet collecte de données produits, réalise une analyse statistique et un clustering des prix, et génère des graphiques.

## Structure du projet

- `scraper/`  
  Contient le script `scraper_custom.py` pour la récupération de données produits et exporter un fichier CSV.

- `analysis/`  
  Contient les scripts d’analyse (`stats_custom.py`) pour le nettoyage, les statistiques, le clustering et la visualisation.

- `data/`  
  Dossier où sont sauvegardés les fichiers CSV générés et les graphiques PNG.

- `main_custom.py`  
  Script principal pour lancer la génération des données, l’analyse et la création des graphiques.

## Installation

1. Cloner le dépôt  
   ```bash
   git clone <URL>
   cd product_analysis_project

Créer un environnement virtuel et installer les dépendances
        python3 -m venv venv
        source venv/bin/activate  # macOS/Linux
        venv\Scripts\activate     # Windows

        pip install -r requirements.txt


bash
Copy
Edit


python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
Usage
Lancer le script principal depuis la racine du projet :

bash
Copy
Edit
python main_custom.py
Cela va :

Simuler 250 produits et les exporter dans data/custom_products.csv

Charger les données, effectuer un clustering des prix

Afficher des statistiques dans la console

Générer des graphiques dans le dossier data/

Dossier data
Ce dossier contient tous les fichiers générés :

Les CSV des produits

Les images des graphiques (histogrammes, boxplots, clustering, etc.)

Remarques
S'Assurer que le dossier data existe à la racine avant de lancer le script

Dépendances principales
pandas
matplotlib
seaborn
scikit-learn
faker

Auteur
HARNOUFI MOHAMMED, LE 16/05/2025