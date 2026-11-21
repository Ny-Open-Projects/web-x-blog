"""Q2872 请求幂等的存储层实现:条件插入与进行中合并等待。

幂等最怕「查了没有,写时已有」的竞态。存储层原语 put_if_absent:
第一个调用者执行工厂函数,并发第二个发现同键在进行中,就地等待并
复用同一结果——工厂只跑一次,两个调用方拿到同一个值。
"""

import threading
import time


class IdempotentStore:
    def __init__(self):
        self._mu = threading.Lock()
        self._store = {}
        self._pending = {}   # key -> [Event, 结果盒子]

    def get_or_create(self, key, factory):
        with self._mu:
            if key in self._store:
                return self._store[key], "hit"
            if key in self._pending:
                ev = self._pending[key][0]
                role = "waiter"
            else:
                ev = threading.Event()
                self._pending[key] = [ev, None]
                role = "leader"
        if role == "leader":
            try:
                value = factory()
                with self._mu:
                    self._store[key] = value
                    self._pending[key][1] = value
                    del self._pending[key]
                    ev.set()
                return value, "created"
            except BaseException:
                with self._mu:
                    self._pending.pop(key, None)
                    ev.set()   # 唤醒等待者,让它们自己重试
                raise
        ev.wait(timeout=5)
        with self._mu:
            if key in self._store:
                return self._store[key], "waiter_hit"
        raise RuntimeError("领导者失败,等待者需重试")


def main():
    store = IdempotentStore()
    calls = {"n": 0}

    def slow_factory():
        calls["n"] += 1
        time.sleep(0.05)
        return {"order": "o1", "state": "paid"}

    start = threading.Barrier(2)
    got = {}

    def worker(i):
        start.wait()
        got[i] = store.get_or_create("pay:o1", slow_factory)

    ts = [threading.Thread(target=worker, args=(i,)) for i in (1, 2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    roles = sorted(v[1] for v in got.values())
    assert roles == ["created", "waiter_hit"], got
    assert got[1][0] == got[2][0], got
    assert calls["n"] == 1, calls   # 工厂只执行一次
    v3, role3 = store.get_or_create("pay:o1", slow_factory)
    assert role3 == "hit" and calls["n"] == 1
    print("两个并发角色:", roles)
    print("工厂执行次数:", calls["n"], "结果一致:", got[1][0] == got[2][0])
    print("后续调用直接命中:", role3)


if __name__ == "__main__":
    main()
