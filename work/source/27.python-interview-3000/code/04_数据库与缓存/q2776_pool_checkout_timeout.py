"""连接池的借还超时: checkout 限时, 借出前验活, 死连接丢弃"""
import queue
import sqlite3
import threading
from contextlib import contextmanager

class BrokenConn:
    def execute(self, *args):
        raise RuntimeError("连接已断")

class Pool:
    def __init__(self, size, checkout_timeout=0.3):
        self._free = queue.LifoQueue()
        self.timeout = checkout_timeout
        self.timed_out = 0
        self.discarded = 0
        for _ in range(size):
            conn = sqlite3.connect(":memory:")
            conn.execute("CREATE TABLE IF NOT EXISTS t (x)")
            self._free.put(conn)

    @contextmanager
    def borrow(self):
        conn = self._checkout()
        try:
            yield conn
        finally:
            self._free.put(conn)

    def _checkout(self):
        while True:
            try:
                conn = self._free.get(timeout=self.timeout)
            except queue.Empty:
                self.timed_out += 1
                raise TimeoutError("checkout 超时: 池已借空且等待超时")
            try:
                conn.execute("SELECT 1").fetchone()     # 借出前验活
                return conn
            except Exception:
                self.discarded += 1                     # 死连接丢弃, 换下一个
                if self._free.empty():
                    self.timed_out += 1
                    raise TimeoutError("池内连接全部失效")

# 1) 池里混进死连接: 验活当场发现并丢弃
pool = Pool(3)
pool._free.put(BrokenConn())
with pool.borrow() as conn:
    conn.execute("SELECT 1").fetchone()
print("验活: 死连接被丢弃 %d 个, 业务拿到的是好连接" % pool.discarded)

# 2) 借空超时: 2 连接池, 3 个借者各持有 0.4s, checkout 限时 0.3s
pool2 = Pool(2, checkout_timeout=0.3)
results = []
barrier = threading.Barrier(3)

def worker(i):
    barrier.wait()
    try:
        with pool2.borrow() as conn:
            conn.execute("SELECT 1").fetchone()
            threading.Event().wait(0.4)
        results.append("ok%d" % i)
    except TimeoutError:
        results.append("timeout%d" % i)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("借还结果:", sorted(results), "| 超时计数 %d (快速失败而不是无限等)" % pool2.timed_out)
