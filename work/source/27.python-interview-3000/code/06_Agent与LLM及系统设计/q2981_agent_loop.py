"""Q2981 Agent 主循环的最小完整实现:计划-执行-观察-终止。

主循环四拍:LLM 按当前轨迹产出下一个动作(调工具或给最终答案),
执行器跑工具并把结果裁剪成观察写回轨迹,循环直到出现终止条件。
终止有三条路:模型主动给最终答案、步数预算耗尽、检测到同参数
重复调用(打转保护)。LLM 用脚本桩,行为确定、可断言。
"""

FAKE_PLAN = [
    {"tool": "search", "args": {"q": "退款政策"}},
    {"tool": "search", "args": {"q": "退款时效"}},   # 换个问法继续检索
    {"tool": "lookup_order", "args": {"order_id": "o_9"}},
    {"final": "订单 o_9 已在 7 天无理由期内,可以退款。"},
]

TOOLS_DOCS = {
    "search": "检索知识库,返回相关条款",
    "lookup_order": "按订单号查订单状态",
}


class FakeLLM:
    """脚本桩:按轨迹长度吐出下一步动作,模拟规划-执行-观察。"""

    def __init__(self, script):
        self.script = script

    def next_action(self, trajectory):
        idx = len([t for t in trajectory if t["role"] == "action"])
        if idx >= len(self.script):
            return {"final": "预算内未收敛,给出兜底答复。"}
        return self.script[idx]


class AgentLoop:
    def __init__(self, llm, tools, max_steps=6):
        self.llm = llm
        self.tools = tools
        self.max_steps = max_steps

    def run(self, question):
        trajectory = [{"role": "user", "content": question}]
        seen_calls = []
        for step in range(self.max_steps):
            action = self.llm.next_action(trajectory)
            if "final" in action:
                trajectory.append({"role": "final", "content": action["final"]})
                return trajectory, "final", step + 1
            tool = action["tool"]
            call_sig = tool + ":" + str(sorted(action["args"].items()))
            if call_sig in seen_calls:
                trajectory.append({"role": "final",
                                   "content": "检测到重复调用,提前终止。"})
                return trajectory, "loop_guard", step + 1
            seen_calls.append(call_sig)
            if tool not in self.tools:
                obs = "错误:未知工具 " + tool
            else:
                try:
                    obs = str(self.tools[tool](**action["args"]))
                except Exception as exc:            # 工具失败转为观察而非崩溃
                    obs = "错误:" + type(exc).__name__
            obs = obs[:80]                          # 观察裁剪,防轨迹爆炸
            trajectory.append({"role": "action", "content": call_sig})
            trajectory.append({"role": "observation", "content": obs})
        trajectory.append({"role": "final", "content": "步数预算耗尽。"})
        return trajectory, "budget", self.max_steps


def main():
    tools = {
        "search": lambda q: "条款:签收后 7 天内可无理由退款。",
        "lookup_order": lambda order_id: "订单 o_9 状态:已签收 3 天。",
    }
    traj, why, steps = AgentLoop(FakeLLM(FAKE_PLAN), tools).run("o_9 能退款吗")
    assert why == "final", why
    assert traj[-1]["content"].startswith("订单 o_9"), traj[-1]
    assert steps == 4, steps

    # 打转保护:模型反复要求同一个调用
    loop_script = [{"tool": "search", "args": {"q": "x"}}] * 10
    traj2, why2, _ = AgentLoop(FakeLLM(loop_script), tools, max_steps=8).run("q")
    assert why2 == "loop_guard", why2

    # 预算耗尽:工具一直失败也不崩溃(每次参数不同,不触发打转保护)
    def boom(n=0):
        raise ValueError("down")
    script3 = [{"tool": "boom", "args": {"n": i}} for i in range(20)]
    traj3, why3, steps3 = AgentLoop(
        FakeLLM(script3), {"boom": boom}, max_steps=3).run("q")
    assert why3 == "budget", why3
    assert steps3 == 3
    print("终止原因:", why, "| 步数:", steps)
    print("打转保护与预算终止均生效,轨迹长度:", len(traj3))


if __name__ == "__main__":
    main()
