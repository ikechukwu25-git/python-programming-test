"""Challenge 03 - Electricity Token Budget."""

UNIT_PRICE = 145
TRANSACTION_FEE = 350


def token_budget(budget, unit_price=UNIT_PRICE, fee=TRANSACTION_FEE):
    """Return (whole_units, money_left). No purchase -> nothing is charged."""
    if budget < 0:
        raise ValueError("Budget cannot be negative.")
    spendable = budget - fee
    if spendable < unit_price:          # cannot afford even one unit plus the fee
        return 0, budget
    units = spendable // unit_price     # floor division
    leftover = spendable % unit_price   # modulo
    return units, leftover


if __name__ == "__main__":
    assert token_budget(18_000) == (121, 105)
    for amount in (18_000, 5_000, 500, 300, 0):
        units, left = token_budget(amount)
        print(f"Budget NGN {amount}: Units: {units}; Balance: NGN {left}")
