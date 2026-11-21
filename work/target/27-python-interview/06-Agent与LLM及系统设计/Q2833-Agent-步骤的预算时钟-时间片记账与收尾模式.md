---
title: [Q2833] Agent 步骤的预算时钟:时间片记账与收尾模式
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2833 · Agent 步骤的预算时钟:时间片记账与收尾模式

> 难度:★★★☆ | 标签:Agent, 预算, 运行时

**问**:Agent 跑到一半预算快用完了,通常怎么处理?比被墙钟硬杀更好的办法是什么?

**答**:多数实现是给整个 run 设个总超时,到点直接 kill,结果是一堆悬挂状态和说不清的半成品。更好的做法是预算时钟:每步开始时按预估领时间片、结束时按实际耗时扣账,实际超过预估的步骤记为超支;剩余预算跌破水位线后运行进入收尾模式,后续步骤自动换便宜路径——检索不重排、生成不展开,把最后一点预算花在产出可用结果上。超支记录是治理数据:哪个步骤总是超预估,下次规划就该按它的真实分布定片。这样预算耗尽是「体面收场」,而不是中途猝死。

```python
# file: code/06_Agent与LLM及系统设计/q2833_budget_clock.py
"""Q2833 Agent 步骤的预算时钟:时间片记账与收尾模式。

给整次运行一个时间预算,每步按预估领时间片、按实际耗时扣账;实际
超过预估的步骤记超支,剩余预算跌破水位线后运行进入收尾模式,后续
步骤自动换便宜路径,而不是被墙钟硬杀在半路留下一堆悬挂状态。
"""

WRAPUP_RATIO = 0.3


class BudgetClock:
    def __init__(self, total_ms):
        self.total = total_ms
        self.remaining = total_ms
        self.overruns = []
        self.mode = "normal"

    def charge(self, name, est_ms, actual_ms):
        """记账一步:先看模式,再按实际扣账,返回本步可用片。"""
        if self.mode == "normal" and self.remaining < self.total * WRAPUP_RATIO:
            self.mode = "wrap_up"
        self.remaining = max(0, self.remaining - actual_ms)
        if actual_ms > est_ms:
            self.overruns.append(name)
        return min(est_ms, self.remaining + actual_ms)


def pick_step_variant(clock, name):
    """收尾模式下选便宜路径:检索不重排、生成不展开。"""
    if clock.mode == "wrap_up":
        return name + ":lite"
    return name + ":full"


def main():
    clock = BudgetClock(1000)
    plan = [
        ("search", 150, 250),   # 超支
        ("read", 200, 300),     # 超支
        ("plan", 200, 200),
        ("draft", 300, 300),
    ]
    chosen = []
    for name, est, actual in plan:
        clock.charge(name, est, actual)
        chosen.append(pick_step_variant(clock, name))
    assert clock.overruns == ["search", "read"], clock.overruns
    assert chosen == ["search:full", "read:full", "plan:full", "draft:lite"], chosen
    assert clock.mode == "wrap_up", clock.mode
    assert clock.remaining == 0, clock.remaining
    print("各步实际选择:", chosen)
    print("超支步骤:", clock.overruns)
    print("最终模式:", clock.mode, "剩余预算:", clock.remaining)
    print("效果:预算快耗尽时自动转收尾,而不是中途被硬杀")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:时间片预估从哪来? 答:冷启动用配置给的保守值,运行后用同类步骤的滑动均值校准,预估本身也要跟着数据走。
- 追问二:收尾模式还超预算怎么办? 答:水位线要预留收尾路径的耗时,收尾步骤只允许 fail-fast,超了就输出已完成的 部分 plus 说明。
