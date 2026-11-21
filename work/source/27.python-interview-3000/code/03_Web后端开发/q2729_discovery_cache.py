"""内部调用的服务发现缓存: TTL、负缓存与刷新失败供旧值(纯标准库)。"""


class DiscoveryCache:
    """实例列表缓存三层策略:

    - TTL 内直接用缓存, 挡住解析压力;
    - 解析结果为空是确定性答案, 进短负缓存, 防止空结果风暴;
    - 解析抛错是故障, TTL 到期后刷新失败继续供旧值并标记, 服务降级优于请求失败。
    """

    def __init__(self, resolver, ttl=30.0, neg_ttl=5.0, now=lambda: 0.0):
        self.resolver = resolver
        self.ttl = ttl
        self.neg_ttl = neg_ttl
        self._now = now
        self.cache = {}
        self.stale_served = []

    def get(self, service):
        t = self._now()
        entry = self.cache.get(service)
        if entry and t < entry["until"]:
            return entry["endpoints"]
        try:
            eps = self.resolver(service)
        except Exception:
            eps = None  # 故障, 与"确定性为空"区分开
        if eps is not None and not eps:
            self.cache[service] = {"endpoints": [], "until": t + self.neg_ttl}
            return []
        if eps:
            self.cache[service] = {"endpoints": eps, "until": t + self.ttl}
            return eps
        # 刷新失败: 还有旧值就续一段短命并标记, 没有则负缓存
        if entry and entry["endpoints"]:
            self.cache[service] = {"endpoints": entry["endpoints"], "until": t + self.neg_ttl}
            self.stale_served.append(service)
            return entry["endpoints"]
        self.cache[service] = {"endpoints": [], "until": t + self.neg_ttl}
        return []


class ScriptResolver:
    """按调用次序吐结果, 统计调用次数。"""

    def __init__(self, script):
        self.script = list(script)
        self.calls = []

    def __call__(self, service):
        self.calls.append(service)
        item = self.script.pop(0)
        if isinstance(item, Exception):
            raise item
        return item


clock = {"t": 0.0}
now = lambda: clock["t"]
resolver = ScriptResolver([["a:1", "a:2"], Exception("registry down"), [], ["a:3"]])
dc = DiscoveryCache(resolver, ttl=30.0, neg_ttl=5.0, now=now)

assert dc.get("a") == ["a:1", "a:2"]
assert dc.get("a") == ["a:1", "a:2"] and resolver.calls == ["a"], "TTL 内不再解析"
clock["t"] = 31.0
assert dc.get("a") == ["a:1", "a:2"], "解析抛错供旧值, 服务不中断"
assert dc.stale_served == ["a"]
clock["t"] = 37.0  # 旧值续命到期, 这次解析成功但返回空列表
assert dc.get("a") == [] and resolver.calls == ["a", "a", "a"], "确定性为空进负缓存"
clock["t"] = 43.0
assert dc.get("a") == ["a:3"] and resolver.calls[-1] == "a"
assert dc.get("ghost") == [], "从未成功的服务返回空列表而非异常"
print("调用轨迹:", resolver.calls, "降级供旧值:", dc.stale_served)
