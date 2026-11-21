"""stale-while-revalidate: 过期后先回旧值, 触发刷新"""

class SwrCache:
    def __init__(self, loader, ttl, stale_window):
        self.loader = loader
        self.ttl = ttl
        self.stale_window = stale_window
        self.value = None
        self.fetched_at = None
        self.refreshing = False

    def get(self, now):
        if self.value is None:
            self.value = self.loader()
            self.fetched_at = now
            return self.value, "miss 同步回源"
        age = now - self.fetched_at
        if age < self.ttl:
            return self.value, "fresh"
        if age < self.ttl + self.stale_window:
            if not self.refreshing:
                self.refreshing = True
                old = self.value
                self.value = self.loader()   # 同步调用模拟后台刷新完成
                self.fetched_at = now
                self.refreshing = False
                return old, "stale 先回旧值 刷新已触发"
            return self.value, "stale 刷新进行中 返回旧值"
        self.value = self.loader()
        self.fetched_at = now
        return self.value, "硬过期 同步回源"

calls = {"n": 0}
def loader():
    calls["n"] += 1
    return "data-v%d" % calls["n"]

cache = SwrCache(loader, ttl=10, stale_window=5)
for now in (0, 5, 11, 13, 26):
    v, why = cache.get(now)
    print("t=%-3d 返回 %-8s 状态=%s" % (now, v, why))
print("SWR 用允许旧值的窗口换掉回源毛刺, 刷新必须单飞, 硬过期是最终兜底")
