"""健康探针的依赖分级: critical 与 optional 的聚合(纯标准库)。"""
import time


class HealthChecker:
    """依赖分两级: critical 决定生死, optional 只降级不摘流。

    每个依赖的检查结果缓存 check_ttl 秒, 避免探针高频触发真实依赖检查。
    """

    def __init__(self, deps, check_ttl=5.0, clock=None):
        self.deps = deps                    # name -> (tier, check_fn)
        self.check_ttl = check_ttl
        self.now = clock or time.time
        self.cache = {}                     # name -> (ok, checked_at)

    def _check(self, name):
        ok, at = self.cache.get(name, (None, -1e18))
        if self.now() - at < self.check_ttl:
            return ok
        tier, fn = self.deps[name]
        try:
            ok = bool(fn())
        except Exception:
            ok = False
        self.cache[name] = (ok, self.now())
        return ok

    def readiness(self):
        """聚合就绪状态: critical 全好且至少可选依赖正常 -> 200, 否则分级。"""
        results = {name: self._check(name) for name in self.deps}
        critical_bad = [n for n, r in results.items()
                        if not r and self.deps[n][0] == "critical"]
        optional_bad = [n for n, r in results.items()
                        if not r and self.deps[n][0] == "optional"]
        if critical_bad:
            return 503, {"state": "down", "critical_failed": critical_bad}
        if optional_bad:
            return 200, {"state": "degraded", "degraded": optional_bad}
        return 200, {"state": "healthy", "dependencies": {n: r for n, r in results.items()}}


def fake_db():
    return True


def broken_cache():
    return False


checker = HealthChecker({"db": ("critical", fake_db),
                         "cache": ("optional", broken_cache),
                         "mq": ("critical", lambda: True)})
status, body = checker.readiness()
print("cache 挂掉 ->", status, body)
assert status == 200 and body["state"] == "degraded"

checker2 = HealthChecker({"db": ("critical", lambda: False),
                          "cache": ("optional", lambda: False)})
status, body = checker2.readiness()
print("db 挂掉 ->", status, body)
assert status == 503 and body["critical_failed"] == ["db"]

clock = {"t": 0.0}
flap = {"up": True}
checker3 = HealthChecker({"db": ("critical", lambda: flap["up"])},
                         check_ttl=10.0, clock=lambda: clock["t"])
r1 = checker3.readiness()[0]
flap["up"] = False
r2 = checker3.readiness()[0]        # TTL 内使用缓存结果, 仍是上次结论
clock["t"] += 11.0
r3 = checker3.readiness()[0]
print("抖动缓存: {} -> {} -> TTL 过期后 {}".format(r1, r2, r3))
assert r1 == 200 and r2 == 200 and r3 == 503
print("要点: 可选依赖挂了只降级不摘流, 关键依赖挂了才 503, 探针结果加 TTL 防止高频真检查")
