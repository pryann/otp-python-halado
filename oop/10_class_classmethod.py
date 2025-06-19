class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def get_company(cls):
        return cls.company.upper()


employee = Employee("Alice", 50000)
employee_2 = Employee("John", 60000)
print(Employee.company)
print(employee.company)
print(employee_2.company)
print(Employee.employee_count)
print(Employee.get_company())
print(employee.get_company())
