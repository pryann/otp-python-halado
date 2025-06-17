def basic_decorator(func):
    def wrapper(name):
        print("Start wrapper")
        func(name)
        print("End wrapper")

    return wrapper


@basic_decorator
def say_hello(name):
    print(f"Hello! {name}")


say_hello("Gergő")  # prints "Start wrapper", "Hello!", "End wrapper"
