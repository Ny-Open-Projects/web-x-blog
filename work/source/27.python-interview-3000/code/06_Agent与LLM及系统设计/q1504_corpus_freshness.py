"""语料新鲜度管理:每源 TTL、过期扫描、按陈旧度与热度的刷新优先级队列。"""
import time


class CorpusFreshness:
    """新鲜度管家:记录每源最后刷新时间,TTL 过期即进入刷新队列,高分优先。"""

    def __init__(self, ttl_days, hotness=None, day=86400.0):
        self.ttl = ttl_days                # source -> 有效期天数
        self.last_refresh = {}             # source -> 时间戳
        self.hotness = hotness or {}       # source -> 查询热度 0-10
        self.day = day

    def touch(self, source, now=None):
        self.last_refresh[source] = now if now is not None else time.time()

    def age_days(self, source, now):
        return (now - self.last_refresh[source]) / self.day

    def stale_sources(self, now):
        """返回已过期源,并按 优先级 = 陈旧倍数 x 热度 排序。"""
        out = []
        for src, last in self.last_refresh.items():
            age = self.age_days(src, now)
            if age > self.ttl[src]:
                mult = age / self.ttl[src]
                score = round(mult * self.hotness.get(src, 1), 2)
                out.append({"source": src, "age_days": round(age, 1), "priority": score})
        return sorted(out, key=lambda r: -r["priority"])

    def freshness_ratio(self, now):
        """整体新鲜度 = 未过期源占比。"""
        total = len(self.last_refresh)
        fresh = sum(1 for s in self.last_refresh if self.age_days(s, now) <= self.ttl[s])
        return fresh / max(1, total)


if __name__ == "__main__":
    now = 1_700_000_000.0
    f = CorpusFreshness(ttl_days={"policy": 7, "news": 1, "faq": 30},
                        hotness={"policy": 8, "news": 10, "faq": 2})
    f.touch("policy", now - 20 * 86400)     # 超 TTL 约 2.9 倍
    f.touch("news", now - 3 * 86400)        # 超 TTL 3 倍
    f.touch("faq", now - 5 * 86400)         # 未过期

    stale = f.stale_sources(now)
    assert [s["source"] for s in stale] == ["news", "policy"], "按 陈旧倍数x热度 排序"
    assert stale[0]["priority"] == 30.0 and stale[1]["priority"] == 22.86
    assert f.freshness_ratio(now) == 1 / 3

    f.touch("news", now - 0.5 * 86400)      # 刷新后回到新鲜
    assert f.freshness_ratio(now) == 2 / 3
    assert f.stale_sources(now)[0]["source"] == "policy"

    hot_missing = CorpusFreshness(ttl_days={"a": 1}).stale_sources(now)
    assert hot_missing == [], "没有登记刷新时间的源不参与扫描 由接入方负责"
    print("新鲜度管理通过:news 优先级 30 排最前 刷新后占比 0.33→0.67")
