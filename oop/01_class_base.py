list = [1, 2, 3]
print(type(list))


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


student = Student("John", "Doe")
print(student)
print(type(student))
print(student.first_name)
print(student.last_name)

print(getattr(student, "first_name"))