"""Challenge 06 - School Result Formatter."""


def grade(score):
    """Return A-F for a score between 0 and 100, or an error message."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        return "Error: score must be a number."
    if not 0 <= score <= 100:
        return "Error: score must be between 0 and 100."
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:
        return "C"
    if score >= 45:
        return "D"
    if score >= 40:
        return "E"
    return "F"


def report(name, subject, score):
    """Return 'Name | Subject | Score | Grade' or a clear error message."""
    result = grade(score)
    if result.startswith("Error"):
        return f"Cannot create report for {name} ({subject}): {result}"
    return f"{name} | {subject} | {score} | {result}"


if __name__ == "__main__":
    assert report("Ada", "Python", 74) == "Ada | Python | 74 | A"
    for n, s, sc in [("Ada", "Python", 74), ("Bola", "Maths", 65), ("Chidi", "English", 52),
                     ("Dayo", "Physics", 45), ("Efe", "Biology", 40), ("Femi", "Chemistry", 12),
                     ("Gina", "History", 101), ("Hauwa", "Art", "ninety")]:
        print(report(n, s, sc))
