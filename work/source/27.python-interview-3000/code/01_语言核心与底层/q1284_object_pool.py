import queue
import threading


class ConnectionPool:
    def __init__(self, factory, size):
        self._free = queue.LifoQueue()
        for i in range(size):
            self._free.put(factory(i))

    def acquire(self, timeout=None):
        return self._free.get(timeout=timeout)   # 池空:阻塞或超时

    def release(self, conn):
        self._free.put(conn)


if __name__ == "__main__":
    pool = ConnectionPool(lambda i: "conn-%d" % i, size=2)
    results = []

    def work(n):
        conn = pool.acquire(timeout=1)
        try:
            results.append((n, conn))
        finally:
            pool.release(conn)                   # 必还契约

    threads = [threading.Thread(target=work, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(sorted(results))
