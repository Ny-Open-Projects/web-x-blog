---
title: [Q241] 手写一个 Agent 主循环
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q241 · 手写一个 Agent 主循环

> 难度:★★★★★ | 标签:Agent, 核心代码

**问**:不依赖框架,手写一个最小 Agent 循环需要哪几个组件?

**答**:四个组件即可:1) LLM 封装(消息进、回复出,能产生 tool_call);2) 工具注册表;3) 循环体(请求模型 → 解析动作 → 执行工具 → 回填 observation);4) 终止与安全控制(最大轮数、异常兜底)。框架(LangChain/LangGraph)本质是把这个循环产品化,加了状态机、检查点、并发等。面试能手写这 30 行,比背框架 API 更有说服力。

```python
# file: code/06_Agent与LLM及系统设计/q241_agent_loop.py
"""最小 Agent 循环:消息驱动、工具注册、最大轮数保护,全部用 stub。"""
import json


class FakeLoopLLM:
    def __init__(self):
        self.turn = 0

    def chat(self, messages, tools):
        self.turn += 1
        if self.turn == 1:
            return {"type": "tool_call", "name": "add", "args": {"a": 2, "b": 3}}
        tool_result = next(m["content"] for m in messages if m["role"] == "tool")
        return {"type": "final", "content": f"2+3 的结果是 {tool_result}"}


class Agent:
    def __init__(self, llm, tools: dict, max_turns: int = 5):
        self.llm, self.tools, self.max_turns = llm, tools, max_turns

    def run(self, task: str) -> str:
        messages = [{"role": "system", "content": "你是会用工具的助手"},
                    {"role": "user", "content": task}]
        for turn in range(self.max_turns):
            resp = self.llm.chat(messages, tools=list(self.tools))
            if resp["type"] == "final":
                return resp["content"]
            try:
                result = self.tools[resp["name"]](**resp["args"])
            except Exception as exc:  # 工具异常回填给模型自纠
                result = f"工具执行失败: {exc}"
            messages.append({"role": "tool", "content": str(result)})
        return "达到最大轮数,强制终止"


if __name__ == "__main__":
    tools = {"add": lambda a, b: json.dumps(a + b)}
    agent = Agent(FakeLoopLLM(), tools, max_turns=5)
    print(agent.run("帮我算 2 加 3"))
```

**追问**:
- 循环卡死怎么办?靠 max_turns 硬上限 + 单步超时 + 检测重复相同调用来熔断。
- 框架和手写循环怎么取舍?——手写循环适合理解与简单任务;需要状态机、检查点、人工审批节点、并发编排时上 LangGraph 这类框架。
- 单步超时怎么实现?——asyncio.wait_for 包住工具执行与 LLM 调用;超时的工具结果以错误形式回填,让模型决定跳过或换路。
- 熔断后怎么收尾?——带着已完成步骤的摘要返回「部分完成」状态并记录日志,而不是静默丢弃整个任务。
