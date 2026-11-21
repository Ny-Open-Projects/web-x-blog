---
title: [Q240] ReAct 模式是什么
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q240 · ReAct 模式是什么

> 难度:★★★★ | 标签:Agent, ReAct

**问**:解释 ReAct 模式,它为什么比一次性回答效果更好?

**答**:ReAct = Reasoning + Acting,模型交替输出 Thought(推理当前缺什么)、Action(调用哪个工具)、Observation(工具结果),循环直到 Thought 判断信息足够再输出 Final Answer。优势:1) 复杂问题分解为多步,每步基于真实观察修正方向,减少幻觉;2) 推理轨迹天然可解释、可审计;3) 遇到工具报错能在下一轮自纠。代价是更多轮调用、更高延迟与成本,简单问题不值得用。

```python
# file: code/06_Agent与LLM及系统设计/q240_react.py
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
```

**追问**:
- ReAct 的 Observation 要截断吗?——要,大结果只回填关键字段或摘要,否则几轮就把上下文撑爆;完整结果存 artifact 传引用。
- ReAct 为什么能减少幻觉?——每步基于工具真实返回修正,而不是一次性靠参数记忆作答;证据链也便于事后审计。
- 什么时候不该用 ReAct?——单步可解的问题(一次检索/一次计算),多轮循环只会烧 token 加延迟;先分类路由再决定循环。
