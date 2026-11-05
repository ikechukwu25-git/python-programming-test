"""Challenge 27 - Student Course Enrollment."""


class Course:
    def __init__(self, title, capacity=3):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.title = title
        self.capacity = capacity
        self._students = []

    def _find(self, name):
        for student in self._students:
            if student.lower() == name.lower():
                return student
        return None

    def enroll(self, name):
        name = name.strip()
        if not name:
            return "invalid name"
        if self._find(name):
            return "already enrolled"
        if len(self._students) >= self.capacity:
            return "course full"
        self._students.append(name)
        return "enrolled"

    def remove(self, name):
        found = self._find(name.strip())
        if not found:
            return "not enrolled"
        self._students.remove(found)
        return "removed"

    def roster(self):
        return list(self._students)      # a copy - the internal list stays private


if __name__ == "__main__":
    course = Course("Python 101")
    assert course.enroll("Ada") == "enrolled"
    assert course.enroll("Ada") == "already enrolled"
    for student in ("Bola", "Chidi", "Dayo"):
        print(f"enroll({student!r}) ->", course.enroll(student))
    print("Roster:", course.roster())

    course.roster().append("Hacker")                 # modifies only the copy
    assert "Hacker" not in course.roster()

    print("remove('Bola') ->", course.remove("Bola"))
    print("remove('Zed')  ->", course.remove("Zed"))
    print("enroll('Dayo') ->", course.enroll("Dayo"))
    print("Roster:", course.roster())
