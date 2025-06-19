from typing import Any, Optional


def summa(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


print(summa(10, 1))


def summa_list(numbers: list[int]) -> int:
    """Returns the sum of a list of integers."""
    return sum(numbers)


print(summa_list([1, 2, 3, 4, 5]))


def first_item(items: list[Any]) -> Optional[Any]:
    """Returns the first item of a list, or None if the list is empty."""
    if len(items) > 0:
        return items[0]
    return None
