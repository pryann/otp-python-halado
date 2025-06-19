import os

# List comprehension:
os.system('python -m timeit --number=10000 "a = [i for i in range(1000)]"')

# # Tuple from list comprehension:
os.system('python -m timeit --number=10000 "a = tuple([i for i in range(1000)])"')


#  Generator only:
os.system('python -m timeit --number=10000 "a = (i for i in range(1000))"')

# # Tuple from generator:
os.system('python -m timeit --number=10000 "a = tuple(i for i in range(1000))"')

# # List from generator:
os.system('python -m timeit --number=10000 "a = list(i for i in range(1000))"')

# # Tuple from unpacking:
os.system('python -m timeit --number=10000 "a = *(i for i in range(1000)),"')
