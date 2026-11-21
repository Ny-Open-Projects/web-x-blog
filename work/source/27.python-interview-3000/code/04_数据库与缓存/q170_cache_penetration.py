"""简易布隆过滤器 + 空值缓存防穿透"""
import hashlib


class BloomFilter:
    def __init__(self, bits: int = 1 << 12, hashes: int = 3):
        self.bits = bytearray(bits // 8)
        self.size = bits
        self.hashes = hashes

    def _positions(self, item: str):
        for i in range(self.hashes):
            h = int(hashlib.md5(f"{i}:{item}".encode()).hexdigest(), 16)
            yield h % self.size

    def add(self, item: str) -> None:
        for p in self._positions(item):
            self.bits[p // 8] |= 1 << (p % 8)

    def might_contain(self, item: str) -> bool:
        return all(self.bits[p // 8] >> (p % 8) & 1 for p in self._positions(item))


class Cache:
    EMPTY = object()          # 空值标记

    def __init__(self):
        self.store: dict = {}
        self.bloom = BloomFilter()
        self.db_calls = 0

    def add_id(self, key: str):
        self.bloom.add(key)

    def get(self, key: str, db_loader):
        if key in self.store:
            return self.store[key], "cache"
        if not self.bloom.might_contain(key):     # 一定不存在, 拦截
            return None, "bloom"
        self.db_calls += 1
        value = db_loader(key)
        self.store[key] = value if value is not None else self.EMPTY
        return value, "db"


if __name__ == "__main__":
    cache = Cache()
    cache.add_id("item:1")
    loader = lambda k: {"item:1": "数据A"}.get(k)
    print(cache.get("item:1", loader))     # db 加载
    print(cache.get("item:1", loader))     # cache 命中
    print(cache.get("item:404", loader))   # bloom 拦截, db_calls 不增加
    print("DB 查询次数:", cache.db_calls)
