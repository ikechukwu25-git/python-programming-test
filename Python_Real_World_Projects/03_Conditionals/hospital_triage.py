"""Challenge 08 - Hospital Triage Queue."""


def triage(age, temperature, emergency):
    """Return (priority, explanation). Emergency always wins."""
    if age < 0 or not 25 <= temperature <= 45:
        raise ValueError("Age or temperature is outside a realistic range.")
    if emergency:
        return 1, "Emergency symptoms present."
    elif age >= 65 and temperature >= 39.0:
        return 2, "Age 65+ and high fever (>= 39.0 C)."
    elif age >= 65:
        return 2, "Age is 65 or older."
    elif temperature >= 39.0:
        return 2, "High fever (>= 39.0 C)."
    else:
        return 3, "No urgent criteria met."


def ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


if __name__ == "__main__":
    assert triage(70, 37.0, False)[0] == 2
    assert triage(30, 36.5, True)[0] == 1
    assert triage(30, 36.5, False)[0] == 3
    for case in [(70, 37.0, False), (30, 39.5, False), (80, 40.0, True), (25, 36.6, False)]:
        p, why = triage(*case)
        print(f"age={case[0]}, temp={case[1]}, emergency={case[2]} -> Priority {p} ({why})")

    print("\n--- Live triage ---")
    age_raw = ask("Age: ")
    if age_raw is not None:
        try:
            age = int(age_raw)
            temp = float(ask("Temperature (C): "))
            emergency = ask("Emergency symptoms? (yes/no): ").strip().lower() in ("y", "yes")
            p, why = triage(age, temp, emergency)
            print(f"Priority {p}: {why}")
        except (ValueError, TypeError, AttributeError) as err:
            print("Invalid input:", err)
