from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Person:
    sort_index: int = field(init=False, repr=False, compare=False)
    first_name: str
    last_name: str
    age: int
    school: str = "Berklee"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if len(self.first_name) < 2:
            raise ValueError("First name must be at least 2 characters long")
        if len(self.last_name) < 2:
            raise ValueError("First name must be at least 2 characters long")

        object.__setattr__(self, "sort_index", self.age)


p1 = Person("John", "Doe", 20)
p2 = Person("Jane", "Doe", 18)
print(p1)
print(p2)

p3 = Person("Alice", "Smith", 10)
# p3.job = "Engineer"
# print(p3.job)
# print(p3)
people = [p1, p2, p3]
print(people)
people.sort()
print(people)
