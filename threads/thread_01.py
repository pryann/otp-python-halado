from time import sleep, perf_counter
from threading import current_thread

thread = current_thread()
print(f"Thread {thread.name} is starting...")


def task():
    print("Task started...")
    # simulate a long-running I/O task
    sleep(2)
    print("Task completed.")


# double underscore, short name for dunder
if __name__ == "__main__":
    start = perf_counter()
    task()
    task()
    end = perf_counter()
    # out = "Total time taken: " + str(end - start) + " seconds"
    # out = "Total time taken: {0} seconds".format(end - start)
    # out = f"Total time taken: {end - start:.2f} seconds"
    # first_name = "John"
    # last_name = "Doe"
    # out = "User name: {0} {1}".format(first_name, last_name)
    # out = f"User name: {first_name} {last_name}"

    print(f"Total time taken: {end - start:.5f} seconds")
