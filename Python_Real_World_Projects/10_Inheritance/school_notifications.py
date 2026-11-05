"""Challenge 30 - School Notification System."""


class Notification:
    def __init__(self, recipient, message):
        if not recipient.strip() or not message.strip():
            raise ValueError("Recipient and message are required.")
        self.recipient = recipient
        self.message = message

    def send(self):
        return f"Notice to {self.recipient}: {self.message}"


class EmailNotification(Notification):
    def __init__(self, recipient, message, subject="School Notice"):
        super().__init__(recipient, message)
        if "@" not in recipient:
            raise ValueError("Email recipient must contain '@'.")
        self.subject = subject

    def send(self):
        return f"Email to {self.recipient} | Subject: {self.subject} | {self.message}"


class SMSNotification(Notification):
    MAX_LENGTH = 160

    def __init__(self, recipient, message):
        super().__init__(recipient, message)
        if len(message) > self.MAX_LENGTH:
            raise ValueError(f"SMS cannot exceed {self.MAX_LENGTH} characters.")

    def send(self):
        return f"SMS to {self.recipient}: {self.message}"


if __name__ == "__main__":
    assert SMSNotification("08031234567", "Exam tomorrow").send() == "SMS to 08031234567: Exam tomorrow"
    notices = [SMSNotification("08031234567", "Exam tomorrow"),
               EmailNotification("parent@example.com", "PTA meeting on Friday", "PTA Meeting"),
               EmailNotification("teacher@school.edu.ng", "Submit grades by Monday"),
               Notification("Principal", "Assembly at 8am")]
    for notice in notices:
        print(notice.send())
    for bad in (lambda: SMSNotification("0803", "x" * 200), lambda: EmailNotification("no-at-sign", "Hi")):
        try:
            bad()
        except ValueError as err:
            print("Rejected:", err)
