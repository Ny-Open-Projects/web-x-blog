# -*- coding: utf-8 -*-
"""锁竞争的观测: 把每次获取锁的排队时间记下来。

- 包装 Lock 记录 acquire 的等待时长, 竞争程度就有了数字;
- 单线程时等待恒为零, 线程一多, p95 和 max 迅速抬头;
- 排队时间的分布比平均值更有用, 它直接对应请求的尾延迟。
"""
import threading
import time


class InstrumentedLock:
    def __init__(self):
        self._lock = threading.Lock()
        self._agg_lock = threading.Lock()
        self.waits = []

    def acquire(self):
        t0 = time.monotonic()
        self._lock.acquire()
        waited = time.monotonic() - t0
        with self._agg_lock:
            self.waits.append(waited)

    def release(self):
        self._lock.release()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *exc):
        self.release()

    def percentile(self, p):
        data = sorted(self.waits)
        if not data:
            return 0.0
        idx = min(len(data) - 1, int(len(data) * p))
        return data[idx]


def hammer(lock, iters, hold_s, gap_s):
    for _ in range(iters):
        with lock:
            time.sleep(hold_s)
        time.sleep(gap_s)


def run(n_threads, iters=40):
    lock = InstrumentedLock()
    threads = [threading.Thread(target=hammer,
                                args=(lock, iters, 0.001, 0.001))
               for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return lock


def main():
    solo = run(1)
    print("1 线程: p50=%.3fms p95=%.3fms max=%.3fms" %
          (solo.percentile(0.5) * 1000, solo.percentile(0.95) * 1000,
           max(solo.waits) * 1000))
    hot = run(8)
    print("8 线程: p50=%.3fms p95=%.3fms max=%.3fms, 采样 %d 次" %
          (hot.percentile(0.5) * 1000, hot.percentile(0.95) * 1000,
           max(hot.waits) * 1000, len(hot.waits)))
    assert solo.percentile(0.95) < 0.001, "单线程排队应接近零"
    assert hot.percentile(0.95) > 0.001, "8 线程下 p95 排队应超过一次持锁时长"


if __name__ == "__main__":
    main()
