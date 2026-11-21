"""会话续期的滑动窗口: 空闲超时与绝对上限双时钟(纯标准库)。"""


class SlidingSessions:
    """expires_at = min(last_seen + idle_ttl, created_at + max_ttl)。

    活跃用户靠 touch 不断顺延空闲线, 但绝对上限永不顺延:
    银行类会话 12 小时强制重认证, 就是这条 max_ttl 兜的底。
    """

    def __init__(self, idle_ttl=1800.0, max_ttl=86400.0, now=lambda: 0.0):
        self.idle_ttl = idle_ttl
        self.max_ttl = max_ttl
        self._now = now
        self.store = {}

    def create(self, sid, user):
        t = self._now()
        self.store[sid] = {"user": user, "created": t, "last": t,
                           "expires_at": min(t + self.idle_ttl, t + self.max_ttl)}
        return self.store[sid]["expires_at"]

    def touch(self, sid):
        """每次活跃请求调用; 三种结果: 新到期时间 / idle_expired / absolute_expired。"""
        s = self.store.get(sid)
        if s is None:
            return "missing"
        t = self._now()
        if t - s["last"] > self.idle_ttl:
            del self.store[sid]
            return "idle_expired"
        if t - s["created"] >= self.max_ttl:
            del self.store[sid]
            return "absolute_expired"
        s["last"] = t
        s["expires_at"] = min(t + self.idle_ttl, s["created"] + self.max_ttl)
        return s["expires_at"]


clock = {"t": 0.0}
ss = SlidingSessions(idle_ttl=1800.0, max_ttl=86400.0, now=lambda: clock["t"])
ss.create("s1", "u1")
clock["t"] = 1000.0
assert ss.touch("s1") == 2800.0, "活跃顺延空闲线"
clock["t"] = 2000.0
assert ss.touch("s1") == 3800.0
capped_at = None
for t in range(3000, 86301, 1000):  # 用户一直活跃, 每 1000 秒动一次
    clock["t"] = float(t)
    r = ss.touch("s1")
    if r == 86400.0 and capped_at is None:
        capped_at = t  # 到期时间被绝对上限封顶, 不再顺延
assert capped_at == 85000.0, capped_at  # 85000 起到达 min 上界
clock["t"] = 86300.0
assert ss.touch("s1") == 86400.0, "封顶后继续活跃也停在 86400"
clock["t"] = 86500.0
assert ss.touch("s1") == "absolute_expired", "活跃也必须重认证"
ss.create("s2", "u2")
clock["t"] = 88400.0
assert ss.touch("s2") == "idle_expired", "不活跃的会话到空闲线就死"
print("时间线: 顺延 -> 84600 秒起封顶 86400 -> 86500 强制重认证; 闲置 s2 空闲过期")
