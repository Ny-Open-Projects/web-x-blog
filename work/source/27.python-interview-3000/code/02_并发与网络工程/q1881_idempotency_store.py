# -*- coding: utf-8 -*-
"""幂等重试的安全集合: 带 TTL 的去重台账, 并发同键只执行一次。

- 台账 key -> (结果, 过期时刻), 命中且未过期直接回放, 不再执行业务函数;
- 计算在锁内完成: 同 key 并发到达时, 后到者阻塞在锁上, 醒来已是回放;
- 守护清扫线程周期剔除过期条目, 台账不会无限膨胀, 过期后允许重新执行。
"""
import threading
import time


class IdempotencyStore:
    def __init__(self, ttl=0.4):
        self.ttl = ttl
        self._lock = threading.Lock()
        self._store = {}                       # key -> (result, expire_at)
        self.executes = 0
        self.duplicates = 0
        self.sweeps = 0
        self._stop = threading.Event()

    def execute(self, key, fn):
        with self._lock:
            hit = self._store.get(key)
            now = time.monotonic()
            if hit is not None and now < hit[1]:
                self.duplicates += 1
                return hit[0], "duplicate"     # 命中回放, 业务函数零执行
            result = fn()                      # 慢操作在锁内, 专注防重复
            self._store[key] = (result, now + self.ttl)
            self.executes += 1
            return result, "fresh"

    def sweep_loop(self):
        while not self._stop.wait(0.05):
            now = time.monotonic()
            with self._lock:
                expired = [k for k, (_, exp) in self._store.items()
                           if exp <= now]
                for k in expired:
                    del self._store[k]
                if expired:
                    self.sweeps += 1

    def stop(self):
        self._stop.set()


def main():
    store = IdempotencyStore(ttl=0.4)
    threading.Thread(target=store.sweep_loop, daemon=True).start()
    calls = []

    def business():
        calls.append("run")
        time.sleep(0.05)
        return "computed-once"

    # 6 个线程同 key 并发: 业务函数只应执行一次
    results = []
    res_lock = threading.Lock()

    def caller():
        r, kind = store.execute("order-42", business)
        with res_lock:
            results.append(kind)

    ts = [threading.Thread(target=caller) for _ in range(6)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=3.0)

    fresh = results.count("fresh")
    dup = results.count("duplicate")
    print("执行 %d 次, 回放 %d 次, 业务函数实际运行 %d 次"
          % (fresh, dup, len(calls)))
    assert fresh == 1 and dup == 5, "并发同键只执行一次"
    assert len(calls) == 1

    # TTL 过期后: 清扫线程剔除台账, 允许重新执行
    time.sleep(0.6)
    r, kind = store.execute("order-42", business)
    print("过期后再次执行:", kind, "累计业务执行", len(calls), "次")
    assert kind == "fresh" and len(calls) == 2
    assert store.sweeps >= 1, "清扫线程应剔除过期条目"

    # 不同 key 互不影响
    r2, kind2 = store.execute("order-43", lambda: "other")
    assert kind2 == "fresh"
    store.stop()
    print("结论: 台账 + TTL + 清扫, 是幂等去重的最小完整闭环")


if __name__ == "__main__":
    main()
