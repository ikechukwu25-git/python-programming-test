"""Challenge 19 - Supermarket Basket Checkout."""


def checkout(prices, basket):
    """Return (total, missing_products). Missing items are not charged."""
    for product, qty in basket.items():
        if qty < 0:
            raise ValueError(f"Negative quantity for {product!r}.")
    total = 0
    missing = []
    for product, qty in basket.items():
        if product in prices:
            total += prices[product] * qty
        else:
            missing.append(product)
    return total, missing


if __name__ == "__main__":
    prices = {"rice": 3000, "oil": 2000}
    assert checkout(prices, {"rice": 2, "salt": 1}) == (6000, ["salt"])
    print(checkout(prices, {"rice": 2, "salt": 1}))
    print(checkout(prices, {}))
    print(checkout(prices, {"rice": 1, "oil": 3, "sugar": 2, "beans": 1}))
    try:
        checkout(prices, {"rice": -1})
    except ValueError as err:
        print("Rejected:", err)
