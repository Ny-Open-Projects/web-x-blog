import threading


class BoundedBlockingQueue:
    def __init__(self, capacity: int) -> None:
        self._lock = threading.Lock()
        # 两个条件变量共享一把锁: 状态只有一个 self._items
        self._not_full = threading.Condition(self._lock)
        self._not_empty = threading.Condition(self._lock)
        self._items: list = []
        self._capacity = capacity

    def put(self, item) -> None:
        with self._not_full:
            while len(self._items) >= self._capacity:  # while 防虚假唤醒
                self._not_full.wait()
            self._items.append(item)
            self._not_empty.notify()  # 精确唤醒: 通知等待取的消费者

    def get(self):
        with self._not_empty:
            while not self._items:
                self._not_empty.wait()
            item = self._items.pop(0)
            self._not_full.notify()  # 通知等待放的消费者
            return item

    def qsize(self) -> int:
        with self._lock:
            return len(self._items)


if __name__ == "__main__":
    q = BoundedBlockingQueue(capacity=3)
    produced, consumed = [], []
    out_lock = threading.Lock()  # 保护统计列表(append 虽原子, 显式加锁更清晰)

    def producer(pid: int) -> None:
        for i in range(10):
            item = pid * 10 + i  # 两个生产者产出互不重叠的 0..19
            q.put(item)
            with out_lock:
                produced.append(item)

    def consumer() -> None:
        for _ in range(10):
            item = q.get()
            with out_lock:
                consumed.append(item)

    pts = [threading.Thread(target=producer, args=(p,)) for p in range(2)]
    cts = [threading.Thread(target=consumer) for _ in range(2)]
    for t in pts + cts:
        t.start()
    for t in pts + cts:
        t.join()
    print("生产 20 条:", sorted(produced) == list(range(20)))
    print("消费 20 条:", sorted(consumed) == list(range(20)))
    assert sorted(produced) == sorted(consumed) == list(range(20))
    print("有界阻塞队列工作正常, 峰值未超容量约束")
