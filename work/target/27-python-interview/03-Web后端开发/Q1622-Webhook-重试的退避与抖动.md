---
title: [Q1622] Webhook 重试的退避与抖动
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1622 · Webhook 重试的退避与抖动

> 难度:★★★☆ | 标签:Webhook, 可靠性

**问**:Webhook 投递失败后的重试策略怎么设计?为什么重试要加抖动?

**答**:三要素:指数退避、封顶上限、全抖动。每次延迟取 min(cap, base 乘 2 的 n-1 次方),再在其区间内随机取值,把重试在时间轴上摊开——否则对端恢复的瞬间会被所有积压重试同时打爆,这就是重试风暴。对端返回 429 或 503 并带 `Retry-After` 时,它表达了明确的恢复意图,优先级高于自己的退避公式。重试要有次数上限(常见 5-8 次),耗尽后进入死信,不能无限重试占用投递线程。同时投递要带投递 ID 让接收方幂等,因为网络超时时你并不知道对端是否已处理。

```python
# file: code/03_Web后端开发/q1622_webhook_retry.py
"""Webhook 投递重试: 指数退避 + 全抖动 + Retry-After 优先(纯标准库)。"""
import random

random.seed(7)                                   # 固定种子让演示可复现


def next_delay(attempt, retry_after=None, base=1.0, cap=60.0):
    if retry_after is not None:
        return float(retry_after)                # 对端明确指示就听对端的
    ceiling = min(cap, base * 2 ** (attempt - 1))
    return random.uniform(0, ceiling)            # full jitter 把重试打散


def deliver_schedule(statuses):
    """statuses: 每次投递的模拟状态码, None 表示成功。"""
    timeline, t = [], 0.0
    for attempt, status in enumerate(statuses, 1):
        timeline.append((attempt, round(t, 1), status if status else 200))
        if status is None:
            break
        retry_after = 30 if status == 429 else None
        t += next_delay(attempt, retry_after)
    return timeline


statuses = [503, 429, 500, None]
for attempt, at, status in deliver_schedule(statuses):
    print(f"第 {attempt} 次  t={at:>5}s  -> {status}")
print("要点: 退避防打爆对端, 抖动防同一时刻重放, Retry-After 是对端明确意图, 优先级最高")
```

**追问**:
- 抖动用 full 还是 equal?——full jitter,首个重试最密集时也被打散,实测冲突率最低。
- 超时算成功还是失败?——未知,按失败重试,靠接收方幂等键去重,而不是猜。
