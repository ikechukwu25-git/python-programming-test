"""Challenge 21 - Election Poll Summary."""


def tally_votes(votes):
    """Frequency dictionary using normalised names (strip + lower)."""
    counts = {}
    for vote in votes:
        name = " ".join(vote.split()).lower()
        if name:                                  # ignore blank ballots
            counts[name] = counts.get(name, 0) + 1
    return counts


def find_winners(counts):
    """Return a list of winners (more than one means a tie; empty if no votes)."""
    if not counts:
        return []
    top = max(counts.values())
    return sorted(name for name, n in counts.items() if n == top)


def summarize(votes):
    counts = tally_votes(votes)
    print("Counts:", counts)
    for name, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {name}: {n}")
    winners = find_winners(counts)
    if not winners:
        print("No valid votes cast.")
    elif len(winners) == 1:
        print("Winner:", winners[0])
    else:
        print("Tie between:", ", ".join(winners))
    return counts, winners


if __name__ == "__main__":
    counts, winners = summarize(["Ada", "bola", "ADA", "Bola", "Ada"])
    assert counts == {"ada": 3, "bola": 2} and winners == ["ada"]
    print()
    summarize(["Ada", " bola ", "BOLA", "ada"])        # tie
    print()
    summarize(["  ", ""])                               # no valid votes
