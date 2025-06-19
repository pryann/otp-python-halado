# class Employee:
#     __slots__ = ("name", "__salary")

#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self):
#         return round(self.__salary, 2)

#     def set_salary(self, salary):
#         if salary > 0 and salary < 2_000_000_000:
#             self.__salary = salary


# employee = Employee("Alice", 50000)
# employee.set_salary(60000)
# print(employee.get_salary())


class Employee:
    __slots__ = ("name", "__salary")

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return round(self.__salary, 2)

    @salary.setter
    def salary(self, salary):
        if salary > 0 and salary < 2_000_000_000:
            self.__salary = salary

    @salary.deleter
    def salary(self):
        print("Deleting salary")
        self.__salary = 0


employee = Employee("Alice", 50000)
print(employee.salary)
employee.salary = 60000
print(employee.salary)
del employee.salary
print(employee.salary)
