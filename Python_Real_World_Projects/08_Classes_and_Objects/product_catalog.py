"""Challenge 24 - E-commerce Product Catalog."""

LOW_STOCK_LEVEL = 5


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - NGN {self.price} ({self.stock} in stock)"


if __name__ == "__main__":
    catalog = [Product("Keyboard", 12_000, 3),
               Product("Mouse", 6_500, 20),
               Product("Monitor", 85_000, 4),
               Product("USB Cable", 1_500, 50),
               Product("Webcam", 18_000, 5)]

    most_expensive = max(catalog, key=lambda p: p.price)
    print("Most expensive:", most_expensive)

    print("Low stock (< 5):")
    for product in catalog:
        if product.stock < LOW_STOCK_LEVEL:
            print("  ", product, "-> low stock")
