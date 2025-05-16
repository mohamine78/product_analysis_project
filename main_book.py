import csv
import os
from scraper.scraper_books import BookScraper

def save_books_to_csv(books, filename='data/books.csv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Titre', 'Prix', 'Disponibilité', 'Note'])
        for book in books:
            writer.writerow([book.title, book.price, book.availability, book.rating])
    print(f"[✓] Données sauvegardées dans {filename}")

def main():
    print("[*] Démarrage du scraping des livres...")
    scraper = BookScraper()
    books = scraper.scrape_all(pages=5) 

    print(f"[✓] {len(books)} livres récupérés.")
    save_books_to_csv(books)

if __name__ == "__main__":
    main()
