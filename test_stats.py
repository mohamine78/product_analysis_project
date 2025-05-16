from analysis.stats import load_books, describe_prices, availability_counts, summary_by_rating

def test_stats():
    df = load_books('data/books.csv')
    describe_prices(df)
    availability_counts(df)
    summary_by_rating(df)

if __name__ == '__main__':
    test_stats()
