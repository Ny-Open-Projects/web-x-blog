import threading
import time


class RWLock:
    """写者优先的读写锁:写者到达后阻止新读者进入,避免写饥饿。"""

    def __init__(self) -> None:
        self._cond = threading.Condition()
        self._readers = 0
        self._writer = False
        self._waiting_writers = 0

    def acquire_read(self) -> None:
        with self._cond:
            while self._writer or self._waiting_writers > 0:
                self._cond.wait()
            self._readers += 1

    def release_read(self) -> None:
        with self._cond:
            self._readers -= 1
            if self._readers == 0:
                self._cond.notify_all()

    def acquire_write(self) -> None:
        with self._cond:
            self._waiting_writers += 1
            while self._writer or self._readers > 0:
                self._cond.wait()
            self._waiting_writers -= 1
            self._writer = True

    def release_write(self) -> None:
        with self._cond:
            self._writer = False
            self._cond.notify_all()


data = {"value": 0}
rw = RWLock()


def reader(idx: int) -> None:
    for _ in range(100):
        rw.acquire_read()
        _ = data["value"]  # 只读, 多个读者可同时进入
        time.sleep(0.0005)
        rw.release_read()


def writer() -> None:
    for _ in range(50):
        rw.acquire_write()
        v = data["value"]
        time.sleep(0.0005)  # 若实现错误, 读者会在此期间并发读写
        data["value"] = v + 1
        rw.release_write()


if __name__ == "__main__":
    threads = [threading.Thread(target=writer) for _ in range(2)]
    threads += [threading.Thread(target=reader, args=(i,)) for i in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("最终值:", data["value"], "期望: 100")
    assert data["value"] == 100, "读写互斥被破坏"
    print("读写锁工作正常")
