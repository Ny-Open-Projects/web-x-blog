"""命中率归因: 未命中必须拆原因, 否则优化没有抓手"""

class AttributedCache:
    def __init__(self, capacity, ttl_len=5):
        self.data = {}
        self.ttl = {}
        self.capacity = capacity
        self.ttl_len = ttl_len
        self.now = 0
        self.evicted = set()
        self.stats = {"hit": 0, "miss_cold": 0, "miss_expired": 0,
                      "miss_evicted": 0, "miss_bypass": 0}

    def set(self, key, value):
        while len(self.data) >= self.capacity and key not in self.data:
            victim = next(iter(self.data))
            del self.data[victim]
            del self.ttl[victim]
            self.evicted.add(victim)
        self.data[key] = value
        self.ttl[key] = self.now + self.ttl_len

    def get(self, key, now, bypass=False):
        self.now = now
        if bypass:
            self.stats["miss_bypass"] += 1
            return None
        if key not in self.data:
            if key in self.evicted:
                self.evicted.discard(key)
                self.stats["miss_evicted"] += 1
            else:
                self.stats["miss_cold"] += 1
            return None
        if now > self.ttl[key]:
            del self.data[key]
            del self.ttl[key]
            self.stats["miss_expired"] += 1
            return None
        self.stats["hit"] += 1
        return self.data[key]

cache = AttributedCache(capacity=2)
cache.set("a", 1)
cache.set("b", 2)
trace = [(0, "a", False), (1, "b", False), (2, "a", False), (6, "a", False),
         (7, "c", False), (8, "d", False), (9, "c", False), (9, "d", False), (9, "b", True)]
for t, k, bp in trace:
    cache.set("c", 3) if (t, k) == (7, "c") else None
    cache.set("d", 4) if (t, k) == (8, "d") else None
    v = cache.get(k, t, bypass=bp)
    print("t=%d get(%s) -> %-4s" % (t, k, v if v is not None else "None"))

s = cache.stats
total = sum(s.values())
print("归因:", s)
print("总命中率 %.0f%%  未命中: cold=%d expired=%d evicted=%d bypass=%d" % (
    s["hit"] * 100.0 / total, s["miss_cold"], s["miss_expired"],
    s["miss_evicted"], s["miss_bypass"]))
print("归因对动作: cold 调预热回填, expired 调 TTL, evicted 调容量, bypass 调口径")
