"""缓存降级开关: 熔断 静默回源与探测恢复"""
import random

random.seed(1)

class FlakyCache:
    def __init__(self, fail_rate):
        self.fail_rate = fail_rate
        self.calls = 0
    def get(self, key):
        self.calls += 1
        if random.random() < self.fail_rate:
            raise TimeoutError("redis timeout")
        return None                        # 简化: 未命中即 None

class Service:
    def __init__(self, cache, db, fail_limit=3, probe_every=10):
        self.cache = cache
        self.db = db
        self.degraded = False
        self.fail_streak = 0
        self.fail_limit = fail_limit
        self.probe_every = probe_every
        self.probe_clock = 0
        self.stats = {"cache_hit": 0, "miss_to_db": 0, "degraded_to_db": 0}
    def read(self, key):
        if self.degraded:
            self.probe_clock += 1
            if self.probe_clock % self.probe_every == 0:   # 周期性探测是否恢复
                try:
                    self.cache.get(key)
                    self.degraded = False
                    self.fail_streak = 0
                except TimeoutError:
                    pass
            if self.degraded:
                self.stats["degraded_to_db"] += 1
                return self.db[key], "降级直读 DB"
        try:
            v = self.cache.get(key)
        except TimeoutError:
            self.fail_streak += 1
            if self.fail_streak >= self.fail_limit:        # 连续失败达阈值 进入熔断
                self.degraded = True
                self.probe_clock = 0
            self.stats["miss_to_db"] += 1
            return self.db[key], "缓存异常回源"
        self.fail_streak = 0
        if v is None:
            self.stats["miss_to_db"] += 1
            return self.db[key], "未命中回源"
        self.stats["cache_hit"] += 1
        return v, "命中"

db = {"k%d" % i: "db-%d" % i for i in range(50)}
cache = FlakyCache(fail_rate=0.5)
svc = Service(cache, db)
for i in range(60):
    svc.read("k%d" % (i % 50))
print("60 次读 cache 调用", cache.calls, "次 各路径:", svc.stats)
print("当前熔断状态:", svc.degraded, " 连续失败触发熔断后 流量不再打向故障的缓存层")
print("结论: 降级要静默 失败计数要连续触发 恢复靠周期探测而不是一直硬试 缓存故障不应拖垮 DB")
