def num_generator():
    yield 1
    yield 2
    yield 3


nums = num_generator()
print(*nums)

# nums = num_generator()
# print(list(nums))  # Output: [1, 2, 3]
