def increase_price_by_tax(tax_rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * (1 + tax_rate / 100)

        return wrapper

    return decorator


def apply_discount(discount_rate):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * (1 - discount_rate / 100)

        return wrapper

    return decorator


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Return value:", result)
        return result

    return wrapper


@log_result
@increase_price_by_tax(5)
@apply_discount(10)
def summa(a, b):
    return a + b


summa(5, 10)
