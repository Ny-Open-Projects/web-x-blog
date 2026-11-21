"""配额双窗口:短窗滑动限速防突刺,长窗管总配额,两道门全过才放行。"""


class DualWindowLimiter:
    def __init__(self, short_limit, short_window, long_quota):
        self.short_limit = short_limit           # 短窗内最多几次
        self.short_window = short_window         # 短窗长度 秒
        self.long_quota = long_quota             # 长窗总配额 次
        self.events = []                         # 放行时刻
        self.long_used = 0

    def allow(self, now):
        recent = [t for t in self.events if now - t < self.short_window]
        if len(recent) >= self.short_limit:
            return False, "short_window"
        if self.long_used >= self.long_quota:
            return False, "quota"
        self.events.append(now)
        self.long_used += 1
        return True, "ok"


if __name__ == "__main__":
    lim = DualWindowLimiter(short_limit=3, short_window=10.0, long_quota=5)
    ticks = [0.0, 1.0, 2.0, 3.0, 30.0, 31.0, 32.0]
    outcomes = [lim.allow(t) for t in ticks]

    assert outcomes[0] == (True, "ok") and outcomes[1] == (True, "ok") and outcomes[2] == (True, "ok")
    assert outcomes[3] == (False, "short_window"), "短窗第 4 次被限速"
    assert outcomes[4] == (True, "ok"), "短窗滑出后恢复"
    assert outcomes[6] == (False, "quota"), "长窗配额耗尽由第二道门拦截"
    assert lim.long_used == 5
    print("双窗口通过:短窗限突刺 长窗管总量,拒绝原因区分处置路径")
