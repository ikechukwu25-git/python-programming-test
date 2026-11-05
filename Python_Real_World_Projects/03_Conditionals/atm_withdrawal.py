"""Challenge 07 - Bank ATM Withdrawal."""

BALANCE = 52_000
DAILY_REMAINING = 30_000


def process_withdrawal(balance, daily_remaining, amount):
    """Return (approved, message, new_balance). Checks run in a logical order."""
    if amount <= 0:
        return False, "Declined: amount must be greater than zero.", balance
    elif amount % 1000 != 0:
        return False, "Declined: amount must be a multiple of NGN 1,000.", balance
    elif amount > balance:
        return False, "Declined: insufficient funds.", balance
    elif amount > daily_remaining:
        return False, "Declined: daily withdrawal limit exceeded.", balance
    else:
        new_balance = balance - amount
        return True, f"Approved. New balance: NGN {new_balance}", new_balance


def ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


if __name__ == "__main__":
    assert process_withdrawal(BALANCE, DAILY_REMAINING, 25_000)[1] == "Approved. New balance: NGN 27000"
    for amt in (25_000, 0, -4000, 2_500, 60_000, 35_000):
        print(f"{amt:>7} -> {process_withdrawal(BALANCE, DAILY_REMAINING, amt)[1]}")

    print("\n--- Live ATM ---")
    raw = ask("Enter withdrawal amount (NGN): ")
    if raw is not None:
        try:
            amount = int(raw.replace(",", "").strip())
        except ValueError:
            print("Declined: please enter a whole number.")
        else:
            print(process_withdrawal(BALANCE, DAILY_REMAINING, amount)[1])
