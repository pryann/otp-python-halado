from time import sleep, perf_counter


def process_fn():
    sleep(1)


if __name__ == "__main__":
    start = perf_counter()
    process_fn()
    process_fn()
    process_fn()
    end = perf_counter()
    print(f"Process finished in {end - start:.5f} seconds")
