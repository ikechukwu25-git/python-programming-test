"""Challenge 17 - Complaint Keyword Detector."""
import re

ESCALATION_TERMS = ("refund", "broken", "fraud")
_PATTERN = re.compile(r"\b(?:" + "|".join(ESCALATION_TERMS) + r")\b", re.IGNORECASE)


def contains_escalation(text):
    """True if any escalation term appears as a whole word (case-insensitive)."""
    if not isinstance(text, str):
        raise TypeError("Complaint text must be a string.")
    return _PATTERN.search(text) is not None


if __name__ == "__main__":
    assert contains_escalation("My item is BROKEN") is True
    assert contains_escalation("unbroken seal") is False
    for text in ["My item is BROKEN", "unbroken seal", "I want a refund!", "This is fraud.",
                 "Refunded already", "Nothing wrong here", "fraud-alert, please help", ""]:
        print(f"{text!r:32} -> {contains_escalation(text)}")
