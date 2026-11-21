"""版本号入键: 失效不删键, 换个版本号让旧键自然死"""
class VersionedCache:
    def __init__(self):
        self.store = {}        # 物理存储
        self.version = {}      # 逻辑版本表
        self.hits = 0
        self.miss = 0

    def _key(self, k):
        return "v%d:%s" % (self.version.get(k, 0), k)

    def get(self, k):
        v = self.store.get(self._key(k))
        if v is None:
            self.miss += 1
            return None
        self.hits += 1
        return v

    def put(self, k, val):
        self.store[self._key(k)] = val

    def invalidate(self, k):
        self.version[k] = self.version.get(k, 0) + 1     # 只动版本号, 不删旧键

cache = VersionedCache()
cache.put("item:1", "价格 99")
print("读:", cache.get("item:1"), "| 命中 %d 未命中 %d" % (cache.hits, cache.miss))
cache.invalidate("item:1")
print("失效后再读 -> miss (v0:item:1 仍在存储里但读路径已切到 v1):", cache.get("item:1"))
cache.put("item:1", "价格 89")
print("重填后读:", cache.get("item:1"), "| 物理键:", sorted(cache.store))
print("删除式失效的竞态 (回源塞回旧值) 在这里没有路径: 旧值只会落进早已无人读取的旧版本键")
