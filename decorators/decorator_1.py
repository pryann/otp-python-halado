def basic_decorator(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")

    return wrapper


def say_hello():
    print("Hello!")


# result = basic_decorator(say_hello)
# result()  # prints "Start wrapper", "Hello!", "End wrapper"
basic_decorator(say_hello)()  # prints "Start wrapper", "Hello!", "End wrapper"
