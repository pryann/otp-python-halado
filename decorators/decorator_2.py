def basic_decorator(func):
    def wrapper():
        print("Start wrapper")
        func()
        print("End wrapper")

    return wrapper


@basic_decorator
def say_hello():
    print("Hello!")


say_hello()  # prints "Start wrapper", "Hello!", "End wrapper"
