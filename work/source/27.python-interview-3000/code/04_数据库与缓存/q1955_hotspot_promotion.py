"""热点探测与本地缓存晋升: 滑窗计数与降级出口"""
from collections import deque

class HotspotDetector:
    """滑动窗口计数: 超过绝对阈值的热 key 才算热点"""
    def __init__(self, window=1000, min_count=30):
        self.window = window
        self.min_count = min_count
        self.events = deque()
        self.counts = {}
    def observe(self, key):
        self.events.append(key)
        self.counts[key] = self.counts.get(key, 0) + 1
        if len(self.events) > self.window:
            old = self.events.popleft()
            self.counts[old] -= 1
            if self.counts[old] <= 0:
                del self.counts[old]
    def hot_keys(self):
        return sorted(((k, c) for k, c in self.counts.items() if c >= self.min_count),
                      key=lambda x: -x[1])

class TieredCache:
    """L1 本地缓存只放晋升的热点 L2 全量 未命中走回源"""
    def __init__(self):
        self.l1 = {}
        self.l2 = {}
        self.stats = {"l1_hit": 0, "l2_hit": 0, "source": 0}
    def get(self, key):
        if key in self.l1:
            self.stats["l1_hit"] += 1
            return self.l1[key]
        if key in self.l2:
            self.stats["l2_hit"] += 1
            return self.l2[key]
        self.stats["source"] += 1
        value = "db-" + key
        self.l2[key] = value
        return value
    def promote(self, key):
        if key in self.l2 and key not in self.l1:
            self.l1[key] = self.l2[key]

cache = TieredCache()
detector = HotspotDetector(window=1000, min_count=30)
traffic = (["star"] * 60) + (["viral"] * 40) + ["norm-%d" % (i % 200) for i in range(900)]
for key in traffic:
    cache.get(key)
    detector.observe(key)

hot = [k for k, _ in detector.hot_keys()]
print("探测到的热点 ->", hot)
for k in hot:
    cache.promote(k)

cache.stats.update({"l1_hit": 0, "l2_hit": 0, "source": 0})
for key in traffic:
    cache.get(key)
print("晋升后一轮   ->", cache.stats, " 热点读全部落在 L1 不再走网络")

# 热度退潮: key 滑出窗口后探测器不再报它 晋升缓存必须跟着降级否则本地越堆越大
detector2 = HotspotDetector(window=1000, min_count=30)
for key in ["norm-%d" % (i % 200) for i in range(1000)]:
    detector2.observe(key)
print("热度退潮后   ->", detector2.hot_keys(), " 应触发 L1 降级回收")
print("结论: 晋升条件要看绝对次数防长尾误晋升 晋升与降级都必须有出口 本地缓存还要配短 TTL")
