"""滑动 TTL: 热键不冻结 冷键自然淘汰, 但要给绝对上限"""
import collections

class SlidingTTLCache:
    def __init__(self, idle_ttl, absolute_cap):
        self.idle_ttl = idle_ttl          # 空闲多久算过期 (访问即续期)
        self.absolute_cap = absolute_cap  # 无论多热, 从创建起最多活这么久
        self.entries = collections.OrderedDict()   # key -> [value, last_at, born_at]

    def get(self, key, now):
        item = self.entries.get(key)
        if item is None:
            return None
        value, last_at, born_at = item
        if now - last_at >= self.idle_ttl or now - born_at >= self.absolute_cap:
            del self.entries[key]
            return None
        item[1] = now                                # 滑动: 访问刷新空闲时钟
        self.entries.move_to_end(key)
        return value

    def set(self, key, value, now):
        born_at = self.entries.get(key, [None, None, now])[2]
        self.entries[key] = [value, now, born_at]
        self.entries.move_to_end(key)

cache = SlidingTTLCache(idle_ttl=10, absolute_cap=50)
cache.set("hot", "H", now=0)
cache.set("cold", "C", now=0)
for now in range(1, 46):
    cache.get("hot", now)              # 热键被持续访问, 空闲时钟一直被续
cold_gone = cache.get("cold", 15) is None   # 冷键 10 tick 空闲后消失
print("tick=15: 冷键已淘汰=%s, 热键仍在=%s" % (cold_gone, cache.get("hot", 15) == "H"))
alive = cache.get("hot", 50) is not None    # 热键再热, 也活不过绝对上限
print("tick=50: 热键是否仍存活(应被绝对上限终结)=%s" % (not alive))
print("键=%s" % list(cache.entries))
print("结论: 纯滑动 TTL 会让永久热点变成永生键, 占着预算不放手;")
print("      滑动过期配绝对上限, '活跃'与'新鲜'两个语义各管各的")
