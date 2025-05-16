import csv

def export_books_to_csv(books, filename="data/books.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "availability", "rating"])
        writer.writeheader()
        for book in books:
            writer.writerow(book.to_dict())
    print(f"{len(books)} livres exportés dans {filename}")