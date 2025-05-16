import requests
from bs4 import BeautifulSoup
from .book import Book

class BookScraper:
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

    def scrape_page(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erreur HTTP {response.status_code} pour {url}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        books = []

        articles = soup.select('article.product_pod')
        for article in articles:
            title = article.h3.a['title']
            price_str = article.select_one('p.price_color').text
            price = float(price_str.replace('£', '').replace('Â', ''))
            availability = article.select_one('p.instock.availability').text.strip()
            rating = article.p['class'][1]  # exemple : 'One', 'Two', etc.
            book = Book(title, price, availability, rating)
            books.append(book)
        return books

    def scrape_all(self, pages=50):
        all_books = []
        for i in range(1, pages + 1):
            url = self.BASE_URL.format(i)
            page_books = self.scrape_page(url)
            if not page_books: 
                break
            all_books.extend(page_books)
            print(f"Page {i} scrappée, {len(page_books)} livres")
        return all_books