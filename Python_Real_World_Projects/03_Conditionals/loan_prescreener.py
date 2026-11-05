"""Challenge 09 - Loan Application Pre-Screener.

Programming simulation only - this is NOT financial advice.
"""

MIN_AGE = 21
MIN_INCOME = 80_000
MAX_DEBT_PERCENT = 40


def prescreen(age, income, debt):
    """Return (eligible, list_of_failed_conditions)."""
    if age < 0 or income < 0 or debt < 0:
        raise ValueError("Age, income and debt cannot be negative.")
    failures = []
    if age < MIN_AGE:
        failures.append("age below 21")
    if income < MIN_INCOME:
        failures.append("income below NGN 80,000")
    # debt <= 40% of income, written with integers to avoid float rounding
    if debt * 100 > income * MAX_DEBT_PERCENT:
        failures.append("debt ratio too high")
    return len(failures) == 0, failures


def describe(age, income, debt):
    eligible, failures = prescreen(age, income, debt)
    return "Eligible" if eligible else "Not eligible: " + "; ".join(failures)


def ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


if __name__ == "__main__":
    assert describe(24, 100_000, 45_000) == "Not eligible: debt ratio too high"
    for case in [(24, 100_000, 45_000), (30, 100_000, 40_000), (19, 50_000, 30_000), (21, 80_000, 0)]:
        print(f"age={case[0]}, income={case[1]}, debt={case[2]} -> {describe(*case)}")

    print("\n--- Live pre-screen ---")
    raw = ask("Age: ")
    if raw is not None:
        try:
            age = int(raw)
            income = float(ask("Monthly income (NGN): "))
            debt = float(ask("Existing monthly debt (NGN): "))
            print(describe(age, income, debt))
        except (ValueError, TypeError) as err:
            print("Invalid input:", err)
