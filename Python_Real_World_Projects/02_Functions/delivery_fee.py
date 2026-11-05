"""Challenge 04 - Food Delivery Fee Estimator."""

BASE_FEE = 500
PER_KM = 150
FREE_DELIVERY_THRESHOLD = 15_000


def calculate_delivery(order_amount, distance_km):
    """Return the delivery fee (a number; nothing is printed here)."""
    if order_amount < 0 or distance_km < 0:
        raise ValueError("Order amount and distance cannot be negative.")
    if order_amount >= FREE_DELIVERY_THRESHOLD:
        return 0
    return BASE_FEE + PER_KM * distance_km


if __name__ == "__main__":
    tests = [(12_000, 4, 1100), (15_000, 4, 0), (5_000, 10, 2000),
             (14_999, 0, 500), (20_000, 25, 0)]
    for amount, km, expected in tests:
        fee = calculate_delivery(amount, km)
        assert fee == expected, (amount, km, fee)
        print(f"calculate_delivery({amount}, {km}) -> {fee}")
    try:
        calculate_delivery(-1, 3)
    except ValueError as err:
        print("Rejected:", err)
