import threading
import time

items: list[int] = []
cond = threading.Condition()


def consumer() -> None:
    with cond:
        while not items:
            print("consumer 无数据, 等待")
            cond.wait()
        print("consumer 取到", items.pop())


def producer() -> None:
    time.sleep(0.3)
    with cond:
        items.append(42)
        print("producer 放入 42")
        cond.notify()


if __name__ == "__main__":
    c = threading.Thread(target=consumer)
    p = threading.Thread(target=producer)
    c.start()
    p.start()
    c.join()
    p.join()
