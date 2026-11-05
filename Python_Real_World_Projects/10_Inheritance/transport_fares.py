"""Challenge 28 - Transport Fare System."""


class Vehicle:
    def __init__(self, plate_number, distance_km):
        if not plate_number:
            raise ValueError("Plate number is required.")
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")
        self.plate_number = plate_number
        self.distance_km = distance_km

    def fare(self):
        raise NotImplementedError("Subclasses must define their own fare().")


class Bike(Vehicle):
    def __init__(self, plate_number, distance_km):
        super().__init__(plate_number, distance_km)

    def fare(self):
        return 300 + 100 * self.distance_km


class Van(Vehicle):
    def __init__(self, plate_number, distance_km):
        super().__init__(plate_number, distance_km)

    def fare(self):
        return 1_000 + 250 * self.distance_km


if __name__ == "__main__":
    assert Bike("BK1", 10).fare() == 1300
    assert Van("VN1", 10).fare() == 3500
    for vehicle in (Bike("BK1", 10), Van("VN1", 10), Bike("BK2", 0), Van("VN2", 42.5)):
        print(f"{type(vehicle).__name__} {vehicle.plate_number}, {vehicle.distance_km} km -> NGN {vehicle.fare()}")
    try:
        Vehicle("XX", 5).fare()
    except NotImplementedError as err:
        print("Base class:", err)
