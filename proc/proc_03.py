from time import sleep, perf_counter
from multiprocessing import Process


def process_fn():
    sleep(1)


def main():
    processes = []
    for _ in range(1600):
        p = Process(target=process_fn)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    start = perf_counter()
    main()
    end = perf_counter()
    print(f"Process finished in {end - start:.5f} seconds")
