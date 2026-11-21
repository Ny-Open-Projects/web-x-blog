---
title: [Q1149] HITL 审批流:暂停-审批-继续
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1149 · HITL 审批流:暂停-审批-继续

> 难度:★★★★ | 标签:HITL, 安全

**问**:Agent 要执行高风险操作(如删库、转账),人机协同审批怎么设计?

**答**:审批流三要素:触发(策略引擎判断哪些操作需要人审,如金额阈值、工具风险等级)、等待(任务置为 PAUSED,生成审批单,含上下文快照与建议动作)、决策(批准/驳回/修改参数,决定写回任务后从断点继续)。工程要点:等待期间不占用模型上下文——把状态落库,由外部事件(审批回调)驱动恢复;审批单要"给人看的完整上下文",缺上下文的审批必然沦为无脑点通过。

```python
# file: code/06_Agent与LLM及系统设计/q1149_hitl_approval.py
"""HITL 审批流:高风险动作暂停生成审批单,审批回调驱动断点继续。"""
import json


class ApprovalFlow:
    def __init__(self, risk_rules):
        self.risk_rules = risk_rules          # 函数: 动作 -> bool 是否需人审
        self.pending = {}                     # approval_id -> 审批单
        self.decisions = {}

    def request(self, task, action, context):
        if not self.risk_rules(action):
            return "auto_approved", None
        aid = f"ap-{len(self.pending) + 1}"
        self.pending[aid] = {
            "task": task, "action": action,
            "context_snapshot": json.dumps(context, ensure_ascii=False),
        }
        task["state"] = "PAUSED"
        return "waiting_approval", aid

    def decide(self, aid, approve, operator):
        assert aid in self.pending, "审批单不存在"
        self.decisions[aid] = {"approve": approve, "operator": operator}
        return self.pending[aid]["task"]


if __name__ == "__main__":
    def risky(action):
        return "转账" in action or "删除" in action

    flow = ApprovalFlow(risky)
    task = {"id": "t-9", "state": "RUNNING", "done_steps": ["query_balance"]}

    # 低风险动作自动放行
    st1, _ = flow.request(task, "查询账单", {"user": "u1"})
    print("低风险:", st1)

    # 高风险动作挂起等审批
    st2, aid = flow.request(task, "转账 50000 元给供应商", {"to": "supplier-7"})
    print("高风险:", st2, "审批单:", aid, "任务状态:", task["state"])
    assert st2 == "waiting_approval" and task["state"] == "PAUSED"

    # 审批人看到完整上下文后批准
    print("审批单上下文:", flow.pending[aid]["context_snapshot"])
    resumed = flow.decide(aid, approve=True, operator="admin-wang")
    resumed["state"] = "RUNNING"
    resumed["done_steps"].append("transfer")
    print("批准后任务恢复:", resumed)
    assert resumed["state"] == "RUNNING"
```

**追问**:
- 审批超时没人管怎么办?答:审批单带 TTL 与升级策略,超时自动驳回并通知升级人,默认拒绝比默认通过安全。
- 高频审批把人淹没了怎么办?答:按风险分层,低风险自动放行 + 抽样人审,并统计人审通过率反过来校准自动放行阈值。
