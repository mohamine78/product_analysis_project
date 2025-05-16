from analysis.stats import load_books, plot_price_histogram, plot_price_boxplot

def test_visuals():
    df = load_books('data/books.csv')
    plot_price_histogram(df)
    plot_price_boxplot(df)
    print("Histograme et boxplot créés dans data/")

if __name__ == "__main__":
    test_visuals()
