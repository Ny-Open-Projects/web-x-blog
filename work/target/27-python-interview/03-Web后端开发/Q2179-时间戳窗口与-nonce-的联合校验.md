---
title: [Q2179] 时间戳窗口与 nonce 的联合校验
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2179 · 时间戳窗口与 nonce 的联合校验

> 难度:★★★☆ | 标签:安全, 防重放

**问**:签名里同时带时间戳和 nonce,两个条件怎么联合校验?时钟偏移怎么容忍?

**答**:联合校验的次序是先时间后 nonce:先检查 |now - ts| 不超过容忍偏移(两端各 90 秒是常见取值),超窗直接拒绝——这一步不用存储,挡掉绝大多数过期重放;再查 nonce 窗口,精确拦截窗口内的重放。关键关系是 nonce 保留窗口必须覆盖两端偏移,即窗口 ≥ 2 倍偏移:窗口小于偏移时,一个偏移边界外的请求被时间窗拒绝后,其 nonce 已被清理,攻击者等到时间窗边缘重放就能绕过。响应要区分两种拒绝:时间超窗返回带服务器时间的 401 提示校时,nonce 重复返回明确的 replayed 错误,调用方才能自查而不是盲目重试。

```python
# file: code/03_Web后端开发/q2179_timestamp_nonce.py
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
```

**追问**:
- 客户端时钟不可控怎么办?——用服务器下发的时间偏移校准,或首次交互返回 401 带服务器时间让客户端自适应。
- 为什么不全靠 nonce 去掉时间戳?——纯 nonce 需要永久存储防超窗重放,时间窗把存储需求压缩到窗口长度,两者是成本互补。
