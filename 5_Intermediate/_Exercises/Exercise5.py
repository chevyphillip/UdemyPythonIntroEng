# type: ignore
"""Exercise 5:
1.)
Write a class Student that has the following member variables:
- Name (String)
- Lastname (String)
- Age (Integer)
- Id (Integer)
2.)
Write a method that prints the information about the student.
E.g. Student('Jan', 'Schaffranek', 29, 1080133228459) will print:
'Jan Schaffranek is 29 years old and has the id 1080133228459'
"""


class Student:
    def __init__(self):
        pass

    def print_student(self):
        pass


def main() -> None:
    oskar = Student("Oskar", "Oskarson", 29, 1080132254623)
    oskar.print_student()
    jan = Student("Jan", "Schaffranek", 28, 1080133228459)
    jan.print_student()


if __name__ == "__main__":
    main()
