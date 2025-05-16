from scraper.scraper_custom import ProductScraper
from analysis import stats_custom as sc

if __name__ == "__main__":
    csv_path = "data/custom_products.csv"

    # 1. Simuler le scraping et exporter CSV dans data/
    scraper = ProductScraper()
    scraper.simulate_scraping(n=250)
    scraper.export_to_csv(csv_path)
    print(f"✅ 250 produits simulés exportés dans {csv_path}")

    # 2. Charger les données
    df = sc.load_products_custom(csv_path)

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

    print("\ Analyse terminée, fichiers crées dans le dossier data/")
