class Student:
    __slots__ = ("first_name", "last_name", "subjects")

    def __init__(self, first_name, last_name, subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects

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


student = Student(
    "John",
    "Doe",
    [
        {"name": "Math", "credits": 3, "grade": 4},
        {"name": "Physics", "credits": 4, "grade": 2},
        {"name": "Algorithms", "credits": 7, "grade": 1},
    ],
)

print(student.calc_avarage())
print(student.calc_credits())
