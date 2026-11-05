"""Challenge 23 - Patient Appointment Details."""


class Appointment:
    def __init__(self, patient_name, date, time, therapist):
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.therapist = therapist

    def __str__(self):
        return (f"{self.patient_name} - {self.date} at {self.time} "
                f"with {self.therapist}")


if __name__ == "__main__":
    first = Appointment("Ife", "2026-11-06", "09:00", "Dr Eze")
    second = Appointment("Tunde", "2026-11-07", "14:30", "Dr Bello")
    for appt in (first, second):
        print(appt)
    assert first.patient_name != second.patient_name   # separate instance data
