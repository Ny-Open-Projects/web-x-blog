import queue
import threading
import time
from typing import Optional

q: "queue.Queue[Optional[int]]" = queue.Queue(maxsize=5)


def producer(pid: int, count: int) -> None:
    for i in range(count):
        item = pid * 100 + i
        q.put(item)  # 队列满时阻塞, 形成背压
        print(f"生产者 {pid} 生产 {item}")
    q.put(None)  # 哨兵


def consumer(cid: int) -> None:
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"消费者 {cid} 消费 {item}")
        time.sleep(0.05)
        q.task_done()


if __name__ == "__main__":
    producers = [threading.Thread(target=producer, args=(p, 3)) for p in range(2)]
    consumers = [threading.Thread(target=consumer, args=(c,)) for c in range(2)]
    for t in producers + consumers:
        t.start()
    for t in producers:
        t.join()
    q.join()
    print("所有任务处理完成")
