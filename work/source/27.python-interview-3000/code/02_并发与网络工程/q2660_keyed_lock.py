# -*- coding: utf-8 -*-
"""按键加锁管理器: 同一 key 串行, 不同 key 并行。

- 全局一把锁: 所有账户互相排队, 吞吐被无关节口拖累;
- 按 key 加锁: 只锁同一条资源, 互不相关的操作并行跑;
- 引用计数回收: 没人用的锁及时销毁, 管理器不随 key 数量无限膨胀。
"""
import threading
import time
from contextlib import contextmanager

WORK = 0.002                            # 模拟每笔操作 2ms 的真实工作量


class KeyedLocks:
    """每 key 一把锁, 引用计数归零即回收。"""

    def __init__(self):
        self._guard = threading.Lock()
        self._locks = {}
        self._refs = {}

    @contextmanager
    def hold(self, key):
        with self._guard:
            lk = self._locks.get(key)
            if lk is None:
                lk = threading.Lock()
                self._locks[key] = lk
                self._refs[key] = 0
            self._refs[key] += 1
        try:
            with lk:
                yield
        finally:
            with self._guard:
                self._refs[key] -= 1
                if self._refs[key] == 0:
                    self._locks.pop(key, None)
                    self._refs.pop(key, None)

    def live_locks(self):
        with self._guard:
            return len(self._locks)


balances = {}
ledger_lock = threading.Lock()           # 仅保护 balances 字典本身的读写


def work_on(km, key, ops):
    for _ in range(ops):
        with km.hold(key):               # 同 key 串行, 异 key 并行
            time.sleep(WORK)             # 锁内干点真活, 串行代价才显形
            with ledger_lock:
                balances[key] = balances.get(key, 0) + 1


if __name__ == "__main__":
    km = KeyedLocks()

    # 场景一: 4 个线程挤同一个 key -> 完全串行
    balances.clear()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=work_on, args=(km, "acct:hot", 20))
          for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    same = time.perf_counter() - t0

    # 场景二: 4 个线程各锁各的 key -> 完全并行
    balances.clear()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=work_on, args=(km, "acct:%d" % i, 20))
          for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    diff = time.perf_counter() - t0

    print("同 key 串行: %.3fs / 异 key 并行: %.3fs" % (same, diff))
    print("异 key 方案提速: %.1f 倍" % (same / diff))
    print("回收验证: 全部结束后存活锁数 =", km.live_locks(), "(应为 0)")
