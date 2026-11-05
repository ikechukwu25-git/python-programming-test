"""Challenge 25 - Digital Wallet."""


class Wallet:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self._balance = balance

    @staticmethod
    def _check_amount(amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def deposit(self, amount):
        self._check_amount(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._check_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    wallet = Wallet("Ada", 10_000)
    wallet.deposit(5_000)
    wallet.withdraw(3_000)
    assert wallet.get_balance() == 12_000
    print(f"{wallet.owner}'s balance: NGN {wallet.get_balance()}")

    for action, amt in [("deposit", 0), ("withdraw", -50), ("withdraw", 999_999), ("deposit", "lots")]:
        try:
            getattr(wallet, action)(amt)
        except ValueError as err:
            print(f"{action}({amt!r}) -> Rejected: {err}")
    print("Balance unchanged:", wallet.get_balance())
