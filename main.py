from course import Course, InvalidMarksError, load_course


def test_student_class():
    """Task 1: Test the Student class and list printing."""
    print("=== Task 1: Student Test ===")

    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def passed(self):
            return self.marks >= 50

        def __str__(self):
            status = "Pass" if self.passed() else "Fail"
            return f"{self.name} ({self.marks}): {status}"

    students = [
        Student("Ali", 72),
        Student("Sara", 45),
        Student("Omar", 50),
    ]

    for s in students:
        print(s)
    print()


def test_course_methods():
    """Task 2 & 3: Test Course methods, len, average, top student, and custom exception."""
    print("=== Task 2 & 3: Course & Exception Test ===")
    
    course = Course("Programming for AI")
    course.add_student("Ali", 88)
    course.add_student("Sara", 92)
    course.add_student("Omar", 75)

    print(f"Total Students: {len(course)}")
    print(f"Course Average: {course.average()}")
    print(f"Top Student: {course.top_student()}")

    # Testing custom exception for invalid marks
    try:
        course.add_student("Bilal", 120)
    except InvalidMarksError as err:
        print("Caught Exception:", err)

    print("Course Summary:", course)
    print()


def test_file_loader():
    """Task 4: Test loading course data from a text file and handling errors."""
    print("=== Task 4: File Loader Test ===")

    # Loading valid file with some bad records inside
    loaded_course = load_course("Programming for AI", "marks.txt")
    print(loaded_course)
    print(f"Top Student from File: {loaded_course.top_student()}")
    print()

    # Testing non-existent file handling
    print("=== Wrong File Test ===")
    load_course("Programming for AI", "non_existent_file.txt")


if __name__ == "__main__":
    test_student_class()
    test_course_methods()
    test_file_loader()