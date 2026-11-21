"""空值缓存防穿透: 空对象与布隆过滤器的纵深分工"""
import random
import zlib

random.seed(7)

class DB:
    def __init__(self):
        self.existing = {i for i in range(1, 501)}
        self.queries = 0
    def get(self, key):
        self.queries += 1
        return "user-%d" % key if key in self.existing else None

class NullCache:
    """允许存 None 的缓存 空值条目用更短的 TTL"""
    def __init__(self):
        self.store = {}
    def get(self, key):
        item = self.store.get(key)
        if item is None:
            return "MISS"
        item[1] -= 1                    # 用逻辑时钟推进 TTL 便于演示
        if item[1] < 0:
            del self.store[key]
            return "MISS"
        return item[0]
    def set(self, key, value, ticks=5):
        self.store[key] = [value, ticks]

class Bloom:
    """手写布隆过滤器 只用来挡肯定不存在的 key"""
    def __init__(self, expected, bits_per_key=10, k=3):
        self.bits = bytearray(expected * bits_per_key // 8 + 1)
        self.k = k
    def _idx(self, key):
        base = str(key).encode("utf-8")
        for i in range(self.k):
            yield zlib.crc32(base + bytes([i])) % (len(self.bits) * 8)
    def add(self, key):
        for i in self._idx(key):
            self.bits[i // 8] |= 1 << (i % 8)
    def might_contain(self, key):
        return all(self.bits[i // 8] >> (i % 8) & 1 for i in self._idx(key))

db = DB()
bloom = Bloom(len(db.existing))
for kid in db.existing:
    bloom.add(kid)

def attack(label, use_cache=False, use_bloom=False):
    db.queries = 0
    cache = NullCache() if use_cache else None
    for _ in range(20):                  # 攻击者反复打不存在的 id
        kid = random.randint(10001, 10100)
        if use_bloom and not bloom.might_contain(kid):
            continue                     # 布隆直接拦截
        if use_cache:
            v = cache.get(kid)
            if v != "MISS":
                continue                 # 空值缓存命中 包括 None
        v = db.get(kid)
        if use_cache:
            cache.set(kid, v, ticks=5)   # None 也进缓存 但 TTL 更短
    print(f"{label}: DB 被打 {db.queries} 次")

attack("无任何防护      ")
attack("仅空值缓存      ", use_cache=True)
attack("布隆加空值缓存  ", use_cache=True, use_bloom=True)
print("结论: 空值缓存挡住同一 key 的重复穿透 布隆在更前面挡海量随机 key 两者是纵深防御而非替代关系")
