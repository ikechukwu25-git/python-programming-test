"""Challenge 05 - Payroll Deduction Calculator."""

PENSION_RATE = 0.05
HEALTH_RATE = 0.02


def net_salary(basic_salary, bonus=0):
    """Net pay = basic - 5% pension - 2% health (on basic only) + bonus."""
    if basic_salary < 0 or bonus < 0:
        raise ValueError("Salary and bonus cannot be negative.")
    deductions = basic_salary * (PENSION_RATE + HEALTH_RATE)
    return round(basic_salary - deductions + bonus, 2)


if __name__ == "__main__":
    assert net_salary(100_000, 10_000) == 103_000.0
    assert net_salary(100_000) == 93_000.0
    print("net_salary(100000, 10000) ->", net_salary(100_000, 10_000))
    print("net_salary(100000)        ->", net_salary(100_000))
    print("net_salary(250000, 15000) ->", net_salary(250_000, 15_000))
    print("net_salary(0)             ->", net_salary(0))
    try:
        net_salary(-5)
    except ValueError as err:
        print("Rejected:", err)
