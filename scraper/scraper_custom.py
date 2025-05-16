import csv
import random
from faker import Faker
import os

class Product:
    def __init__(self, title, price, source):
        self.title = title
        self.price = price
        self.source = source

    def to_dict(self):
        return {"title": self.title, "price": self.price, "source": self.source}


class ProductScraper:
    def __init__(self):
        self.fake = Faker()
        self.products = []

    def simulate_scraping(self, n=250):
        game_titles = [
            "The Legend of Zelda", "FIFA 24", "Call of Duty", "Minecraft", "Elden Ring",
            "Hogwarts Legacy", "Fortnite", "Animal Crossing", "Mario Kart", "Assassin’s Creed",
            "Cyberpunk 2077", "Baldur's Gate 3", "GTA V", "Starfield", "Red Dead Redemption 2"
        ]

        for _ in range(n):
            title = random.choice(game_titles) + " - " + self.fake.word().capitalize()
            price = round(random.uniform(10.0, 80.0), 2)
            source = "Google Shopping"
            product = Product(title, price, source)
            self.products.append(product)

    def export_to_csv(self, filename="data/custom_products.csv"):
        # Créer dossier data si pas deja le cas
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "price", "source"])
            writer.writeheader()
            for product in self.products:
                writer.writerow(product.to_dict())


if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.simulate_scraping(n=250)
    scraper.export_to_csv("data/custom_products.csv")
    print("✅ 250 produits simulés exportés dans data/custom_products.csv")
