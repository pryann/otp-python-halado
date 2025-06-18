from threading import Thread
from time import sleep, time, ctime


def log_service(thread_name, delay):
    while True:
        sleep(delay)
        print(f"{thread_name}: {ctime(time())}")


if __name__ == "__main__":
    Thread(target=log_service, args=("LogService1", 1), daemon=True).start()
    Thread(target=log_service, args=("LogService2", 1.5), daemon=True).start()
    print("Do other stuff")
    sleep(5)
    print("Main thread finished")
