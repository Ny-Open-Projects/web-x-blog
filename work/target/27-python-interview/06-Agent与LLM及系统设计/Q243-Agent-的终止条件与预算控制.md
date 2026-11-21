---
title: [Q243] Agent 的终止条件与预算控制
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q243 · Agent 的终止条件与预算控制

> 难度:★★★ | 标签:Agent, 可靠性

**问**:Agent 怎么停?不设终止条件会发生什么?

**答**:终止条件至少四重:1) 模型显式输出 final answer;2) 最大迭代轮数(硬上限);3) token/成本预算(累计消耗超限即停);4) 步骤超时或连续重复动作检测(如连续两次相同 tool_call 视为循环)。不设终止最典型的故障是"工具调用死循环"——模型反复查同一个东西,烧钱又不出结果。工程上还应支持"优雅降级":超预算时带着已有中间结果返回,而非直接报错。

```python
# file: code/06_Agent与LLM及系统设计/q243_budget_control.py
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
```

**追问**:
- 超预算时怎么优雅降级?——带着已完成的中间结果返回并说明「未完成部分」,而不是抛错;用户可拿到部分价值。
- 成本预算按什么粒度?——单任务上限 + 用户/租户日配额双层;只有单任务上限会被恶意循环刷爆总账。
- 重复动作检测怎么实现?——对 (tool, params_hash) 记录最近调用,连续 N 次相同即熔断;参数完全一样的调用结果几乎不会变。
