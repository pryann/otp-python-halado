a = 1000
b = a
print(id(a))  # should be the same
print(id(b))  # should be the same

b = 10
print(id(a))
print(id(b))

names = ["John", "Jane", "Bobby"]
names_copy = names
print(id(names))
print(id(names_copy))

names.append("Alice")
print(names)
print(names_copy)

names_copy.append("Bob")
print(names)
print(names_copy)

print(id(names))  # should be the same
print(id(names_copy))  # should be the same

names_copy = ["Jonny", "Jack"]
print(names)
print(names_copy)

salaries = [1000, 2000, 3000]


def modify_list(lst):
    lst.append(4000)
    print("Inside function:", lst)


modify_list(salaries)
print("Outside function:", salaries)

names = ["John", "Jane", "Bobby"]
names_shallow_copy = names.copy()  # Create a shallow copy
# names_shallow_copy = names[:] 
print(id(names))  # Print the memory address of names
print(id(names_shallow_copy))  # Print the memory address of names_real_copy
