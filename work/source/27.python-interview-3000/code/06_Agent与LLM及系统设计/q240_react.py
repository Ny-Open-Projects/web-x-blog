"""用 FakeLLM 演示标准 ReAct 循环:Thought / Action / Observation / Final。"""


class FakeReActLLM:
    """按脚本返回 ReAct 步骤,模拟真实模型的多轮推理。"""

    def __init__(self):
        self.steps = [
            ("thought", "我需要先查北京到上海的距离"),
            ("action", {"tool": "query_distance", "args": {"from": "北京", "to": "上海"}}),
            ("thought", "距离约1200公里,高铁350km/h,可以算时间了"),
            ("action", {"tool": "calc", "args": {"expr": "1200/350"}}),
            ("thought", "约3.4小时,信息足够了"),
            ("finish", "北京到上海高铁约需 3.4 小时"),
        ]
        self.i = 0

    def next_step(self, messages):
        step = self.steps[self.i]
        self.i += 1
        return step


TOOLS = {
    "query_distance": lambda **kw: "约1200公里",
    "calc": lambda expr: str(round(eval(expr), 2)),
}


def react_loop(llm, question: str, max_steps: int = 10):
    history = [f"Question: {question}"]
    for _ in range(max_steps):
        kind, payload = llm.next_step(history)
        if kind == "thought":
            history.append(f"Thought: {payload}")
        elif kind == "action":
            obs = TOOLS[payload["tool"]](**payload["args"])
            history.append(f"Action: {payload}\nObservation: {obs}")
            print(f"  调用 {payload['tool']} -> {obs}")
        elif kind == "finish":
            return payload, history
    return "超过最大步数", history


if __name__ == "__main__":
    answer, trace = react_loop(FakeReActLLM(), "北京到上海高铁要多久?")
    print("Final Answer:", answer)
    print("轨迹步数:", len(trace))
