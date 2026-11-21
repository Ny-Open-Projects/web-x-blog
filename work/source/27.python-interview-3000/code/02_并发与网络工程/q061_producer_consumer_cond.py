import threading
import time

buffer: list[int] = []
MAX_SIZE = 3
cond = threading.Condition()


def producer(pid: int, count: int) -> None:
    for i in range(count):
        with cond:
            while len(buffer) >= MAX_SIZE:
                cond.wait()  # 缓冲区满, 等消费者
            item = pid * 100 + i
            buffer.append(item)
            print(f"生产者 {pid} 放入 {item}, 缓冲区 {buffer}")
            cond.notify_all()
        time.sleep(0.05)


def consumer(cid: int, total: int) -> None:
    consumed = 0
    while consumed < total:
        with cond:
            while not buffer:
                cond.wait()  # 缓冲区空, 等生产者
            item = buffer.pop(0)
            consumed += 1
            print(f"消费者 {cid} 取出 {item}, 缓冲区 {buffer}")
            cond.notify_all()


if __name__ == "__main__":
    ps = [threading.Thread(target=producer, args=(p, 3)) for p in range(2)]
    cs = [threading.Thread(target=consumer, args=(c, 3)) for c in range(2)]
    for t in ps + cs:
        t.start()
    for t in ps + cs:
        t.join()
    print("完成, 缓冲区剩余:", buffer)
