---
title: [Q2050] 流式首 token 时延监控:TTFT 分位与 SLO
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2050 · 流式首 token 时延监控:TTFT 分位与 SLO

> 难度:★★★☆ | 标签:LLM运维, 时延, 监控

**问**:用户抱怨等好久才蹦出第一个字,这个指标叫什么,怎么系统化监控?

**答**:叫 TTFT,首 token 时延,流式体验的第一指标。做法是每次流式请求记录发出请求到首个内容 token 的毫秒数,样本进滑动窗口,算 p50 与 p95,对 p95 设 SLO 门限,破线即告警。为什么盯 p95 不盯均值:均值被海量快请求稀释,长尾用户早已流失。滑动窗口的第二个价值是自动恢复:长尾样本滚出窗口后 p95 回落,告警自然解除,不用人工清零。演示里两成长尾样本把 p95 拖破 800 毫秒线,快样本滚满窗口后恢复,破线计数如实累加。

```python
# file: code/06_Agent与LLM及系统设计/q2050_ttft_monitor.py
"""流式首 token 时延监控:TTFT 样本进滑动窗口,算分位数,超 SLO 告警与恢复。"""
from collections import deque


class TTFTMonitor:
    def __init__(self, window=100, slo_ms=800):
        self.samples = deque(maxlen=window)
        self.slo = slo_ms
        self.breaches = 0

    def record(self, ms):
        self.samples.append(ms)

    def percentile(self, p):
        if not self.samples:
            return None
        xs = sorted(self.samples)
        k = max(0, min(len(xs) - 1, int(round(p / 100.0 * len(xs))) - 1))
        return xs[k]

    def status(self):
        p50, p95 = self.percentile(50), self.percentile(95)
        breach = p95 is not None and p95 > self.slo
        if breach:
            self.breaches += 1
        return {"p50": p50, "p95": p95, "slo_ms": self.slo, "slo_breach": breach}


if __name__ == "__main__":
    m = TTFTMonitor(window=20, slo_ms=800)
    for _ in range(16):
        m.record(120)
    m.record(2000)
    m.record(2500)
    m.record(3000)
    m.record(1800)
    s1 = m.status()
    assert s1["p50"] == 120 and s1["p95"] > s1["slo_ms"], s1
    assert s1["slo_breach"] is True, "两成长尾就把 p95 拖破线"

    # 滑动窗口滚走长尾后恢复:窗口容量 20,再灌 20 条快样本
    for _ in range(20):
        m.record(150)
    s2 = m.status()
    assert s2["p95"] <= s2["slo_ms"] and s2["slo_breach"] is False, s2
    assert m.breaches == 1, "只发生过一次破线,status 调用不重复累计"

    empty = TTFTMonitor()
    assert empty.status() == {"p50": None, "p95": None, "slo_ms": 800,
                              "slo_breach": False}, "无样本不告警也不误报"
    print("TTFT 监控通过:p50 不动 p95 破线,长尾滚出窗口后自动恢复")
```

**追问**:
- 窗口多大合适? 答:按请求速率定,覆盖最近几分钟即可,太大对劣化不敏感,太小抖动
- TTFT 和端到端时延什么关系? 答:TTFT 管体感起点,端到端管总时长,两者分位都要看,劣化原因常不同
