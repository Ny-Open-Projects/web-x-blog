import multiprocessing


def producer(q: multiprocessing.Queue) -> None:
    for i in range(5):
        q.put(f"item-{i}")
    q.put(None)


def consumer(q: multiprocessing.Queue) -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print(f"消费 {item}")


if __name__ == "__main__":
    q: multiprocessing.Queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=producer, args=(q,))
    c = multiprocessing.Process(target=consumer, args=(q,))
    p.start()
    c.start()
    p.join()
    c.join()
    print("IPC 完成")
