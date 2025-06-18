from time import sleep
from multiprocessing import Process
from decorators import runtime_benchmark


def process_fn():
    sleep(1)


@runtime_benchmark
def main():
    processes = [Process(target=process_fn) for _ in range(16)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
