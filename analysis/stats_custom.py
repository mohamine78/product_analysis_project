import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# Étape 5 – Chargement et nettoyage
def load_products_custom(filepath):
    df = pd.read_csv(filepath)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df.dropna(subset=["price"], inplace=True)
    return df

# Étape 6 – Statistiques
def describe_prices_custom(df):
    print(df["price"].describe())

def summary_by_source_custom(df):
    return df.groupby("source")["price"].describe()

# Étape 7 – Visualisations
def plot_price_histogram_custom(df):
    plt.figure()
    df["price"].hist(bins=20)
    plt.title("Histogramme des prix (Produits Custom)")
    plt.xlabel("Prix (€)")
    plt.ylabel("Nombre de produits")
    plt.savefig("data/histogram_price_custom.png")
    plt.close()

def plot_price_boxplot_custom(df):
    plt.figure()
    plt.boxplot(df["price"])
    plt.title("Boxplot des prix (Produits Custom)")
    plt.ylabel("Prix (€)")
    plt.savefig("data/boxplot_price_custom.png")
    plt.close()

def plot_price_clusters_custom(df):
    plt.figure()
    plt.scatter(df.index, df["price"], c=df["price_cluster"], cmap="viridis")
    plt.title("Clustering des prix (Produits Custom)")
    plt.xlabel("Index")
    plt.ylabel("Prix (€)")
    plt.savefig("data/clustering_price_custom.png")
    plt.close()

def plot_cluster_distribution_custom(df):
    plt.figure()
    sns.boxplot(x="price_cluster", y="price", data=df)
    plt.title("Boxplot par cluster de prix (Produits Custom)")
    plt.xlabel("Cluster")
    plt.ylabel("Prix (€)")
    plt.savefig("data/cluster_boxplot_custom.png")
    plt.close()

# Étape 8 – Clustering
def price_clustering_custom(df):
    model = KMeans(n_clusters=3, random_state=42, n_init='auto')
    df["price_cluster"] = model.fit_predict(df[["price"]])
    return df

def summary_by_cluster_custom(df):
    return df.groupby("price_cluster")["price"].describe()
