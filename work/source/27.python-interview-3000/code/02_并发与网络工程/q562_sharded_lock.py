import threading
import time

SHARDS = 16


class ShardedCounter:
    def __init__(self, shards: int = SHARDS) -> None:
        self._shards = [{"lock": threading.Lock(), "data": {}} for _ in range(shards)]

    def _idx(self, key: str) -> int:
        return hash(key) % len(self._shards)

    def incr(self, key: str) -> None:
        shard = self._shards[self._idx(key)]
        with shard["lock"]:
            shard["data"][key] = shard["data"].get(key, 0) + 1

    def total(self) -> int:
        n = 0
        for shard in self._shards:  # 逐片快照, 结果可能略有延迟但不会错
            with shard["lock"]:
                n += sum(shard["data"].values())
        return n


class SingleLockCounter:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._data = {}

    def incr(self, key: str) -> None:
        with self._lock:
            self._data[key] = self._data.get(key, 0) + 1

    def total(self) -> int:
        with self._lock:
            return sum(self._data.values())


def bench(counter, n_threads=4, n_iter=50000) -> float:
    keys = [f"k{i % 64}" for i in range(n_iter)]

    def work(tid: int) -> None:
        for k in keys[tid::n_threads]:
            counter.incr(k)

    ts = [threading.Thread(target=work, args=(i,)) for i in range(n_threads)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return time.perf_counter() - t0


if __name__ == "__main__":
    s = ShardedCounter()
    o = SingleLockCounter()
    t_shard = bench(s)
    t_single = bench(o)
    print(f"分段锁: {t_shard:.3f}s, 单锁: {t_single:.3f}s")
    print("计数校验:", s.total(), o.total())
