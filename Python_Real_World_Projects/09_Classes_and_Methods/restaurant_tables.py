"""Challenge 26 - Restaurant Table Reservations."""


class RestaurantTable:
    def __init__(self, number, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.number = number
        self.capacity = capacity
        self._party_size = 0       # 0 means available

    def reserve(self, party_size):
        if party_size <= 0:
            return "invalid party size"
        if self._party_size:
            return "already reserved"
        if party_size > self.capacity:
            return f"party too large (capacity {self.capacity})"
        self._party_size = party_size
        return "success"

    def cancel(self):
        if not self._party_size:
            return "no reservation to cancel"
        self._party_size = 0
        return "reservation cancelled"

    def status(self):
        if self._party_size:
            return f"Table {self.number}: reserved for {self._party_size}"
        return f"Table {self.number}: available (seats {self.capacity})"


if __name__ == "__main__":
    table = RestaurantTable(4, 6)
    assert table.reserve(5) == "success"
    assert table.reserve(2) == "already reserved"
    print(table.status())
    print(table.cancel())
    print(table.status())
    print("Reserve 8 on a 6-seater:", table.reserve(8))
    print("Reserve 0:", table.reserve(0))
    print("Cancel when empty:", table.cancel())
    print("Rebook after cancel:", table.reserve(2))
