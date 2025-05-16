import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def load_books(filepath):

    df = pd.read_csv(filepath)

    df['price'] = df['price'].astype(str).str.replace('[^0-9.]', '', regex=True)
    df['price'] = df['price'].astype(float)

    df['availability'] = df['availability'].str.strip()

    return df


def describe_prices(df: pd.DataFrame):
    description = df['price'].describe()
    print(description)

def availability_counts(df: pd.DataFrame):
    print("Disponibilité générale :")
    print(df['availability'].value_counts())
    print("\nDisponibilité par rating :")
    print(df.groupby('rating')['availability'].value_counts())

def summary_by_rating(df: pd.DataFrame):
    summary = df.groupby('rating')['price'].mean()
    print("Prix moyen par rating :")
    print(summary)



def plot_price_histogram(df):
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogramme des prix')
    plt.xlabel('Prix')
    plt.ylabel('Nombre de livres')
    plt.savefig('data/histogram_price.png')
    plt.close()

def plot_price_boxplot(df):
    plt.boxplot(df['price'])
    plt.title('Boxplot des prix')
    plt.ylabel('Prix')
    plt.savefig('data/boxplot_price.png')
    plt.close()

def plot_price_clusters(df):
    if 'price_cluster' not in df.columns:
        print("Erreur : La colonne 'price_cluster' n'existe pas. Faire l'étape 8 d'abord.")
        return
    colors = ['red', 'green', 'blue']
    for cluster in sorted(df['price_cluster'].unique()):
        cluster_data = df[df['price_cluster'] == cluster]
        plt.scatter(cluster_data.index, cluster_data['price'], color=colors[cluster], label=f'Cluster {cluster}')
    plt.title('Clustering des prix')
    plt.xlabel('Index')
    plt.ylabel('Prix')
    plt.legend()
    plt.savefig('data/clustering_price.png')
    plt.close()

def plot_cluster_distribution(df):
    if 'price_cluster' not in df.columns:
        print("Erreur : La colonne 'price_cluster' n'existe pas. Faire l'étape 8 d'abord.")
        return
    df.boxplot(column='price', by='price_cluster', grid=False)
    plt.title('Distribution des prix par cluster')
    plt.suptitle('')
    plt.xlabel('Cluster')
    plt.ylabel('Prix')
    plt.savefig('data/cluster_boxplot.png')
    plt.close()

    


def price_clustering(df, n_clusters=3):
    X = df[['price']]
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    df['price_cluster'] = model.fit_predict(X)
    return df

def summary_by_cluster(df):
    return df.groupby('price_cluster')['price'].describe()




    