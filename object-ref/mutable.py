names = ["John", "Jane", "Bobby"]
print(id(names))  # Print the memory address of names

names.append("Alice")  # Modify the list by appending a new name
print(id(names))  # Print the memory address of names again, should be the same

names = ["Jonny", "Jack"]
print(id(names))  # Print the memory address of name, should be different
