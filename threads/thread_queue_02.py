from time import sleep
from threading import Thread
from queue import Queue


def producer(q):
    for i in range(5):
        sleep(1)
        value = f"Produced {i}"
        print(value)
        q.put(value)
    q.put(None)


def consumer(q):
    while True:
        value = q.get()
        if value is None:
            break
        print(f"Consumed: '{value}'")


if __name__ == "__main__":
    q = Queue()
    Thread(target=producer, args=(q,), daemon=True).start()
    Thread(target=consumer, args=(q,), daemon=True).start()
    sleep(10)
    print("Main thread finished")
