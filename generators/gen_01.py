def num_generator():
    yield 1
    yield 2
    yield 3


nums = num_generator()
print(next(nums))  # Output: 1
print(next(nums))  # Output: 2
print(next(nums))  # Output: 3
# StopIteration will be raised if we call next() again
# print(next(nums))  

