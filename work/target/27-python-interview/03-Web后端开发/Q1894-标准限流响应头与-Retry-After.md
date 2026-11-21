---
title: [Q1894] 标准限流响应头与 Retry-After
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1894 · 标准限流响应头与 Retry-After

> 难度:★★★☆ | 标签:限流, HTTP 头

**问**:除了返回 429,限流的响应头怎么设计才让客户端能自适应?

**答**:标准化方向是 RateLimit-Limit(窗口额度)、RateLimit-Remaining(剩余)、RateLimit-Reset(重置倒计时),每个正常响应都携带,让客户端在到达上限之前主动降速;429 时再补 Retry-After,明确"何时可以重试"。两者语义必须分开:Remaining 是常态预算,Retry-After 是惩罚期指令,混用会让客户端把限流当故障。Reset 的口径有两种——距重置的秒数或重置时刻的时间戳,团队要统一并写进文档。缺少这些头时客户端只能盲目重试,是重试风暴的常见诱因;由网关层统一注入比每个业务自算更可靠。配额体系还可以区分"限速"与"欠费":限速回 429,配额耗尽回 403 加配额标识,供计费系统分别处理。

```python
# file: code/03_Web后端开发/q1894_ratelimit_headers.py
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
```

**追问**:
- RateLimit 头的字段名为什么还在变?——IETF draft 多轮迭代(RateLimit-* 与 RateLimit-Policy),生产落地常双写兼容。
- Retry-After 用秒数还是日期?——秒数适合短窗口,日期适合长冷却,两者都合法,按窗口时长选。
