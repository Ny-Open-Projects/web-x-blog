"""带四重终止条件的 Agent 循环:轮数、token 预算、重复动作检测、最终回答。"""


class LoopyLLM:
    """前两次调用同一工具,第三次给出答案,用于演示重复检测。"""

    def __init__(self):
        self.n = 0

    def step(self, history):
        self.n += 1
        if self.n <= 2:
            return {"tool": "search", "args": {"q": "同一问题"}}
        return {"final": "答案就是 42"}


def run_agent(llm, budget_tokens: int = 100, max_turns: int = 10):
    tokens_used, last_action, repeat = 0, None, 0
    for turn in range(1, max_turns + 1):
        step = llm.step([])
        if "final" in step:
            print(f"[终止] 模型给出最终答案,第 {turn} 轮")
            return step["final"]
        action = (step["tool"], str(sorted(step["args"].items())))
        repeat = repeat + 1 if action == last_action else 0
        last_action = action
        tokens_used += 30  # 模拟每轮消耗
        if repeat >= 2:
            print("[终止] 连续重复动作,判定死循环")
            return None
        if tokens_used > budget_tokens:
            print(f"[终止] 超出预算 {tokens_used}>{budget_tokens},优雅降级")
            return None
    print("[终止] 达到最大轮数")
    return None


if __name__ == "__main__":
    print("结果:", run_agent(LoopyLLM(), budget_tokens=1000))
