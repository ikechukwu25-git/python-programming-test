"""Challenge 01 - Market Stall Sales Tracker."""

# --- Stated scenario ---------------------------------------------------------
rice_quantity = 8
rice_price = 42_500
noodle_quantity = 5
noodle_price = 9_800
delivery_cost = 12_000

gross_sales = rice_quantity * rice_price + noodle_quantity * noodle_price
net_revenue = gross_sales - delivery_cost
total_items = rice_quantity + noodle_quantity
# Matches the workbook example: gross sales spread over every item sold.
average_per_item = gross_sales / total_items

print("=== Stated scenario ===")
print(f"Gross sales: NGN {gross_sales}")
print(f"Net revenue: NGN {net_revenue}")
print(f"Average per item: NGN {average_per_item:.2f}")


# --- Extra test cases (same arithmetic, different numbers) --------------------
def sales_summary(rice_qty, rice_cost, noodle_qty, noodle_cost, delivery):
    """Return (gross, net, average_per_item); rejects bad inputs."""
    if min(rice_qty, rice_cost, noodle_qty, noodle_cost, delivery) < 0:
        raise ValueError("Quantities, prices and delivery cost cannot be negative.")
    items = rice_qty + noodle_qty
    if items == 0:
        raise ValueError("No items sold - cannot compute an average.")
    gross = rice_qty * rice_cost + noodle_qty * noodle_cost
    return gross, gross - delivery, gross / items


print("\n=== Extra cases ===")
for case in [(2, 40_000, 10, 9_000, 5_000), (0, 42_500, 4, 9_800, 0), (0, 0, 0, 0, 0)]:
    try:
        g, n, a = sales_summary(*case)
        print(f"{case} -> Gross {g}, Net {n}, Average {a:.2f}")
    except ValueError as err:
        print(f"{case} -> Error: {err}")
