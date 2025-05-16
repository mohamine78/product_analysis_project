# main_custom.py

from scraper.scraper_custom import ProductScraper
from analysis import stats_custom as sc

if __name__ == "__main__":
    # 1. Scraper depuis Google Shopping
    scraper = ProductScraper(query="jeu de console")
    scraper.scrape_with_serpapi()

    # 2. Charger les données
    df = sc.load_products_custom("data/custom_products.csv")

    # 3. Clustering des prix
    df = sc.price_clustering_custom(df)

    # 4. Afficher des statistiques
    print("\n=== Description des prix ===")
    sc.describe_prices_custom(df)

    print("\n=== Résumé par source ===")
    print(sc.summary_by_source_custom(df))

    print("\n=== Résumé par cluster de prix ===")
    print(sc.summary_by_cluster_custom(df))

    # 5. Générer les graphiques
    sc.plot_price_histogram_custom(df)
    sc.plot_price_boxplot_custom(df)
    sc.plot_price_clusters_custom(df)
    sc.plot_cluster_distribution_custom(df)

    print("\\ Analyse terminée, fichiers crée dans data/")
