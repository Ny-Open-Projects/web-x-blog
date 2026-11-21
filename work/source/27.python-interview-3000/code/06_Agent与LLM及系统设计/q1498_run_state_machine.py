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
