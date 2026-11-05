"""Challenge 29 - Employee Salary System."""


class Employee:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Employee name is required.")
        self.name = name

    def calculate_pay(self):
        raise NotImplementedError("Subclasses must implement calculate_pay().")


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class Freelancer(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        if hourly_rate < 0 or hours < 0:
            raise ValueError("Rate and hours cannot be negative.")
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self):
        return self.hourly_rate * self.hours


if __name__ == "__main__":
    assert FullTimeEmployee("Ada", 150_000).calculate_pay() == 150_000
    assert Freelancer("Bola", 5_000, 12).calculate_pay() == 60_000

    staff = [FullTimeEmployee("Ada", 150_000), Freelancer("Bola", 5_000, 12),
             FullTimeEmployee("Chidi", 220_000), Freelancer("Dayo", 7_500, 0)]
    total = 0
    for person in staff:                      # polymorphism: same call, different behaviour
        pay = person.calculate_pay()
        total += pay
        print(f"{type(person).__name__:17} {person.name:6} -> NGN {pay}")
    print("Total payroll:", total)
