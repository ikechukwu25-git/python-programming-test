"""Challenge 11 - Savings Growth by Month (recursion, no loops)."""

FIRST_DEPOSIT = 5_000
MONTHLY_INCREASE = 1_000


def total_savings(months):
    """Total deposits after `months` months."""
    if isinstance(months, bool) or not isinstance(months, int):
        raise TypeError("Months must be a whole number.")
    if months < 0:
        raise ValueError("Months cannot be negative.")
    if months == 0:                                   # base case
        return 0
    this_month = FIRST_DEPOSIT + MONTHLY_INCREASE * (months - 1)
    return this_month + total_savings(months - 1)     # recursive case


if __name__ == "__main__":
    assert total_savings(4) == 26_000
    assert total_savings(0) == 0
    assert total_savings(1) == 5_000
    for n in (0, 1, 4, 12):
        print(f"total_savings({n}) -> {total_savings(n)}")
    try:
        total_savings(-3)
    except ValueError as err:
        print("Rejected:", err)
