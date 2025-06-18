from concurrent.futures import ThreadPoolExecutor
from time import sleep, time, ctime


def log_service(thread_name, delay):
    while logging:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    max_tasks = 5
    logging = True

    with ThreadPoolExecutor(max_workers=5) as executor:
        # Create a generator for thread names and delays
        # ("Thread-name-1", 1)
        # ("Thread-name-2", 2)
        # ("Thread-name-3", 3)
        # ("Thread-name-4", 4)
        # ("Thread-name-5", 5)
        args = ((f"Thread-name-{i + 1}", i + 1) for i in range(max_tasks))
        # zip(
        #     ("Thread-name-1", 1),
        #     ("Thread-name-2", 2),
        #     ("Thread-name-3", 3),
        #     ("Thread-name-4", 4),
        #     ("Thread-name-5", 5),
        # )
        # = 
        # ("Thread-name-1", "Thread-name-2", "Thread-name-3", "Thread-name-4", "Thread-name-5")
        # (1, 2, 3, 4, 5)
        executor.map(log_service, *zip(*args))
        sleep(5)
        logging = False
