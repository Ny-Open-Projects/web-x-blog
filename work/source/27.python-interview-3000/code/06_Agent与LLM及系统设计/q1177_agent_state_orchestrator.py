"""Agent 编排状态机:转换表 + 纯转换处理函数 + 上下文版本控制。"""


TRANSITIONS = {
    "PLAN": {"EXECUTE", "FAILED"},
    "EXECUTE": {"REVIEW", "RETRY", "FAILED"},
    "RETRY": {"EXECUTE", "FAILED"},
    "REVIEW": {"DONE", "EXECUTE"},      # 审查不过退回执行
    "FAILED": {"PLAN"},                 # 允许重新规划
    "DONE": set(),
}


class Orchestrator:
    def __init__(self, handlers, max_transitions=20):
        self.handlers, self.max_transitions = handlers, max_transitions
        self.audit = []

    def run(self, ctx, state="PLAN"):
        steps = 0
        while state != "DONE" and steps < self.max_transitions:
            steps += 1
            handler = self.handlers[state]
            state, patch = handler(ctx)
            ctx.update(patch)
            self.audit.append({"step": steps, "to": state, "retries": ctx.get("retries", 0)})
        return state, ctx


if __name__ == "__main__":
    def h_plan(ctx):
        ctx["plan"] = ["查数据", "写结论"]
        return "EXECUTE", {"plan": ctx["plan"]}

    def h_execute(ctx):
        i = ctx.get("cursor", 0)
        if i < len(ctx["plan"]):
            task = ctx["plan"][i]
            # 首次写结论产出残缺结果,触发审查退回
            out = "略" if (task == "写结论" and ctx.get("retries", 0) == 0) else f"{task} 完成"
            return "EXECUTE", {"cursor": i + 1, f"out_{i}": out}
        return "REVIEW", {}

    def h_review(ctx):
        if "结论" not in str(ctx.get("out_1", "")):
            ctx["retries"] = ctx.get("retries", 0) + 1
            if ctx["retries"] <= 1:
                return "EXECUTE", {"cursor": 1, "review_note": "结论缺失,重写"}
            return "FAILED", {}
        return "DONE", {}

    handlers = {"PLAN": h_plan, "EXECUTE": h_execute, "RETRY": h_execute, "REVIEW": h_review}
    orch = Orchestrator(handlers)
    final, ctx = orch.run({"plan": [], "cursor": 0, "retries": 0})
    print("最终状态:", final)
    print("审计轨迹:", [(a["step"], a["to"]) for a in orch.audit])
    assert final == "DONE"
    assert any(a["to"] == "EXECUTE" for a in orch.audit[3:5]), "审查退回重试路径已触发"
    assert "写结论 完成" in ctx["out_1"], "重写后结论补全"
    print("状态机编排完成,重试路径与审计齐全")
