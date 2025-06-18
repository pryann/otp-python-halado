from time import perf_counter


def runtime_benchmark(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Function '{fn.__name__}' took {finish - start: 0.5f} sec.")
        return result

    return wrapper
