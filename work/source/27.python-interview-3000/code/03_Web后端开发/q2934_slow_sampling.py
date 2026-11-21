"""慢接口的采样统计: 水库抽样固定内存 + 分位数与慢请求率(纯标准库)。"""
import random


class RouteSampler:
    """每条路由只保留 k 个水库样本, 常数内存下估算分位数; 计数器走全量。"""

    def __init__(self, k=200, slow_ms=800):
        self.k = k
        self.slow_ms = slow_ms
        self._samples = {}
        self._count = {}
        self._slow = {}

    def record(self, route, duration_ms):
        self._count[route] = n = self._count.get(route, 0) + 1
        if duration_ms >= self.slow_ms:
            self._slow[route] = self._slow.get(route, 0) + 1
        bucket = self._samples.setdefault(route, [])
        if len(bucket) < self.k:
            bucket.append(duration_ms)
        else:
            j = random.randint(0, n - 1)   # 以 k/n 概率入样, 每条记录等概率
            if j < self.k:
                bucket[j] = duration_ms

    def report(self, route):
        data = sorted(self._samples[route])

        def pct(p):
            return data[min(int(len(data) * p), len(data) - 1)]

        n = self._count[route]
        return {
            "count": n,
            "sampled": len(data),
            "p50_ms": pct(0.50),
            "p95_ms": pct(0.95),
            "p99_ms": pct(0.99),
            "slow_rate": round(self._slow.get(route, 0) / n, 4) if n else 0.0,
        }


random.seed(7)
sampler = RouteSampler(k=100, slow_ms=800)

# 模拟流量: 常规耗时指数分布, 每 97 笔混入一笔慢调用
for i in range(3000):
    d = 30 + random.expovariate(1 / 120)
    if i % 97 == 0:
        d += 1500
    sampler.record("GET /api/orders", d)

for i in range(500):
    sampler.record("GET /api/health", 2 + random.random() * 3)
for i in range(800):
    sampler.record("GET /api/users", 50 + random.expovariate(1 / 90))

r1 = sampler.report("GET /api/orders")
print("orders:", r1)
r2 = sampler.report("GET /api/health")
print("health:", r2)

assert r1["count"] == 3000 and r1["sampled"] == 100, "样本数恒为 k"
assert r1["p50_ms"] < r1["p95_ms"] < r1["p99_ms"], "分位数单调"
assert 0.009 <= r1["slow_rate"] <= 0.012, "慢请求率约 1/97, 全量计数不抽样"
assert r2["p99_ms"] < 10 and r2["slow_rate"] == 0.0

# 样本池在扰动下仍稳定: 再打 10 万条也不扩内存
for i in range(100000):
    sampler.record("GET /api/orders", 40 + random.random() * 60)
r3 = sampler.report("GET /api/orders")
print("扰动后:", r3)
assert r3["sampled"] == 100

# top 榜: 按慢请求率排序, 找治理对象
routes = ["GET /api/orders", "GET /api/health", "GET /api/users"]
top = sorted(routes, key=lambda r: -sampler.report(r)["slow_rate"])[:2]
print("慢接口 top:", top)
assert top[0] == "GET /api/orders"
print("采样统计演示通过")
