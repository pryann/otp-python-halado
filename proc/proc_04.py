from time import sleep
from multiprocessing import Pool
from decorators import runtime_benchmark


def process_fn(sec):
    sleep(sec)
    return f"Process completed after {sec} seconds"


@runtime_benchmark
def main():
    proc_count = 5
    pool = Pool(processes=proc_count)
    args = [i + 1 for i in range(proc_count)]
    result = pool.map(process_fn, args)
    pool.close()
    print("Processes completed:", result)


if __name__ == "__main__":
    main()
