"""Challenge 13 - Pharmacy Stock Reorder."""

REORDER_LEVEL = 5


def items_to_reorder(names, quantities, level=REORDER_LEVEL):
    """Return [(name, qty), ...] for stock below `level`, lowest stock first."""
    if len(names) != len(quantities):
        raise ValueError("Names and quantities lists must be the same length.")
    low = [(name, qty) for name, qty in zip(names, quantities) if qty < level]
    return sorted(low, key=lambda pair: (pair[1], pair[0]))


if __name__ == "__main__":
    names = ["Soap", "Bandage", "Gloves", "Syringe", "Mask"]
    quantities = [12, 3, 8, 1, 15]
    assert items_to_reorder(names, quantities) == [("Syringe", 1), ("Bandage", 3)]
    print(items_to_reorder(names, quantities))
    print(items_to_reorder(["A", "B"], [9, 10]))                    # nothing to reorder
    print(items_to_reorder(["A", "B", "C"], [0, 4, 4]))             # tie sorted by name
    try:
        items_to_reorder(["A"], [1, 2])
    except ValueError as err:
        print("Rejected:", err)
