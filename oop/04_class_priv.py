class Student:
    __slots__ = (
        "first_name",
        "last_name",
        "__neptun_code",
        "subjects",
    )

    def __init__(
        self,
        first_name,
        last_name,
        neptun_code,
        subjects,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects
        self.__neptun_code = neptun_code

    def calc_avarage(self):
        summa_grade = sum(subject["grade"] for subject in self.subjects)
        avarage_grade = summa_grade / len(self.subjects)
        return round(avarage_grade, 2)

        # return round(
        #     sum(subject["grade"] for subject in self.subjects) / len(self.subjects), 2
        # )

    def calc_credits(self):
        return sum(
            subject["credits"] for subject in self.subjects if subject["grade"] > 1
        )

    def log_stat(self):
        print(
            f"{self.first_name} {self.last_name} ({self.__neptun_code}) - "
            f"Average: {self.calc_avarage()}, Credits: {self.calc_credits()}"
        )


student = Student(
    "John",
    "Doe",
    "APC123",
    [
        {"name": "Math", "credits": 3, "grade": 4},
        {"name": "Physics", "credits": 4, "grade": 2},
        {"name": "Algorithms", "credits": 7, "grade": 1},
    ],
)

print(student.calc_avarage())
print(student.calc_credits())
# AttributeError
# print(student.__neptun_code)
student.log_stat()

print(
    student._Student__neptun_code
)  # Accessing the private attribute using name mangling
