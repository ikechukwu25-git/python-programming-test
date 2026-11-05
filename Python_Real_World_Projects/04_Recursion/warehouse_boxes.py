"""Challenge 10 - Warehouse Box Counter (recursion)."""


def count_items(box):
    """Sum every item count in a box that may contain nested boxes (lists)."""
    if isinstance(box, list):
        return sum(count_items(content) for content in box)   # recursive case
    if isinstance(box, bool) or not isinstance(box, (int, float)):
        raise TypeError(f"Invalid warehouse content: {box!r}")
    if box < 0:
        raise ValueError("Item counts cannot be negative.")
    return box                                                 # base case: a number


if __name__ == "__main__":
    assert count_items([4, [2, 3], [1, [5]]]) == 15
    assert count_items([]) == 0
    assert count_items([[[[7]]]]) == 7
    print(count_items([4, [2, 3], [1, [5]]]))   # 15
    print(count_items([]))                      # 0
    print(count_items([[[[7]]], 3, [[], [2]]])) # 12
    try:
        count_items([1, "box"])
    except TypeError as err:
        print("Rejected:", err)
