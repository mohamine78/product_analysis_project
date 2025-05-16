import csv

def export_products_to_csv_custom(products, filepath):
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "source"])
        writer.writeheader()
        for product in products:
            writer.writerow(product.to_dict())
