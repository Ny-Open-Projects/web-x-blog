"""键空间分段: 前缀即命名空间, 隔离 TTL 配额与清理半径"""

class SegmentedCache:
    def __init__(self):
        self.data = {}

    def set(self, seg, key, value, ttl=None, quota=None):
        full = seg + ":" + key
        if quota is not None:
            same = [k for k in self.data if k.startswith(seg + ":")]
            if len(same) >= quota:
                victim = same[0]
                print("  段 %s 超配额, 先淘汰 %s" % (seg, victim))
                del self.data[victim]
        self.data[full] = (value, ttl)
        return full

    def clear_segment(self, seg):
        victims = [k for k in self.data if k.startswith(seg + ":")]
        for k in victims:
            del self.data[k]
        return len(victims)

    def keys(self):
        return sorted(self.data)

cache = SegmentedCache()
cache.set("sess", "u1", "token-a", ttl=1800)
cache.set("sess", "u2", "token-b", ttl=1800)
cache.set("cfg", "pay_channel", "on", ttl=86400)
cache.set("tmp", "export-1", "bytes...", ttl=60)
print("现有键:", cache.keys())
n = cache.clear_segment("tmp")
print("只清 tmp 段, 删了 %d 个键 -> 清理半径被前缀框住" % n)
print("剩余键:", cache.keys())
cache.set("tmp", "x1", "a", quota=1)
cache.set("tmp", "x2", "b", quota=1)
print("分段让 TTL 配额 清理 故障半径都按段隔离, 键规范要当成 API 维护")
