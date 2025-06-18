from time import sleep, perf_counter
from multiprocessing import Process


def process_fn():
    sleep(1)


if __name__ == "__main__":
    start = perf_counter()
    p1 = Process(target=process_fn)
    p2 = Process(target=process_fn)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = perf_counter()
    print(f"Process finished in {end - start:.5f} seconds")
