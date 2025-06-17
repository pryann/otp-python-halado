import math


def increase_salary(salary, percent=10):
    """Increase the salary by a given percentage."""
    return salary * (1 + percent / 100)


# sorrendi argumentumok
print(increase_salary(1000, 10))
# nevesített argumentumok
print(increase_salary(percent=10, salary=1000))
# alapértelmezett érték használata
print(increase_salary(1000))


# sorrendi paraméterlista tuple-ben
def log_args(*args):
    print(args, type(args))


log_args(1, 2, 3, "hello", [1, 2, 3], (1, 2), {"key": "value"})


def log_kwargs(**kwargs):
    print(kwargs, type(kwargs))


log_kwargs(salary=1000, percent=10, name="John", age=30)


def log_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


log_args_kwargs(1, 2, 3, name="Alice", age=25, city="New York")


def generate_sqaure_matrix(*args):
    # matrix = []
    # size = math.floor(math.sqrt(len(args)))
    # for i in range(size):
    #     row = []
    #     for j in range(size):
    #         index = i * size + j
    #         if index < len(args):
    #             row.append(args[index])
    #         else:
    #             row.append(None)
    #     matrix.append(row)
    # return matrix

    # matrix = []
    # size = math.floor(math.sqrt(len(args)))
    # for i in range(0, len(args), size):
    #     matrix.append(list(args[i : size + i]))
    # return matrix

    size = math.floor(math.sqrt(len(args)))
    return [list(args[i : i + size]) for i in range(0, len(args), size)]


print(generate_sqaure_matrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
