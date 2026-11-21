"""时间戳窗口与 nonce 的联合校验: 时钟偏移容忍的边界(纯标准库)。"""

SKEW = 90                                          # 允许的时钟偏移秒数
WINDOW = 2 * SKEW                                  # nonce 保留窗口须覆盖两端偏移


class ReplayGuard:
    def __init__(self):
        self.seen = {}

    def verify(self, ts, nonce, now):
        """先查时间窗, 再查 nonce; 返回 (状态码, 原因)。"""
        if abs(now - ts) > SKEW:
            return 401, "timestamp_out_of_range"
        if self.seen.get(nonce, -1) > now - WINDOW:
            return 401, "nonce_replayed"
        self.seen[nonce] = now
        return 200, "ok"

    def forget_outside(self, now):
        """只允许遗忘窗口外的 nonce, 保证窗口覆盖两端偏移。"""
        stale = [n for n, t in self.seen.items() if now - t > WINDOW]
        for n in stale:
            del self.seen[n]
        return stale


guard = ReplayGuard()
cases = [
    (1000, "n1", 1050, "时钟正常"),
    (970, "n2", 1050, "偏移在容忍内"),
    (800, "n3", 1050, "太旧"),
    (1200, "n4", 1050, "来自未来"),
]
for ts, nonce, now, label in cases:
    code, reason = guard.verify(ts, nonce, now)
    print("{:9s} ts={:5d} -> {} {}".format(label, ts, code, reason))
print("重放 n1        ->", guard.verify(1000, "n1", 1050)[1])
print("窗口外遗忘     ->", guard.forget_outside(1050))
print("要点: 时间窗免存储挡过期重放, nonce 兜住窗口内精确重放; 窗口必须不小于两端偏移之和")
