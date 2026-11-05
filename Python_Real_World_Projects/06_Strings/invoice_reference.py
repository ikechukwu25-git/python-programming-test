"""Challenge 18 - Invoice Reference Generator."""
from datetime import datetime


def invoice_ref(full_name, date, number):
    """Build INITIALS-YYYYMMDD-NNNN."""
    if not isinstance(full_name, str) or not full_name.split():
        raise ValueError("Name must contain at least one non-empty word.")
    if not isinstance(date, str):
        raise ValueError("Date must be a YYYYMMDD string.")
    try:
        datetime.strptime(date, "%Y%m%d")
    except ValueError:
        raise ValueError(f"Invalid date {date!r}; expected a real YYYYMMDD date.") from None
    if len(date) != 8:
        raise ValueError("Date must be exactly 8 digits (YYYYMMDD).")
    if isinstance(number, bool) or not isinstance(number, int) or not 0 <= number <= 9999:
        raise ValueError("Invoice number must be an integer from 0 to 9999.")
    initials = "".join(word[0] for word in full_name.split()).upper()
    return f"{initials}-{date}-{number:04d}"


if __name__ == "__main__":
    assert invoice_ref("Ada Obi", "20261104", 27) == "AO-20261104-0027"
    print(invoice_ref("Ada Obi", "20261104", 27))
    print(invoice_ref("  chinedu   okafor  eze ", "20260105", 9999))
    print(invoice_ref("bola", "20251231", 0))
    for args in [("   ", "20261104", 1), ("Ada Obi", "2026-11-04", 1),
                 ("Ada Obi", "20261104", 10000), ("Ada Obi", "20261340", 5)]:
        try:
            invoice_ref(*args)
        except ValueError as err:
            print(f"{args} -> Rejected: {err}")
