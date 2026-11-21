"""用队列模拟连接池的借出与归还语义"""
import queue


class FakeConn:
    def __init__(self, cid: int):
        self.cid, self.in_use = cid, False

    def execute(self, sql: str) -> str:
        return f"conn#{self.cid} 执行 {sql}"


class MiniPool:
    def __init__(self, size: int = 3):
        self.idle: queue.Queue = queue.Queue(maxsize=size)
        for i in range(size):
            self.idle.put(FakeConn(i))

    def borrow(self, timeout: float = 1.0) -> FakeConn:
        try:
            return self.idle.get(timeout=timeout)
        except queue.Empty:
            raise RuntimeError("连接池已耗尽, 请调大池或检查连接泄漏")

    def give_back(self, conn: FakeConn) -> None:
        self.idle.put(conn)


if __name__ == "__main__":
    pool = MiniPool()
    c1 = pool.borrow()
    print(c1.execute("SELECT 1"))
    pool.give_back(c1)
    print("池中空闲连接数:", pool.idle.qsize())
