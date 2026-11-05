"""Challenge 02 - Ride Fare Calculator."""

BASE_FARE = 900
PER_KM = 250
PER_MINUTE = 80
TAX_RATE = 0.075  # 7.5% service tax


def trip_fare(distance_km, minutes):
    """Return (fare_before_tax, total_after_tax)."""
    if distance_km < 0 or minutes < 0:
        raise ValueError("Distance and time cannot be negative.")
    fare = BASE_FARE + PER_KM * distance_km + PER_MINUTE * minutes
    total = fare + fare * TAX_RATE
    return fare, total


if __name__ == "__main__":
    for km, mins in [(12, 18), (5, 10), (0, 0), (30, 55)]:
        fare, total = trip_fare(km, mins)
        print(f"{km} km, {mins} min -> Fare: NGN {fare:.2f}; Total: NGN {total:.2f}")

    fare, total = trip_fare(12, 18)
    assert f"{fare:.2f}" == "5340.00" and f"{total:.2f}" == "5740.50"
    try:
        trip_fare(-1, 5)
    except ValueError as err:
        print("Rejected:", err)
