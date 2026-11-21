---
title: [Q1498] Agent 运行状态机:守卫条件拒绝非法转移
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1498 · Agent 运行状态机:守卫条件拒绝非法转移

> 难度:★★★☆ | 标签:Agent, 状态机, 架构

**问**:把 Agent 主循环写成状态机,比 while True 加一堆 if 好在哪?

**答**:好在三件事。非法转移被结构性拒绝:idle 直接跳 done、没做计划就想执行,这类半途跳步在转移表里根本不存在,走到就抛异常,而不是靠每个开发者都记得写检查。守卫条件显式化:plan_ready 才能进 acting,budget_ok 才能从 finishing 回 planning,预算耗尽想重规划被守卫拦下,业务规则从散落的 if 集中到一处可测试的表。历史轨迹可审计:状态序列就是一次运行的骨架画像,配合步骤埋点能精确回答在哪一步坏掉。失败态从任意状态可达,保证任何异常都有出口,不会卡在中间态。

```python
# file: code/06_Agent与LLM及系统设计/q1498_run_state_machine.py
"""Agent 运行状态机:显式状态与守卫条件,非法转移直接拒绝,杜绝半途跳步。"""


class IllegalTransition(Exception):
    pass


class RunStateMachine:
    """运行时状态机:状态转移必须声明过守卫;守卫不满足抛 IllegalTransition。"""

    TRANSITIONS = {
        ("idle", "planning"): lambda s: s["goal"] is not None,
        ("planning", "acting"): lambda s: s["plan_ready"] is True,
        ("acting", "observing"): lambda s: s["tool_pending"] is True,
        ("observing", "acting"): lambda s: s["needs_more"] is True,
        ("observing", "planning"): lambda s: s["needs_replan"] is True,
        ("acting", "finishing"): lambda s: s["tool_pending"] is False and s["budget_ok"] is True,
        ("finishing", "done"): lambda s: s["answer_ok"] is True,
        ("finishing", "planning"): lambda s: s["answer_ok"] is False and s["budget_ok"] is True,
        ("*", "failed"): lambda s: True,            # 任何状态都可进入失败
    }

    def __init__(self, goal=None):
        self.state = "idle"
        self.ctx = {"goal": goal, "plan_ready": False, "tool_pending": False,
                    "needs_more": False, "needs_replan": False,
                    "budget_ok": True, "answer_ok": False}
        self.history = [self.state]

    def transition(self, to):
        key1, key2 = (self.state, to), ("*", to)
        guard = self.TRANSITIONS.get(key1) or self.TRANSITIONS.get(key2)
        if guard is None:
            raise IllegalTransition(f"未声明转移 {self.state} -> {to}")
        if not guard(self.ctx):
            raise IllegalTransition(f"守卫不满足 {self.state} -> {to}")
        self.state = to
        self.history.append(to)
        return self.state

    def set(self, **kw):
        self.ctx.update(kw)


if __name__ == "__main__":
    sm = RunStateMachine(goal="订机票")
    assert sm.transition("planning") == "planning"

    jumped = None
    try:
        sm.transition("done")                  # 计划都没做就想完成 非法
    except IllegalTransition as e:
        jumped = str(e)
    assert jumped is not None and "未声明" in jumped

    sm.set(plan_ready=True)
    assert sm.transition("acting") == "acting"
    sm.set(tool_pending=True)
    assert sm.transition("observing") == "observing"
    sm.set(needs_more=True)
    assert sm.transition("acting") == "acting"           # 观察后继续行动

    sm.set(tool_pending=False, budget_ok=True)
    assert sm.transition("finishing") == "finishing"
    sm.set(answer_ok=False)
    sm.set(budget_ok=False)                              # 预算耗尽还想 replan
    rejected = None
    try:
        sm.transition("planning")
    except IllegalTransition as e:
        rejected = str(e)
    assert rejected is not None and "守卫不满足" in rejected

    sm2 = RunStateMachine(goal="x")
    sm2.set(plan_ready=True)
    sm2.transition("planning")
    sm2.transition("acting")
    sm2.transition("failed")                             # 任何状态可进 failed
    assert sm2.history == ["idle", "planning", "acting", "failed"]
    print("状态机通过:合法链 idle→planning→acting→observing→acting→finishing 非法跳步与守卫均被拒")
```

**追问**:
- 状态会不会爆炸? 答:运行时状态机只要 7 个左右状态,复杂的是任务级状态机,分层各管各的就不会爆炸;
- 守卫失败是异常还是转移失败态? 答:建议抛异常并记录,让上层区分 编程错误 与 合法等待。
