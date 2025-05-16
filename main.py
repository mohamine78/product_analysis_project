from scraper.scraper_custom import get_cdiscount_data

def main():
    print("[*] Démarrage du scraping jeux PS5 sur Cdiscount...")
    data = get_cdiscount_data()
    print(f"[+] {len(data)} produits récupérés et sauvegardés dans data/custom_products.csv")

if __name__ == "__main__":
    main()
