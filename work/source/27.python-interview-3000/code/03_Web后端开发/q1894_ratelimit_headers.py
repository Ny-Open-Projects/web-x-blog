"""限流响应头: RateLimit-Limit/Remaining/Reset 与 Retry-After 的语义(纯标准库)。"""


class FixedWindow:
    """按调用时刻动态给出标准限流头; 窗口重置点取整到分钟边界。"""

    def __init__(self, limit, window_seconds=60):
        self.limit = limit
        self.window = window_seconds
        self.count = 0
        self.reset_at = 0

    def _roll(self, now):
        if now >= self.reset_at:
            self.reset_at = now + self.window
            self.count = 0

    def take(self, n, now):
        """尝试消费 n 个配额, 返回 (allowed, headers)。"""
        self._roll(now)
        if self.count + n > self.limit:
            reset_in = max(1, self.reset_at - now)
            headers = {
                "RateLimit-Limit": str(self.limit),
                "RateLimit-Remaining": str(max(0, self.limit - self.count)),
                "RateLimit-Reset": str(reset_in),
                "Retry-After": str(reset_in),          # 429 专用: 何时可重试
            }
            return False, headers
        self.count += n
        headers = {
            "RateLimit-Limit": str(self.limit),
            "RateLimit-Remaining": str(self.limit - self.count),
            "RateLimit-Reset": str(max(1, self.reset_at - now)),
        }
        return True, headers


window = FixedWindow(limit=5, window_seconds=60)
now = 1000
for i in range(4):
    ok, h = window.take(1, now)
    print("第{}次请求 -> allowed {} Remaining={} Reset={}".format(
        i + 1, ok, h["RateLimit-Remaining"], h["RateLimit-Reset"]))
    assert ok

ok, h = window.take(2, now)          # 剩 1 个, 一次要 2 个 -> 拒绝
print("超限请求 -> allowed {} 状态码 429 Retry-After={}".format(ok, h["Retry-After"]))
assert not ok and h["Retry-After"] == "60"

ok, h = window.take(1, now)          # 剩余刚好够
print("最后一次 -> allowed {} Remaining={}".format(ok, h["RateLimit-Remaining"]))
assert ok

# 窗口翻滚后自动恢复
ok, h = window.take(1, now + 61)
print("窗口翻滚后 -> allowed {} Remaining={}".format(ok, h["RateLimit-Remaining"]))
assert ok

print("要点: 正常响应暴露 Remaining 让客户端自适应降速, 429 才带 Retry-After, 两者语义不可混用")
