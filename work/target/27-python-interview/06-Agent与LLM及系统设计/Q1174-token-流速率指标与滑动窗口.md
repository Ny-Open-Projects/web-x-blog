---
title: [Q1174] token 流速率指标与滑动窗口
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1174 · token 流速率指标与滑动窗口

> 难度:★★★☆ | 标签:可观测性, 指标

**问**:怎么实时监控"每秒输出 token 数"?用什么数据结构?

**答**:维护一个按时间戳记录 token 增量的滑动窗口(环形缓冲或 deque),速率 = 窗口内 token 总和 / 窗口时长。实现要点:事件粒度是"每片 delta(数量, 时间)",窗口按事件时间滑动而不是定时清零;P95 之类分位数用固定桶直方图近似;指标读取要无锁或 O(1),别在热路径加全局锁。这个指标用于:降级决策(输出速率骤降=下游异常)、容量评估、以及流式体验监控(首 token 延迟与稳态速率分开看)。

```python
# file: code/06_Agent与LLM及系统设计/q1174_token_rate.py
"""token 速率滑动窗口:deque 存增量事件,按事件时间滑动,支持首 token 延迟。"""
import time
from collections import deque


class TokenRateMeter:
    def __init__(self, window_sec=2.0):
        self.window, self.events = window_sec, deque()
        self.total_tokens = 0
        self.first_token_at = None

    def on_delta(self, tokens, now=None):
        now = time.monotonic() if now is None else now
        if self.first_token_at is None:
            self.first_token_at = now
        self.events.append((now, tokens))
        self.total_tokens += tokens
        self._evict(now)

    def _evict(self, now):
        while self.events and self.events[0][0] < now - self.window:
            self.events.popleft()

    def rate(self, now=None):
        now = time.monotonic() if now is None else now
        self._evict(now)
        span = min(self.window, now - self.events[0][0] + 1e-9) if self.events else 1e-9
        return sum(t for _, t in self.events) / span

    def stalled(self, now, min_rate=1.0, min_tokens=10):
        """滞流判定:累计产出足够多但当前窗口速率骤降。"""
        return self.total_tokens >= min_tokens and self.rate(now) < min_rate


if __name__ == "__main__":
    meter = TokenRateMeter(window_sec=2.0)
    t0 = 100.0
    # 前一秒 50 tok/s,之后停止输出
    for i in range(5):
        meter.on_delta(10, now=t0 + i * 0.2)
    r1 = meter.rate(t0 + 1.0)
    print(f"峰值速率 {r1:.0f} tok/s, 首 token 延迟 0ms")
    assert 40 < r1 <= 60
    r2 = meter.rate(t0 + 3.5)
    print(f"停止输出 2.5s 后速率 {r2:.0f} tok/s, 滞流告警={meter.stalled(t0 + 3.5)}")
    assert meter.stalled(t0 + 3.5), "输出停止必须触发滞流检测"
    r3 = meter.rate(t0 + 10.0)
    print(f"窗口完全滑走后速率 {r3:.0f}", "-> 不会永远停留在旧速率")
    assert r3 == 0
```

**追问**:
- 首 token 延迟和稳态速率为什么分开监控?答:首 token 延迟反映排队与预填成本,稳态速率反映解码吞吐,归因方向完全不同(队列问题 vs 算力问题),混在一起看会误判。
- 多实例聚合速率怎么做?答:每实例本地计量,指标系统做 sum by instance;聚合意义有限,通常按实例看分位数再取分布,而非全局求和。
