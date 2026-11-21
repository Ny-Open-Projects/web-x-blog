"""外部数据的保鲜缓存与降级快照: 宁可标旧, 不编数据(纯标准库)。"""


class FetchError(Exception):
    pass


class FreshCache:
    """三层读法: 新鲜窗口直接用; 过期刷新, 失败退快照并标 stale;
    无快照或快照超过 max_stale 就显式抛错, 调用方决定降级文案。
    """

    def __init__(self, fetcher, ttl=60.0, max_stale=86400.0, now=lambda: 0.0):
        self.fetcher = fetcher
        self.ttl = ttl
        self.max_stale = max_stale
        self._now = now
        self.items = {}

    def get(self, key):
        t = self._now()
        entry = self.items.get(key)
        if entry and t < entry["until"]:
            return entry["value"], "fresh"
        try:
            value = self.fetcher(key)
            self.items[key] = {"value": value, "until": t + self.ttl, "fetched_at": t}
            return value, "refreshed"
        except FetchError:
            if entry and t - entry["fetched_at"] <= self.max_stale:
                return entry["value"], "stale"
            raise


class ScriptFetcher:
    def __init__(self, script):
        self.script = list(script)

    def __call__(self, key):
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


clock = {"t": 0.0}
now = lambda: clock["t"]
fetcher = ScriptFetcher([6.8, FetchError("upstream down"), FetchError("upstream down")])
fc = FreshCache(fetcher, ttl=60.0, max_stale=900.0, now=now)

v, m = fc.get("usd")
assert (v, m) == (6.8, "refreshed")
clock["t"] = 10.0
assert fc.get("usd") == (6.8, "fresh"), "TTL 内不再请求上游"
clock["t"] = 70.0
assert fc.get("usd") == (6.8, "stale"), "刷新失败退快照并标记"
clock["t"] = 1000.0  # 超过 max_stale, 快照也不可信
try:
    fc.get("usd")
except FetchError:
    print("快照过期 -> 显式失败, 由调用方给降级文案")
empty = FreshCache(ScriptFetcher([FetchError("down")]), now=now)
try:
    empty.get("usd")
except FetchError:
    print("无快照且上游不可用 -> 不编造默认值, 直接抛错")
print("读法轨迹: refreshed -> fresh -> stale -> 超限抛错, 快照永远带标记出门")
