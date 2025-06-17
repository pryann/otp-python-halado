# Higher-Order Function with Closure Example
def outer_function(text):
    msg = text.upper()

    def inner_function():
        print(msg)

    return inner_function


outer_function_result = outer_function("hello")
outer_function_result()  # prints "HELLO"
outer_function_result()  # prints "HELLO"
# simple version
outer_function("curly")()


def make_incrementor(n):
    def incrementor(x):
        return x + n

    return incrementor


inc = make_incrementor(42)
print(inc(10))  # prints 52
print(inc(20))  # prints 62
print(inc(100))  # prints 142


def make_counter(count):
    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter(1234)
print(counter())  # prints 1235
print(counter())  # prints 1236

counter_2 = make_counter(1000)
print(counter_2())  # prints 1001
print(counter_2())  # prints 1002
