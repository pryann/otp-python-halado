def basic_decorator(func):
    def wrapper(a, b):
        result = func(a, b)
        print("Return value:", result)
        return result

    return wrapper


@basic_decorator
def summa(a, b):
    return a + b


summa(5, 10)
