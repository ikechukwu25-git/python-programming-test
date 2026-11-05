"""Challenge 20 - Class Attendance Register."""


def mark_present(attendance, name):
    """Increment an existing student or add a new one; returns the register."""
    name = name.strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    attendance[name] = attendance.get(name, 0) + 1
    return attendance


def top_attendee(attendance):
    """Name with the highest count (ties -> alphabetical); None if empty."""
    if not attendance:
        return None
    return min(attendance, key=lambda student: (-attendance[student], student))


if __name__ == "__main__":
    register = {"Ada": 4, "Bola": 2}
    mark_present(register, "Bola")
    assert register == {"Ada": 4, "Bola": 3}
    print(register, "-> top:", top_attendee(register))

    mark_present(register, "Chidi")
    mark_present(register, "Ada")
    print(register, "-> top:", top_attendee(register))

    tie = {"Zainab": 3, "Efe": 3, "Musa": 1}
    print(tie, "-> top (tie):", top_attendee(tie))
    print({}, "-> top:", top_attendee({}))
    try:
        mark_present(register, "   ")
    except ValueError as err:
        print("Rejected:", err)
