import collections
import threading
import time


class LRUTTLCache:
    def __init__(self, capacity: int, ttl: float) -> None:
        self._capacity = capacity
        self._ttl = ttl
        self._data = collections.OrderedDict()  # key -> (value, expire_at)
        self._lock = threading.Lock()
        self.hit = 0
        self.miss = 0
        self.evicted = 0
        self.expired = 0

    def get(self, key):
        now = time.monotonic()
        with self._lock:
            item = self._data.get(key)
            if item is None:
                self.miss += 1
                return None
            value, expire_at = item
            if expire_at <= now:
                del self._data[key]
                self.expired += 1
                return None
            self._data.move_to_end(key)
            self.hit += 1
            return value

    def put(self, key, value) -> None:
        now = time.monotonic()
        with self._lock:
            self._data[key] = (value, now + self._ttl)
            self._data.move_to_end(key)
            while len(self._data) > self._capacity:
                self._data.popitem(last=False)
                self.evicted += 1


def main() -> None:
    cache = LRUTTLCache(capacity=3, ttl=0.1)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.put("d", 4)                    # 挤出最久未用的 a
    assert cache.get("a") is None
    assert cache.get("d") == 4
    cache.put("e", 5)                    # 挤出 b
    assert cache.get("b") is None
    time.sleep(0.15)                     # 全部过期
    assert cache.get("c") is None and cache.get("e") is None

    cache2 = LRUTTLCache(capacity=100, ttl=10)
    def worker(seed: int) -> None:
        for i in range(2000):
            k = (i * seed) % 50
            if i % 3 == 0:
                cache2.put(k, k)
            else:
                v = cache2.get(k)
                assert v is None or v == k
    threads = [threading.Thread(target=worker, args=(s + 1,)) for s in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"驱逐 {cache.evicted}, 过期 {cache.expired}; "
          f"并发后 命中 {cache2.hit} 未命中 {cache2.miss}, 容量守恒 {len(cache2._data) <= 100}")
    print("LRU + TTL 语义验证通过")


if __name__ == "__main__":
    main()
