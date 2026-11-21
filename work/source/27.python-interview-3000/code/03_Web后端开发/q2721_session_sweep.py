"""会话过期的回收: 惰性判定与定期清扫配合(纯标准库)。"""


class SessionStore:
    """惰性: 读到才判过期, 实现最简但冷数据会长期占内存;
    清扫: 定期批量删, 给存储体积一个上界, 两者缺一不可。
    """

    def __init__(self, now=lambda: 0.0):
        self.sessions = {}
        self._now = now

    def create(self, sid, user, ttl=3600.0):
        self.sessions[sid] = {"user": user, "expires_at": self._now() + ttl}

    def get(self, sid):
        s = self.sessions.get(sid)
        if s is not None and s["expires_at"] > self._now():
            return s
        self.sessions.pop(sid, None)  # 惰性删除: 撞见了才清
        return None

    def sweep(self, batch=100):
        """返回 (发现的过期数, 本次删除数); 批量上限防止清扫拖垮请求处理。"""
        t = self._now()
        expired = [sid for sid, s in self.sessions.items() if s["expires_at"] <= t]
        for sid in expired[:batch]:
            del self.sessions[sid]
        return len(expired), min(len(expired), batch)


clock = {"t": 0.0}
store = SessionStore(now=lambda: clock["t"])
for i in range(250):
    store.create("s%d" % i, "u", ttl=10.0 if i < 240 else 100000.0)
clock["t"] = 20.0

assert store.get("s0") is None, "惰性判定: 过期会话读即删"
found, removed = store.sweep(batch=100)
assert (found, removed) == (239, 100), (found, removed)  # s0 已被惰性删掉
found2, removed2 = store.sweep(batch=100)
assert (found2, removed2) == (139, 100)
found3, removed3 = store.sweep(batch=100)
assert (found3, removed3) == (39, 39)
assert len(store.sessions) == 10, "三轮清扫后只剩未过期的 10 个"
assert store.get("s240") is not None, "未过期会话不受清扫影响"
print("过期 240 个: 惰性删 1 个, 批量清扫按 100/轮 三轮清完, 存储 250 -> 10")
