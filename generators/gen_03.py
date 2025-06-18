def num_generator(n):
    id = n + 1
    while True:
        yield id
        id += 1


nums = num_generator(100)
print(next(nums))
print(next(nums))

ids = num_generator(0)
for _ in range(100):
    id = next(ids)
    if id > 100:
        break
    print(id)

for _ in range(100):
    id = next(ids)
    if id > 200:
        break
    print(id)
