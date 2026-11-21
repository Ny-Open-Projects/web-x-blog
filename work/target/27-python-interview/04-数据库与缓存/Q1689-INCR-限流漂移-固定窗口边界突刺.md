---
title: [Q1689] INCR 限流漂移: 固定窗口边界突刺
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1689 · INCR 限流漂移: 固定窗口边界突刺

> 难度:★★☆☆ | 标签:Redis, 限流

**问**:INCR 加 EXPIRE 实现的限流,为什么压测时总会超放一倍流量?

**答**:这是固定窗口限流的结构性缺陷:计数器按整秒/整分切窗,窗口切换瞬间计数清零。攻击或正常高峰正好压在边界两侧时,前窗口末尾打满 N 次、新窗口开头又放 N 次,两个窗口交界约一个窗口长度内实际放行 2N 次,这就是限流漂移。它不是参数没调好,数学上固定窗口必然存在这个突刺。修正思路:滑动窗口用 zset 存时间戳,统计最近窗口长度内的请求数,精确但内存大;令牌桶以固定速率补桶,容忍突发又限制平均速率,是网关限流的默认选择;保留固定窗口则要把限值乘上保守系数。

```python
# file: code/04_数据库与缓存/q1689_incr_drift.py
"""INCR 限流漂移: 固定窗口在边界处的双倍突刺复现"""

class FakeRedis:
    def __init__(self):
        self.kv = {}

    def incr(self, key):
        self.kv[key] = self.kv.get(key, 0) + 1
        return self.kv[key]

LIMIT = 5
WINDOW = 1.0                                     # 秒

def fixed_window(r, key, now):
    window_id = int(now // WINDOW)               # 窗口按整秒切
    k = f"rate:{key}:{window_id}"
    n = r.incr(k)
    return n <= LIMIT, n

r = FakeRedis()
t0 = 1000.0
print("窗口 1000 末尾连续 5 次:", [fixed_window(r, "u1", t0 + 0.99)[0] for _ in range(LIMIT)])
burst = [fixed_window(r, "u1", t0 + 1.01)[0] for _ in range(LIMIT)]
print("窗口 1001 开头 1ms 内又放行 5 次:", burst)
print("两个窗口交界约 20ms 内实际放行 10 次: 突刺是固定窗口的结构性问题, 不是参数没调好")
print("修法: 滑动窗口 zset 时间戳 或 令牌桶把计数连续化;")
print("      若保留固定窗口, 把 LIMIT 乘上窗口重叠修正系数, 并接受边界突刺")
```

**追问**:
- 滑动窗口 zset 方案的内存怎么算?——每请求一个成员,大流量用户 zset 会膨胀,可以按用户分级:VIP 用滑动,普通用户用固定窗口。
- INCR 后键没有 TTL 会怎样?——计数器永久残留撑爆内存,INCR 之后的 EXPIRE 只在首次设置,或直接用 Lua 把两步原子化。

---
