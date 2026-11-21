"""命中率统计与环比告警"""
class CacheMetrics:
    def __init__(self):
        self.hits = self.misses = 0

    def hit(self):
        self.hits += 1

    def miss(self, source="expiry"):
        self.misses += 1
        self.last_miss_source = source

    @property
    def hit_rate(self):
        total = self.hits + self.misses
        return self.hits / total if total else 1.0

def alert(current, baseline, drop_threshold=0.05):
    drop = baseline - current
    if drop > drop_threshold:
        actions = ["检查最近发布是否改了 key 或 TTL",
                   "看 evicted 是否容量不足",
                   "看是否有批量过期或主动清缓存"]
        return f"命中率 {current:.0%} 较基线 {baseline:.0%} 下降 {drop:.0%} -> " + \
               "; ".join(actions)
    return f"命中率 {current:.0%} 正常"

if __name__ == "__main__":
    m = CacheMetrics()
    for i in range(800):
        m.hit()
    for i in range(200):
        m.miss()
    print(f"当前命中率: {m.hit_rate:.0%}")
    print(alert(m.hit_rate, baseline=0.95))
    print("配套指标: evicted 速率 / P99 RTT / 回源 QPS / 对账差异量")
