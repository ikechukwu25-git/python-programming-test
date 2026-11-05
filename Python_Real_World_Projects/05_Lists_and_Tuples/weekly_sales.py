"""Challenge 15 - Weekly Sales Analysis."""


def analyse_sales(sales):
    """Return (total, average, highest_day_index, lowest_day_index) (zero-based)."""
    if not sales:
        raise ValueError("No sales data supplied.")
    if any(value < 0 for value in sales):
        raise ValueError("Sales figures cannot be negative.")
    total = sum(sales)
    average = round(total / len(sales), 2)
    return total, average, sales.index(max(sales)), sales.index(min(sales))


if __name__ == "__main__":
    week = [200, 350, 150, 400, 300, 250, 350]
    assert analyse_sales(week) == (2000, 285.71, 3, 2)
    print(analyse_sales(week))
    print(analyse_sales([100] * 7))                      # all equal -> first day
    print(analyse_sales([0, 0, 0, 0, 0, 0, 5000]))
    for bad in ([], [10, -5, 3]):
        try:
            analyse_sales(bad)
        except ValueError as err:
            print(f"{bad} -> Rejected: {err}")
