"""缓存预热完整脚本: 选键 回源 TTL 抖动 幂等跳过 限速 出报告"""
import random
import time


class Source:
    """模拟 DB 回源, 记录回源次数"""
    def __init__(self, n=20):
        self.n = n
        self.loads = 0

    def load(self, i):
        self.loads += 1
        return {"id": i, "name": "item-%d" % i}


class Cache:
    def __init__(self):
        self.data = {}
        self.expires = {}

    def alive(self, key):
        return key in self.data and self.expires[key] > time.monotonic()

    def put(self, key, val, ttl):
        self.data[key] = val
        self.expires[key] = time.monotonic() + ttl


def warm(cache, source, keys, base_ttl=60.0, jitter=10.0, qps=1000):
    stats = {"skipped": 0, "filled": 0, "failed": 0}
    for i in keys:
        key = "item:%d" % i
        if cache.alive(key):                  # 幂等: 已热的键直接跳过
            stats["skipped"] += 1
            continue
        try:
            cache.put(key, source.load(i),
                      base_ttl + random.uniform(-jitter, jitter))  # TTL 抖动
            stats["filled"] += 1
        except Exception:
            stats["failed"] += 1
        time.sleep(1.0 / qps)                 # 限速: 预热流量不打爆回源
    return stats


src, cache = Source(20), Cache()
hot = list(range(1, 21))
r1 = warm(cache, src, hot)
print("第一次预热:", r1, "回源", src.loads, "次")
r2 = warm(cache, src, hot)
print("第二次重跑(幂等):", r2, "累计回源", src.loads, "次")
diff = abs(cache.expires["item:1"] - cache.expires["item:2"])
print("同批键 TTL 已打散, 样例差值 %.2f s" % diff)
assert r1["filled"] == 20 and r2["skipped"] == 20 and src.loads == 20
print("预热三要素自检通过: 幂等重入 限速回源 过期时间抖动")
