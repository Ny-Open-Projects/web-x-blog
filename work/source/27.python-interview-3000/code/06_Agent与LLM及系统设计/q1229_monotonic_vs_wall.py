"""单调钟 vs 墙钟:模拟时钟回拨,对比租约判定的两种实现。"""


class Lease:
    def __init__(self, ttl):
        self.ttl = ttl

    def acquire_wall(self, now_wall):
        self.wall_deadline = now_wall + self.ttl       # 用墙钟,可被回拨坑

    def acquire_mono(self, now_mono):
        self.mono_deadline = now_mono + self.ttl       # 用单调钟

    def valid_wall(self, now_wall):
        return now_wall < self.wall_deadline

    def valid_mono(self, now_mono):
        return now_mono < self.mono_deadline


if __name__ == "__main__":
    lease = Lease(ttl=10)
    lease.acquire_wall(now_wall=1000.0)
    lease.acquire_mono(now_mono=100.0)
    # 真实流逝 15s(单调钟 100 -> 115),期间 NTP 回拨 30s:墙钟 1000 -> 970+15=985
    wall_now, mono_now = 985.0, 115.0
    print("回拨后 墙钟判定有效:", lease.valid_wall(wall_now),
          "-> 回拨让租约看起来还剩 25s,锁超卖风险")
    assert lease.valid_wall(wall_now), "墙钟被回拨欺骗"
    print("真实时间已流逝 15s,单调钟判定有效:", lease.valid_mono(mono_now),
          "-> 正确判定已过期")
    assert not lease.valid_mono(mono_now), "单调钟正确判定已过期"
    # 正常推进(无时钟调整):两种钟判定一致
    lease2 = Lease(ttl=10)
    lease2.acquire_wall(1000.0)
    lease2.acquire_mono(200.0)
    assert lease2.valid_wall(1008.0) and lease2.valid_mono(208.0)
    print("正常推进两种钟判定一致;只有时钟调整时才分胜负")
    print("结论: 超时/租约/TTL 一律单调钟,墙钟只做日历时间")
