# scraper/scraper_custom.py

import os
import csv
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPAPI_KEY")

class ProductScraper:
    def __init__(self, query="jeux de console", output_path="data/custom_products.csv"):
        self.query = query
        self.output_path = output_path

    def scrape_with_serpapi(self):
        if not API_KEY:
            raise ValueError("Clé API SerpAPI manquante")

        params = {
            "engine": "google_shopping",
            "q": self.query,
            "hl": "fr",
            "gl": "fr",
            "api_key": API_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        products = results.get("shopping_results", [])

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        with open(self.output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "price", "source"])
            writer.writeheader()
            for product in products:
                title = product.get("title")
                price = product.get("price")
                source = product.get("source", "Google Shopping")
                if title and price:
                    writer.writerow({
                        "title": title,
                        "price": price.replace("€", "").replace(",", "."),
                        "source": source
                    })

        print(f"✅ {len(products)} produits enregistrés dans {self.output_path}")
