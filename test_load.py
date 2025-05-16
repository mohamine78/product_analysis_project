from analysis.stats import load_books

def test_load():
    df = load_books('data/books.csv')
    print(df.head())
    print(df.dtypes)

if __name__ == '__main__':
    test_load()

#tester etape 5 ppour verifier le float