"""Q2984 多 Agent 流水线的完整编排:规划-写作-评审-返工-降级。

编排器维护一份工件在 Agent 间流转:上游写作、下游评审,评审不通过
带着结构化反馈打回上游,返工有上限,超限降级为「带瑕疵放行+留痕」
而不是死循环。关键设计:Agent 之间不直接对话,全部经由编排器传递
结构化消息,这样每一步都可观测、可重放、可加预算。
"""

MAX_REWORK = 1
BLACKLIST_FEATURES = {"导出报表"}     # 模拟无论怎么改都过不了评审的情形


class WriterAgent:
    def __init__(self):
        self.rounds = 0

    def write(self, plan, feedback=None):
        self.rounds += 1
        draft = "实现:" + plan["feature"]
        if feedback:
            draft += "(已修:" + feedback["issue"] + ")"
        return {"draft": draft, "rounds": self.rounds}


class ReviewerAgent:
    def review(self, plan, artifact):
        if plan["feature"] in BLACKLIST_FEATURES:
            return {"verdict": "reject", "issues": ["功能在禁改清单"]}
        if not plan.get("tests"):
            return {"verdict": "reject", "issues": ["缺少测试计划"]}
        return {"verdict": "approve", "issues": []}


class Orchestrator:
    """流水线编排:结构化消息在阶段间流转,返工计数有上限。"""

    def __init__(self, writer, reviewer):
        self.writer = writer
        self.reviewer = reviewer
        self.log = []

    def run(self, plan):
        feedback = None
        rework = 0
        self.log.append("stage:plan:" + plan["feature"])
        while True:
            artifact = self.writer.write(plan, feedback=feedback)
            verdict = self.reviewer.review(plan, artifact)
            self.log.append("stage:review:" + verdict["verdict"])
            if verdict["verdict"] == "approve":
                return artifact, "approved", rework
            rework += 1
            if rework > MAX_REWORK:
                self.log.append("stage:degrade:over_rework_limit")
                return artifact, "degraded", rework
            self.log.append("stage:rework:" + verdict["issues"][0])
            feedback = {"issue": verdict["issues"][0]}
            plan = dict(plan)
            plan["tests"] = ["case_1"]          # 按反馈修补计划再重写


def main():
    orch = Orchestrator(WriterAgent(), ReviewerAgent())
    artifact, status, rework = orch.run({"feature": "搜索联想"})
    assert status == "approved", status                 # 打回一次后通过
    assert rework == 1, rework
    assert artifact["draft"].endswith("(已修:缺少测试计划)")
    assert orch.log[0] == "stage:plan:搜索联想"
    assert "stage:review:reject" in orch.log
    assert "stage:rework:缺少测试计划" in orch.log

    # 无论怎么改都过不了评审:走降级路径而不是死循环
    orch2 = Orchestrator(WriterAgent(), ReviewerAgent())
    _, status2, rework2 = orch2.run({"feature": "导出报表", "tests": []})
    assert status2 == "degraded", status2
    assert rework2 == 2, rework2
    assert "stage:degrade:over_rework_limit" in orch2.log

    # 一次就合格的计划:零返工
    orch3 = Orchestrator(WriterAgent(), ReviewerAgent())
    _, status3, rework3 = orch3.run({"feature": "健康检查", "tests": ["c1"]})
    assert status3 == "approved" and rework3 == 0
    print("流水线状态:", status, "| 返工:", rework)
    print("编排轨迹:", " -> ".join(orch.log))
    print("降级轨迹:", " -> ".join(orch2.log))


if __name__ == "__main__":
    main()
