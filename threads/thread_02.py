from time import sleep, perf_counter
from threading import Thread


def task():
    print("Task started...")
    # simulate a long-running I/O task
    sleep(2)
    print("Task completed.")


# double underscore, short name for dunder
if __name__ == "__main__":
    start = perf_counter()
    # GIL - Global Interpreter Lock
    # The GIL allows only one thread to execute Python bytecode at a time.
    # This means that even if you have multiple threads, only one can run Python code at a time.
    # This is why Python threads are not ideal for CPU-bound tasks.
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = perf_counter()
    # out = "Total time taken: " + str(end - start) + " seconds"
    # out = "Total time taken: {0} seconds".format(end - start)
    # out = f"Total time taken: {end - start:.2f} seconds"
    # first_name = "John"
    # last_name = "Doe"
    # out = "User name: {0} {1}".format(first_name, last_name)
    # out = f"User name: {first_name} {last_name}"

    print(f"Total time taken: {end - start:.5f} seconds")
