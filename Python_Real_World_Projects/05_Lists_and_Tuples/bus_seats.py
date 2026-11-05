"""Challenge 14 - Bus Seat Booking."""

TOTAL_SEATS = 12


def available_seats(booked):
    return tuple(seat for seat in range(1, TOTAL_SEATS + 1) if seat not in booked)


def book_seat(booked, seat_no):
    """Try to book a seat. Returns (message, available_seats_tuple)."""
    if isinstance(seat_no, bool) or not isinstance(seat_no, int):
        return "Invalid seat number", available_seats(booked)
    if not 1 <= seat_no <= TOTAL_SEATS:
        return f"Out of range (seats are 1-{TOTAL_SEATS})", available_seats(booked)
    if seat_no in booked:
        return "Already booked", available_seats(booked)
    booked.append(seat_no)
    return f"Seat {seat_no} booked", available_seats(booked)


if __name__ == "__main__":
    booked = [2, 5]
    msg, free = book_seat(booked, 5)
    assert msg == "Already booked" and booked == [2, 5]
    print(msg, free)
    for seat in (7, 0, 13, 7, "3"):
        msg, free = book_seat(booked, seat)
        print(f"book_seat(booked, {seat!r}) -> {msg}; available: {free}")
    print("Booked list:", booked)
