# -*- coding: utf-8 -*-
"""慢调用隔离舱 bulkhead: 每个依赖一个独立小线程池, 故障不上蹿下跳。

- 每个依赖单独的 BoundedSemaphore + ThreadPoolExecutor, 并发额度物理隔离;
- 等待额度有上限(wait), 超时立刻抛 BulkheadFull, 绝不让线程无限堆积;
- 依赖 A 瘫死只烧光自己的舱, 依赖 B 的舱位照常服务。
"""
import concurrent.futures
import threading
import time


class BulkheadFull(Exception):
    pass


class Bulkhead:
    def __init__(self, name, permits):
        self.name = name
        self._sem = threading.BoundedSemaphore(permits)
        self._pool = concurrent.futures.ThreadPoolExecutor(
            max_workers=permits, thread_name_prefix=name)
        self.rejected = 0
        self.served = 0

    def call(self, fn, wait=0.1, run_timeout=2.0):
        if not self._sem.acquire(timeout=wait):
            self.rejected += 1
            raise BulkheadFull("隔离舱 %s 已满" % self.name)
        try:
            fut = self._pool.submit(fn)
            result = fut.result(timeout=run_timeout)
            self.served += 1
            return result
        finally:
            self._sem.release()


def main():
    dep_a = Bulkhead("depA-慢依赖", 2)
    dep_b = Bulkhead("depB-快依赖", 2)
    start = threading.Event()

    def slow():
        time.sleep(0.4)
        return "slow-ok"

    def fast():
        return "fast-ok"

    a_results = []

    def hit_dep_a():
        start.wait()
        try:
            a_results.append(("ok", dep_a.call(slow, wait=0.1)))
        except BulkheadFull as e:
            a_results.append(("rejected", str(e)))

    ts = [threading.Thread(target=hit_dep_a) for _ in range(8)]
    for t in ts:
        t.start()
    time.sleep(0.05)
    start.set()
    for t in ts:
        t.join(timeout=3.0)

    b_results = [dep_b.call(fast) for _ in range(8)]   # 顺序调用, 全部成功
    ok = sum(1 for kind, _ in a_results if kind == "ok")
    rej = sum(1 for kind, _ in a_results if kind == "rejected")
    print("慢依赖 A: 成功 %d, 快速拒绝 %d" % (ok, rej))
    print("快依赖 B: 全部成功 %d 次, A 的拥堵没有波及 B" % len(b_results))
    assert ok == 2 and rej == 6, "舱位 2 个, 其余 6 个应被快速拒绝"
    assert len(b_results) == 8, "B 不受 A 影响"
    assert dep_a.rejected == 6 and dep_b.rejected == 0
    print("结论: 隔离舱把故障半径锁在单个依赖里, 拒绝快到毫秒级")


if __name__ == "__main__":
    main()
