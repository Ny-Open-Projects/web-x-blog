"""实现 allkeys-lru 淘汰: OrderedDict 近似 Redis 的 LRU 淘汰池"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, maxmemory: int = 3):
        self._data: OrderedDict = OrderedDict()
        self._maxmemory = maxmemory

    def set(self, key, value) -> None:
        if key in self._data:
            self._data.move_to_end(key)     # 访问即置为新
        self._data[key] = value
        while len(self._data) > self._maxmemory:
            victim, _ = self._data.popitem(last=False)   # 淘汰最久未用
            print(f"内存超限, 淘汰 key={victim}")

    def get(self, key):
        if key not in self._data:
            return None
        self._data.move_to_end(key)
        return self._data[key]


if __name__ == "__main__":
    cache = LRUCache(maxmemory=3)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3)
    cache.get("a")            # a 变热
    cache.set("d", 4)         # 淘汰 b
    print("get a:", cache.get("a"), "get b:", cache.get("b"))
