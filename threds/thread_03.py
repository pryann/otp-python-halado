from time import sleep, perf_counter
from threading import Thread


def task(id):
    # print(f"Task {id} started...")
    sleep(1)
    # print(f"Task {id} completed.")


if __name__ == "__main__":
    start_time = perf_counter()
    threads = []

    for i in range(100000):
        thread = Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = perf_counter()
    print(f"Total time taken: {end_time - start_time:.5f} seconds")
