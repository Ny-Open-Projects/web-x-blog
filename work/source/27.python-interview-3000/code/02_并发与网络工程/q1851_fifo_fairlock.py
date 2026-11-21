# -*- coding: utf-8 -*-
"""FIFO 公平锁: 队列票号保证先到先得, 消除线程饥饿。

- acquire 时原子登记到队列尾部拿票, 谓词是 "自己是队首且锁空闲";
- release 必须 notify_all: 只有队首能通过谓词, 其余唤醒后继续睡, 这是公平的代价;
- 六个线程同一瞬间起跑, 票号随机但服务顺序必须严格等于票号顺序。
"""
import collections
import threading
import time


class FairLock:
    def __init__(self):
        self._cond = threading.Condition()
        self._queue = collections.deque()
        self._owner = None
        self._next_ticket = 0

    def acquire(self, timeout=5.0):
        me = threading.get_ident()
        with self._cond:
            self._next_ticket += 1            # 全局唯一票号, 登记顺序即票号顺序
            ticket = self._next_ticket
            self._queue.append(me)
            deadline = time.monotonic() + timeout
            while self._owner is not None or self._queue[0] != me:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("公平锁等待超时")
                self._cond.wait(remain)
            self._queue.popleft()
            self._owner = me
            return ticket

    def release(self):
        with self._cond:
            if self._owner != threading.get_ident():
                raise RuntimeError("不能释放不属于当前线程的锁")
            self._owner = None
            self._cond.notify_all()           # 只让队首通过, 其余是无效唤醒

    def __enter__(self):
        return self.acquire()

    def __exit__(self, *exc):
        self.release()


def main():
    lock = FairLock()
    served = []
    tickets = {}
    served_lock = threading.Lock()
    start = threading.Event()

    def worker(name):
        start.wait()
        ticket = lock.acquire()
        with served_lock:
            tickets[name] = ticket
            served.append(name)
        time.sleep(0.01)                      # 持有一下, 观察交接
        lock.release()

    names = ["t%d" % i for i in range(6)]
    ts = [threading.Thread(target=worker, args=(n,)) for n in names]
    for t in ts:
        t.start()
    time.sleep(0.05)                          # 确保全员都堵在起跑线上
    start.set()
    for t in ts:
        t.join(timeout=5.0)
        assert not t.is_alive(), "公平锁不应饿死任何线程"

    print("服务顺序:", served)
    print("票号:", tickets)
    order_by_ticket = [n for n, _ in sorted(tickets.items(), key=lambda kv: kv[1])]
    assert sorted(tickets.values()) == [1, 2, 3, 4, 5, 6], "并发起跑票号连续唯一"
    assert served == order_by_ticket, "服务顺序必须等于票号顺序, 无人插队"
    print("结论: 票号即顺序, 公平锁用 notify_all 的浪费换无人饥饿")


if __name__ == "__main__":
    main()
