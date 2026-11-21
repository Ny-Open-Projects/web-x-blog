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
