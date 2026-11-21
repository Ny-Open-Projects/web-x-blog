"""Q2991 人工确认的工作流状态机:守卫+超时升级+拒绝回路。

高危操作(大额退款、批量删除)不能让 Agent 自主执行,必须经过
人工确认状态机:合法迁移用表驱动硬编码,非法迁移一律拒绝;工单
在 pending 停留超时自动升级给上级审批者;拒绝后回 draft 可改材料
重新提交,而不是死在终态。状态机是审计的骨架,每个迁移都留痕。
"""

DRAFT, PENDING, APPROVED, REJECTED, EXECUTING, DONE, ESCALATED = \
    "draft", "pending", "approved", "rejected", "executing", "done", \
    "escalated"

TRANSITIONS = {
    DRAFT:     {PENDING: "submit"},
    PENDING:   {APPROVED: "approve", REJECTED: "reject",
                ESCALATED: "timeout"},
    ESCALATED: {APPROVED: "approve", REJECTED: "reject"},
    REJECTED:  {DRAFT: "revise"},
    APPROVED:  {EXECUTING: "begin"},
    EXECUTING: {DONE: "finish", REJECTED: "abort"},
}


class WorkflowError(Exception):
    pass


class ApprovalFlow:
    def __init__(self, clock, timeout=10.0, on_escalate=None):
        self.state = DRAFT
        self.clock = clock
        self.timeout = timeout
        self.on_escalate = on_escalate or (lambda level: "L%d" % (level + 1))
        self.submitted_at = None
        self.escalation_level = 0
        self.trail = []

    def fire(self, event):
        targets = TRANSITIONS.get(self.state, {})
        target = None
        for t, ev in targets.items():
            if ev == event:
                target = t
                break
        if target is None:
            raise WorkflowError("非法迁移: %s 在状态 %s 下触发 %s"
                                % (event, self.state, event))
        prev = self.state
        self.state = target
        self.trail.append("%s --%s--> %s" % (prev, event, target))
        if target == PENDING:
            self.submitted_at = self.clock()
        if target == ESCALATED:
            self.escalation_level += 1
            self.on_escalate(self.escalation_level)
        return self.state

    def check_timeout(self):
        """pending 停留超过阈值则自动升级,升级后重新计时。"""
        if self.state in (PENDING, ESCALATED) and \
           self.clock() - self.submitted_at > self.timeout:
            self.fire("timeout")

    def execute(self):
        if self.state != APPROVED:
            raise WorkflowError("只有 approved 可以执行")
        self.fire("begin")
        self.fire("finish")


def main():
    now = [0.0]
    escalated = []
    flow = ApprovalFlow(clock=lambda: now[0], timeout=10.0,
                        on_escalate=lambda lv: escalated.append(lv))

    # 非法迁移:draft 不能直接 approve
    try:
        flow.fire("approve")
        raise AssertionError("应当抛非法迁移")
    except WorkflowError as exc:
        assert "非法迁移" in str(exc)

    flow.fire("submit")
    assert flow.state == PENDING
    now[0] = 11.0                       # 超时
    flow.check_timeout()
    assert flow.state == ESCALATED and escalated == [1], flow.state
    flow.fire("approve")                # 上级批准
    flow.execute()
    assert flow.state == DONE
    assert len(flow.trail) == 5, flow.trail

    # 拒绝回路:rejected 回 draft 改材料再提交
    flow2 = ApprovalFlow(clock=lambda: 0.0)
    flow2.fire("submit")
    flow2.fire("reject")
    flow2.fire("revise")
    assert flow2.state == DRAFT
    flow2.fire("submit")
    flow2.fire("approve")
    assert flow2.state == APPROVED

    # 执行中途发现异常可 abort 回 rejected,留完整轨迹
    flow3 = ApprovalFlow(clock=lambda: 0.0)
    flow3.fire("submit")
    flow3.fire("approve")
    flow3.fire("begin")
    flow3.fire("abort")
    assert flow3.state == REJECTED
    print("升级轨迹:", " | ".join(str(x) for x in escalated))
    print("完整迁移链:", " -> ".join(t.split("--")[1] for t in flow.trail))


if __name__ == "__main__":
    main()
