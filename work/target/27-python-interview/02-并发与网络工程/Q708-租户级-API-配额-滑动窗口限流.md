---
title: [Q708] 租户级 API 配额:滑动窗口限流
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q708 · 租户级 API 配额:滑动窗口限流

> 难度:★★★☆ | 标签:配额, 滑动窗口, 多租户

**问**:SaaS 平台按租户卖 API 配额,限流器怎么设计才能"公平且可解释"?

**答**:按租户 key 维度的滑动窗口计数:每个租户保留窗口内请求时间戳队列(或环形桶),超配额拒绝并返回 reset 时间(距最早一条出窗的时间)——客户端能算出"何时恢复",这是可解释性的关键。对比固定窗口:滑动窗口消除边界突刺(窗口交界瞬间 2 倍通过);多机部署用 Redis ZSET+Lua 原子化。配额设计:套餐配额 + 突发余量(burst)+ 超量策略(拒绝 429 或降级),并暴露 X-RateLimit-Remaining/Reset 头。计费口径与限流口径必须一致,否则对账打架。

```python
# file: code/02_并发与网络工程/q708_tenant_quota.py
import time
from collections import deque


class SlidingWindowQuota:
    def __init__(self, limit: int, window: float = 1.0) -> None:
        self.limit = limit
        self.window = window
        self._hits: dict = {}

    def take(self, tenant: str) -> tuple:
        now = time.monotonic()
        dq = self._hits.setdefault(tenant, deque())
        while dq and dq[0] <= now - self.window:  # 淘汰出窗时间戳
            dq.popleft()
        if len(dq) < self.limit:
            dq.append(now)
            remaining = self.limit - len(dq)
            return True, {"remaining": remaining, "reset_in": 0.0}
        reset_in = self.window - (now - dq[0])  # 最早一条出窗即恢复
        return False, {"remaining": 0, "reset_in": round(reset_in, 2)}


if __name__ == "__main__":
    quotas = {"free": SlidingWindowQuota(limit=3, window=1.0),
              "pro": SlidingWindowQuota(limit=10, window=1.0)}

    print("free 租户连发 5 个请求 (配额 3/min):")
    for i in range(5):
        ok, meta = quotas["free"].take("free")
        status = "200" if ok else "429"
        extra = "" if ok else f" reset_in={meta['reset_in']}s"
        print(f"  req{i}: {status} remaining={meta['remaining']}{extra}")

    print("\npro 租户连发 5 个请求 (配额 10/min):")
    for i in range(5):
        ok, meta = quotas["pro"].take("pro")
        print(f"  req{i}: {'200' if ok else '429'} remaining={meta['remaining']}")

    print("\n等待窗口滑过...")
    time.sleep(1.05)
    ok, meta = quotas["free"].take("free")
    print("free 恢复后:", "200" if ok else "429", "remaining =", meta["remaining"])
    assert ok
    print("要点: 时间戳队列实现真滑动窗口, reset_in 让客户端可预期")
```

**追问**:1) 滑动窗口的内存账怎么算?——每租户每窗口最多 limit 个时间戳(每个约 50 字节),10 万租户 × 1000 配额 = 数 GB,超大规模要换"环形桶"固定内存(O(窗口/桶粒度))或中心化 Redis 方案。2) 滑动窗口与固定窗口怎么取舍?——滑动消除边界突刺(窗口交界瞬间 2 倍通过),代价是内存与计算(时间戳队列/环形桶);固定窗口实现便宜适合粗粒度;折中方案是滑动窗口日志(多桶加权近似)。3) 可解释性怎么落地?——响应头 X-RateLimit-Limit/Remaining/Reset+429 带 Retry-After(=reset 时刻);客户端能算出「何时恢复」而不是盲重试;计费口径与限流口径必须一致,否则对账打架。4) 生产陷阱?——每租户时间戳队列无上限,租户量大时内存爆(换环形桶或 Redis);多机各自计数实际配额×N(中心化 Redis+Lua);429 不带 Reset,客户端同步重试风暴;突发余量没灰度,放开瞬间打挂下游。

---
