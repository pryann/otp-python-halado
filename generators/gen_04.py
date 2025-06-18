def squer_inputs():
    while True:
        num = yield
        yield num**2


squares = squer_inputs()
next(squares)  # Initialize the generator
print(squares.send(2))
next(squares)  # Initialize the generator
print(squares.send(20))
