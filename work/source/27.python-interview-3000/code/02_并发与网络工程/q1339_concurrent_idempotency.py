import threading
import time


class IdempotencyStore:
    def __init__(self, ttl: float = 1.0) -> None:
        self._ttl = ttl
        self._lock = threading.Lock()
        self._done = {}       # key -> (result, expire_at)
        self._inflight = {}   # key -> Event
        self.executions = 0

    def execute(self, key: str, fn):
        waiter = None
        while True:
            with self._lock:
                now = time.monotonic()
                rec = self._done.get(key)
                if rec and rec[1] > now:
                    return "CACHED", rec[0]          # TTL 内: 直接回结果
                ev = self._inflight.get(key)
                if ev is not None:
                    waiter = ev                       # 有 leader 在跑
                else:
                    self._inflight[key] = threading.Event()
                    break                             # 自己成为 leader
            waiter.wait(timeout=2.0)                  # 等 leader 写结果或失败退场
        try:
            result = fn()
            with self._lock:
                self.executions += 1
                self._done[key] = (result, time.monotonic() + self._ttl)
                waiter = self._inflight.pop(key, None)
            return "EXECUTED", result
        except BaseException:
            with self._lock:                          # 失败: 不缓存, 唤醒等待者
                waiter = self._inflight.pop(key, None)
            raise
        finally:
            if waiter:
                waiter.set()


def main() -> None:
    store = IdempotencyStore(ttl=1.0)
    results = []
    lock = threading.Lock()

    def business() -> str:
        time.sleep(0.1)                    # 模拟写库
        return "order-42"

    def requester():
        status, r = store.execute("idem-1", business)
        with lock:
            results.append((status, r))

    threads = [threading.Thread(target=requester) for _ in range(6)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    executed = sum(1 for s, _ in results if s == "EXECUTED")
    cached = sum(1 for s, _ in results if s == "CACHED")
    print(f"6 个并发同 key 请求: 真实执行 {executed} 次, 命中缓存 {cached} 次")
    assert executed == 1 and cached == 5 and len(set(r for _, r in results)) == 1

    time.sleep(1.05)                       # TTL 过期
    status, r = store.execute("idem-1", business)
    print(f"TTL 过期后再来: {status} {r} (业务时间窗外, 允许重新执行)")
    assert status == "EXECUTED"


if __name__ == "__main__":
    main()
