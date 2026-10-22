
class InvalidMarksError(Exception):
    pass


class Course:
    """A course that stores students and their marks."""

    def remove_student(self, name: str) -> None:
        """Remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]

        
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        self.marks[student] = marks

    def average(self):
        if len(self.marks) == 0:
            return 0.0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        return len(self.marks)

    def __str__(self):
        count = len(self)
        word = "student" if count == 1 else "students"

        return (
            f"{self.name}: {count} {word}, "
            f"average {self.average():.1f}"
        )


def load_course(name, filename):
    course = Course(name)

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    student, marks = line.split(",")
                    course.add_student(student, int(marks))

                except ValueError:
                    student = line.split(",")[0]
                    print(f"Skipping {student}: marks is not a number")

                except InvalidMarksError as e:
                    print("Skipping:", e)

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


if __name__ == "__main__":
    c = Course("Test")
    c.add_student("Ali", 50)
    print(c)