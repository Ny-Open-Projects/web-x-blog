import threading
import time
from contextlib import contextmanager


class FakeConn:
    _id = 0

    def __init__(self) -> None:
        FakeConn._id += 1
        self.id = FakeConn._id
        self.alive = True

    def ping(self) -> bool:
        return self.alive

    def close(self) -> None:
        self.alive = False


class ConnectionPool:
    def __init__(self, max_size: int = 3) -> None:
        self._idle = []
        self._created = 0
        self._max = max_size
        self._cond = threading.Condition()
        self.discarded = 0

    @contextmanager
    def borrow(self, timeout: float = 1.0):
        conn = self._acquire(timeout)
        try:
            yield conn
        except Exception:
            self._discard(conn)           # 异常连接状态不可信, 弃用
            raise
        else:
            self._release(conn)

    def _acquire(self, timeout: float) -> FakeConn:
        deadline = time.monotonic() + timeout
        with self._cond:
            while True:
                while self._idle:
                    conn = self._idle.pop()
                    if conn.ping():
                        return conn       # 健康检查通过才借出
                    self.discarded += 1   # 空闲期被对端掐掉: 就地换新
                    self._created -= 1
                    conn.close()
                if self._created < self._max:
                    self._created += 1
                    return FakeConn()
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("连接池借出超时")
                self._cond.wait(remaining)

    def _release(self, conn: FakeConn) -> None:
        with self._cond:
            if conn.ping():
                self._idle.append(conn)
            else:
                self._created -= 1
                self.discarded += 1
            self._cond.notify()

    def _discard(self, conn: FakeConn) -> None:
        with self._cond:
            conn.close()
            self._created -= 1
            self.discarded += 1
            self._cond.notify()


def main() -> None:
    pool = ConnectionPool(max_size=2)

    # 事故一: 借出期间调用方抛异常 -> 连接弃用不归还
    try:
        with pool.borrow() as conn:
            conn.alive = False           # 模拟使用中坏掉
            raise RuntimeError("业务炸了")
    except RuntimeError:
        pass
    print(f"事故一: 弃用 {pool.discarded} 个, 池内未腐蚀")

    # 事故二: 空闲连接被对端掐掉 -> 借出前健康检查换新
    with pool.borrow() as c1:
        pass                             # 正常归还一个
    with pool.borrow() as c2:
        c2.alive = False                 # 归还后悄悄死掉
    with pool.borrow() as c3:
        assert c3.ping(), "健康检查应保证借出的连接是活的"
        print(f"事故二: 死连接被替换为新连接 id={c3.id}")
        assert c3.id > c2.id

    # 压力: 多线程借还, 容量守恒
    errs = []
    def hammer():
        for _ in range(50):
            try:
                with pool.borrow() as c:
                    time.sleep(0.0005)
                    assert c.ping()
            except Exception as exc:
                errs.append(exc)
    threads = [threading.Thread(target=hammer) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errs
    print(f"200 次并发借还零失败, created={pool._created} 守恒于 max=2, 弃用累计 {pool.discarded}")
    assert pool._created <= 2


if __name__ == "__main__":
    main()
