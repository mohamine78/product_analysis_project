from analysis.stats import load_books, price_clustering, summary_by_cluster, plot_price_clusters, plot_cluster_distribution

def test_clustering():
    df = load_books('data/books.csv')
    df = price_clustering(df)
    print(summary_by_cluster(df))
    plot_price_clusters(df)
    plot_cluster_distribution(df)
    print("Graphiques clustering générés dans data/")

if __name__ == "__main__":
    test_clustering()
