---
title: [Q824] 重试语义:退避、Jitter 与重试风暴
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q824 · 重试语义:退避、Jitter 与重试风暴

> 难度:★★★★ | 标签:重试, 稳定性

**问**:下游抖动,客户端重试为什么反而把它打死?正确的重试策略是什么?

**答**:故障时所有客户端**同步周期性重试**,流量被放大数倍,下游彻底失去恢复窗口——重试风暴。正确策略:**指数退避 + jitter**(随机化打散重试时间点)、**重试预算**(如重试流量不超过总请求 10%,超了就熔断停止重试)、**只重试幂等请求**、**尊重 Retry-After**(429/503 给的等待时间必须遵守)。分级:连接失败可快速重试,读超时可重试,写请求绝不盲目重试。

```python
# file: code/03_Web后端开发/q824_retry_budget.py
import random

def retry_call(attempts: list, max_retry: int = 3, budget_ms: float = 100) -> str:
    spent = 0.0
    for i in range(max_retry + 1):
        cost = random.uniform(10, 80)
        spent += cost
        attempts.append(f"try{i}:{cost:.0f}ms")
        if cost < 50:
            return "ok"
        if spent > budget_ms:
            attempts.append("预算耗尽 停止重试")
            break
    return "failed"

res: list = []
print(retry_call(res), res)
```

**追问**:
- jitter 为什么必要?——去掉随机性后所有客户端的重试点重合,形成周期性脉冲,等于没有退避。
- 重试预算谁维护?——客户端侧滑动窗口统计重试占比,超预算期间新失败直接快速失败,保护彼此。
