# -*- coding: utf-8 -*-
"""读计数的写入合并: 线程本地攒批, 一次锁提交一整批。

- 每次计数都拿锁: 8000 次自增就是 8000 次锁往返;
- 写入合并: 本地攒 100 次再合并提交, 锁次数砍到 1/100;
- 代价是可见性滞后: 观察者在合并点之间看到的是旧值。
"""
import threading
import time

N_THREADS = 4
N_INCR = 2000
FLUSH_EVERY = 100


class CountedLock:
    """包一层, 统计 acquire 次数, 用来对账锁的开销。"""

    def __init__(self):
        self._lock = threading.Lock()
        self.acquires = 0

    def __enter__(self):
        with self._lock:
            pass
        self.acquires += 1
        return self

    def __exit__(self, *exc):
        return False


total = [0]
lk = CountedLock()


def naive_worker():
    for _ in range(N_INCR):
        with lk:
            total[0] += 1


def merged_worker():
    buf = 0
    for i in range(1, N_INCR + 1):
        buf += 1
        if i % FLUSH_EVERY == 0:
            with lk:
                total[0] += buf       # 一把锁提交 100 次的量
            buf = 0
    if buf:
        with lk:
            total[0] += buf


def bench(fn):
    global total, lk
    total, lk = [0], CountedLock()
    mid_samples = []
    stop = threading.Event()

    def observer():
        while not stop.is_set():
            with lk:
                mid_samples.append(total[0])
            time.sleep(0.0005)

    obs = threading.Thread(target=observer)
    obs.start()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=fn) for _ in range(N_THREADS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    elapsed = time.perf_counter() - t0
    stop.set()
    obs.join()
    return elapsed, lk.acquires, mid_samples


if __name__ == "__main__":
    e1, a1, m1 = bench(naive_worker)
    e2, a2, m2 = bench(merged_worker)
    print("朴素逐次加锁: %.3fs, 锁 %d 次" % (e1, a1))
    print("合并提交:      %.3fs, 锁 %d 次 (应为 %d)"
          % (e2, a2, N_THREADS * (N_INCR // FLUSH_EVERY)))
    print("锁次数缩减: %.0f 倍" % (a1 / a2))
    expect = N_THREADS * N_INCR
    print("可见性滞后: 合并模式中途采样最大值 %d < 最终值 %d: %s"
          % (max(m2) if m2 else -1, expect, max(m2) < expect if m2 else False))
    print("两种模式最终计数一致:", total[0] == expect)
