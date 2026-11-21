"""deque 的线程安全边界:单端操作原子,组合操作与迭代不保。"""
import threading
from collections import deque

if __name__ == "__main__":
    q = deque()

    def producer():
        for i in range(1000):
            q.append(i)

    threads = [threading.Thread(target=producer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("4 线程并发 append 无丢失:", len(q) == 4000)

    task_q = deque(range(600))

    def worker():
        while True:
            try:
                task_q.popleft()
            except IndexError:
                return

    workers = [threading.Thread(target=worker) for _ in range(3)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    print("并发消费后清空:", len(task_q) == 0)

    d = deque(range(3))
    try:
        for v in d:
            d.append(v)
    except RuntimeError as exc:
        print("迭代中被修改:", exc)
