"""互斥锁 singleflight: 同一 key 并发重建只放行一个"""
import threading
import time


class SingleFlightCache:
    def __init__(self):
        self.store: dict = {}
        self.key_locks: dict = {}
        self._guard = threading.Lock()
        self.db_calls = 0

    def _lock_for(self, key: str) -> threading.Lock:
        with self._guard:                       # 只保护锁表的创建
            return self.key_locks.setdefault(key, threading.Lock())

    def get(self, key: str, loader):
        if key in self.store:
            return self.store[key]
        lk = self._lock_for(key)
        with lk:                                # 同 key 串行, 其余线程在此等待
            if key in self.store:               # 双重检查: 等待期间别人已重建
                return self.store[key]
            self.db_calls += 1
            value = loader(key)
            self.store[key] = value
            return value


if __name__ == "__main__":
    cache = SingleFlightCache()

    def slow_loader(key: str) -> str:
        time.sleep(0.1)                          # 模拟 DB 慢查询
        return f"value-of-{key}"

    def worker(results: list, i: int):
        results[i] = cache.get("hot:key", slow_loader)

    results = [None] * 20
    threads = [threading.Thread(target=worker, args=(results, i)) for i in range(20)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("20 个并发请求, DB 实际查询次数:", cache.db_calls)   # 1
