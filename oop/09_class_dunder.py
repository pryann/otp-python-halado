class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Employee(name={self.name!r}, age={self.age})"

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Employee):
            return False
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return len(self.name) > 0 and self.age > 0


employee = Employee("Alice", 30)
employee_2 = Employee("Alice", 30)
print(employee)
print(repr(employee))
print(employee == employee_2)
print(bool(employee))
