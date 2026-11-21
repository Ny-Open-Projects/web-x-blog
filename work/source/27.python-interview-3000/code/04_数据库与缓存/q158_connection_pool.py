"""线程安全连接池: LifoQueue + 上下文管理器 + 健康检查"""
import queue
import threading
from contextlib import contextmanager


class Conn:
    def __init__(self, cid: int):
        self.cid = cid
        self.closed = False

    def ping(self) -> bool:
        return not self.closed        # 真实场景换成 conn.ping()

    def execute(self, sql: str) -> str:
        return f"conn#{self.cid}: {sql}"


class Pool:
    def __init__(self, factory, size: int = 3):
        self._factory = factory
        self._idle: queue.LifoQueue = queue.LifoQueue(maxsize=size)
        self._lock = threading.Lock()
        self._total = 0
        self._size = size

    def _create(self):
        with self._lock:
            if self._total < self._size:
                self._total += 1
                return self._factory(self._total)
        raise RuntimeError("池已满且无空闲连接")

    @contextmanager
    def borrow(self, timeout: float = 2.0):
        try:
            conn = self._idle.get(timeout=timeout)
        except queue.Empty:
            conn = self._create()     # 池空且未达上限则新建
        if not conn.ping():           # 归还前的连接可能已失效
            conn = self._factory(conn.cid)
        try:
            yield conn
        finally:
            self._idle.put(conn)


if __name__ == "__main__":
    pool = Pool(lambda i: Conn(i), size=2)

    def worker(tid: int):
        with pool.borrow() as conn:
            print(f"线程{tid} ->", conn.execute("SELECT 1"))

    ts = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()
