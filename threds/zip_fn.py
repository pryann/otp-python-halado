a = [1, 2, 3]
b = ["a", "b", "c"]

print(list(zip(a, b)))

for x, y in zip(a, b):
    print(x, y)

pairs = [(1, "a"), (2, "b"), (3, "c")]
x, y = zip(*pairs)
print(x, y)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

for x,y,z in zip(a, b, c):
    print(x, y, z)