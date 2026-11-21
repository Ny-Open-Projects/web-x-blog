import threading
import time


class PerThreadCounter:
    def __init__(self) -> None:
        self._local = threading.local()
        self._shards: list = []
        self._reg = threading.Lock()  # 只在首次注册时竞争

    def incr(self) -> None:
        shard = getattr(self._local, "shard", None)
        if shard is None:
            shard = self._local.shard = [0]
            with self._reg:
                self._shards.append(shard)
        shard[0] += 1  # 本地计数: 无锁无竞争

    def total(self) -> int:
        return sum(s[0] for s in self._shards)  # 弱一致快照


class LockedCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._n = 0

    def incr(self) -> None:
        with self._lock:
            self._n += 1

    def total(self) -> int:
        return self._n


def bench(counter, n_threads=4, n_iter=300000) -> float:
    ts = [
        threading.Thread(
            target=lambda: [counter.incr() for _ in range(n_iter)]
        )
        for _ in range(n_threads)
    ]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return time.perf_counter() - t0


if __name__ == "__main__":
    p, l = PerThreadCounter(), LockedCounter()
    tp = bench(p)
    tl = bench(l)
    print(f"per-thread: {tp:.3f}s, 单锁: {tl:.3f}s, 提速约 {tl / tp:.1f}x")
    print("计数校验:", p.total(), l.total(), "(期望均 1200000)")
    assert p.total() == l.total() == 4 * 300000
