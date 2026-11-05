"""Challenge 16 - Customer Phone Number Cleaner."""
import re


def normalize_phone(raw):
    """Return an 11-digit local Nigerian number, or raise ValueError."""
    if not isinstance(raw, str):
        raise ValueError("Phone number must be text.")
    cleaned = raw.replace(" ", "").replace("-", "")
    if not re.fullmatch(r"\+?[0-9]+", cleaned):          # digits + optional leading +
        raise ValueError(f"Invalid characters in {raw!r}.")
    if cleaned.startswith("+"):
        if not re.fullmatch(r"\+234[0-9]{10}", cleaned):
            raise ValueError(f"Invalid +234 number: {raw!r}.")
        cleaned = "0" + cleaned[4:]
    if not re.fullmatch(r"0[0-9]{10}", cleaned):
        raise ValueError(f"Number must be 11 digits starting with 0: {raw!r}.")
    return cleaned


if __name__ == "__main__":
    assert normalize_phone("+234 803-123-4567") == "08031234567"
    tests = ["+234 803-123-4567", "0803 123 4567", "080-3123-4567", "08031234567",
             "0803123456", "+2348031234", "+234 (803) 123", "234 803 123 4567", "0803abc4567", ""]
    for t in tests:
        try:
            print(f"{t!r:24} -> {normalize_phone(t)!r}")
        except ValueError as err:
            print(f"{t!r:24} -> Rejected: {err}")
