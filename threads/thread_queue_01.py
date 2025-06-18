from time import sleep, perf_counter
from threading import Thread
from queue import Queue


def task(id, result_queue):
    sleep(1)
    result_queue.put(f"Task {id} completed.")


if __name__ == "__main__":
    threads = []
    result_queue = Queue()

    for i in range(10):
        thread = Thread(target=task, args=(i, result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while not result_queue.empty():
        print(result_queue.get())
