from time import sleep
from multiprocessing import Pool
# from decorators import runtime_benchmark

results = []


def process_fn(sec):
    sleep(sec)
    return f"Process completed after {sec} seconds"


def success_callback(result):
    result_dict = {"status": "success", "results": result}
    results.append(result_dict)


# @runtime_benchmark
def main():
    proc_count = 5
    pool = Pool(processes=proc_count)
    args = [i + 1 for i in range(proc_count)]
    async_result = pool.map_async(process_fn, args, callback=success_callback)
    pool.close()
    async_result.wait()
    print(results)


if __name__ == "__main__":
    main()
