def summarize(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference of two integers."""
    return a - b


def divide(a: int, b: int) -> float:
    """Returns the division of two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
