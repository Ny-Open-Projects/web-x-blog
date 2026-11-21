"""带字节预算的本地缓存驱逐: 先清过期, 再逐出 LRU"""
import collections

class BudgetCache:
    def __init__(self, budget):
        self.budget = budget
        self.used = 0
        self.entries = collections.OrderedDict()   # key -> [value, size, expire_at]
        self.now = 0

    def get(self, key):
        item = self.entries.get(key)
        if item is None:
            return None
        value, size, expire_at = item
        if self.now >= expire_at:                  # 惰性过期
            del self.entries[key]
            self.used -= size
            return None
        self.entries.move_to_end(key)              # 访问即晋升为最近使用
        return value

    def set(self, key, value, size, ttl):
        self.now += 1
        expire_at = self.now + ttl
        if key in self.entries:
            self.used -= self.entries[key][1]
            del self.entries[key]
        self.entries[key] = [value, size, expire_at]
        self.used += size
        self._evict()

    def _evict(self):
        # 第一优先级: 过期项先走, 无论新旧
        expired = [(k, s) for k, (_, s, e) in self.entries.items() if self.now >= e]
        for k, s in expired:
            del self.entries[k]
            self.used -= s
        # 第二优先级: 仍超预算, 按最久未使用逐出
        while self.used > self.budget and self.entries:
            k, (_, s, _) = self.entries.popitem(last=False)
            self.used -= s
            print("  超预算, LRU 逐出 %s (回收 %d 字节)" % (k, s))

cache = BudgetCache(100)
cache.set("a", "A" * 30, 30, ttl=1)
cache.set("b", "B" * 30, 30, ttl=99)
cache.now += 5                                     # 时间前进, a 已过期
cache.set("c", "C" * 30, 30, ttl=99)               # 触发驱逐: 过期的 a 先被惰性清掉
print("过期优先后: 键=%s used=%d" % (list(cache.entries), cache.used))
assert "a" not in cache.entries

cache.set("d", "D" * 50, 50, ttl=99)               # 再塞大的, 超出预算
print("最终: 键=%s used=%d/%d" % (list(cache.entries), cache.used, cache.budget))
print("结论: 字节预算下的正确驱逐顺序是'过期项 -> LRU',")
print("      先逐出热点未过期项是最常见的实现事故, 会让命中率当场跳水")
