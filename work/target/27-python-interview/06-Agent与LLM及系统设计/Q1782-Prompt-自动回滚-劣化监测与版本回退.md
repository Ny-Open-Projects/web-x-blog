---
title: [Q1782] Prompt 自动回滚:劣化监测与版本回退
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1782 · Prompt 自动回滚:劣化监测与版本回退

> 难度:★★★☆ | 标签:LLM 运维, 回滚, 监控

**问**:灰度放量后线上效果开始变差,靠人盯告警太慢,怎么自动兜底?

**答**:自动回滚器按窗口观察灰度版质量:单窗低于基线容差只记观察,连续 k 个窗口都低才触发回滚,防抖设计让偶发坏窗不会误杀好版本;任何一个健康窗口都把连坏计数清零,趋势性劣化才积累到阈值。触发后立即把流量切回基线版本并落回滚事件,此后即使再收到坏窗数据也不再响应,直到人工重新放量,避免回滚器自己来回振荡。回滚指标要和灰度指标同一口径,否则回滚器对着错误的尺子做决策。

```python
# file: code/06_Agent与LLM及系统设计/q1782_auto_rollback.py
"""Prompt 自动回滚:滑窗质量连续 k 窗低于基线容差,自动切回基线并防抖。"""


class AutoRollback:
    def __init__(self, baseline_score=0.90, drop=0.05, windows=3):
        self.baseline = baseline_score
        self.drop = drop
        self.need = windows
        self.bad_streak = 0
        self.active = "candidate"
        self.actions = []

    def observe(self, window_score):
        if self.active != "candidate":
            return "already_rolled_back"         # 回滚后不再振荡
        if window_score < self.baseline - self.drop:
            self.bad_streak += 1
            if self.bad_streak >= self.need:
                self.active = "baseline"
                self.actions.append("rollback")
                return "rolled_back"
            return "watching"
        self.bad_streak = 0                      # 健康窗清零,防偶发抖动误杀
        return "healthy"


if __name__ == "__main__":
    rb = AutoRollback(baseline_score=0.90, drop=0.05, windows=3)
    assert rb.observe(0.92) == "healthy"
    assert rb.observe(0.80) == "watching", "低 1 窗:观察"
    assert rb.observe(0.93) == "healthy", "好窗清零"
    seq = [rb.observe(s) for s in (0.83, 0.84, 0.82)]
    assert seq == ["watching", "watching", "rolled_back"], "连续 3 低窗触发回滚"
    assert rb.active == "baseline" and rb.actions == ["rollback"]
    assert rb.observe(0.50) == "already_rolled_back", "回滚后流量守在基线"
    print("自动回滚通过:连续 3 窗劣化才回滚,单窗好转清零防抖,回滚后守稳")
```

**追问**:
- k 取多少? 答:k 越大越稳但响应越慢,通常 2 到 3 个窗,窗口长度取小时级,让回滚在小时级完成而不是天级。
- 回滚要通知谁? 答:回滚事件进告警与值班群,附最后 k 窗指标明细,自动兜底加人工复盘双轨。
