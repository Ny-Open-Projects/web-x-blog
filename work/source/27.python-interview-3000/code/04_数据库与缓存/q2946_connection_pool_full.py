"""连接池完整实现: 上限控制 借还验活 等待超时 坏连接置换"""
import contextlib
import itertools
import queue
import threading
import time


class FakeConn:
    _ids = itertools.count(1)

    def __init__(self):
        self.id = next(FakeConn._ids)
        self.healthy = True
        self.closed = False

    def ping(self):
        if self.closed or not self.healthy:
            raise RuntimeError("connection broken")

    def close(self):
        self.closed = True


class Pool:
    def __init__(self, max_size=3):
        self.max_size = max_size
        self._free = queue.LifoQueue()
        self._all = []
        self._mu = threading.Lock()
        self.created = 0

    def _acquire(self, timeout=1.0):
        deadline = time.monotonic() + timeout
        while True:
            with self._mu:
                if len(self._all) < self.max_size:   # 上限内先造新连接
                    c = FakeConn()
                    self._all.append(c)
                    self.created += 1
                    return c
            wait = deadline - time.monotonic()
            if wait <= 0:
                raise TimeoutError("pool exhausted, max_size=%d" % self.max_size)
            try:
                c = self._free.get(timeout=wait)     # 先等归还
            except queue.Empty:
                continue
            try:
                c.ping()                             # 借出前验活
                return c
            except RuntimeError:
                with self._mu:
                    self._all.remove(c)
                c.close()                            # 坏连接置换, 继续等
                print("  [pool] 连接 #%d 健康检查失败, 已丢弃" % c.id)

    def _release(self, c):
        try:
            c.ping()
            self._free.put(c)
        except RuntimeError:
            with self._mu:
                self._all.remove(c)
            c.close()

    @contextlib.contextmanager
    def borrow(self, timeout=1.0):
        c = self._acquire(timeout)
        try:
            yield c
        finally:
            self._release(c)


pool = Pool(max_size=2)
with pool.borrow() as c1:
    print("拿到连接 #%d, 累计创建 %d" % (c1.id, pool.created))
with pool.borrow() as c1:
    print("再次借到 #%d (复用归还的连接)" % c1.id)

c = pool._acquire()
c.healthy = False            # 模拟连接在使用中被断开
pool._release(c)             # 归还时验活发现坏了 -> 直接丢弃
with pool.borrow() as c2:
    print("坏连接置换后拿到 #%d, 累计创建 %d" % (c2.id, pool.created))

held = [pool._acquire() for _ in range(2)]
try:
    pool._acquire(timeout=0.2)
except TimeoutError as e:
    print("打满后超时:", e)
for x in held:
    pool._release(x)
with pool.borrow() as c3:
    print("释放后可再借: #%d" % c3.id)
