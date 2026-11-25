---
title: [Q7642] A2A 协议与多 Agent 互操作的演进
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7642 · A2A 协议与多 Agent 互操作的演进

难度：P6 ｜ 标签：版本演进 / 多 Agent / 协议

**问**：MCP 解决了"Agent ↔ 工具"的连接问题，"Agent ↔ Agent"的互操作是另一层。A2A（Agent-to-Agent）协议要解决什么问题？它的核心机制（Agent Card、任务生命周期）是什么，与 MCP、与自建消息总线相比怎么选？

**答**：
- **结论**：A2A（2025 由 Google 发起、后进入 Linux 基金会）解决的是**跨厂商/跨框架的 Agent 互操作**：你的 LangGraph Agent 要调用别人的 Agent（可能是不同框架、不同厂商、身份不同），需要标准化的"能力发现 + 任务委托 + 状态回报"。核心机制：① **Agent Card**：托管在 `/.well-known/agent.json` 的能力自描述（名称、技能、端点、认证要求），客户端先发现再调用——对应 MCP 的 tools list，但粒度是"Agent 整体技能"而非"单个工具"；② **任务生命周期**：调用不是函数调用而是**长任务**（`tasks/send` / `tasks/sendSubscribe`），带 task id 与状态机（submitted → working → input-required → completed/failed），支持流式（SSE）与长时任务轮询——"input-required" 状态是特色：被调 Agent 可以请求补充输入（HITL，Q7633 的等待问题在协议层有了位置）；③ **产物与消息**：任务产出 Artifact（文件/结构化数据），消息按角色组织。选型：MCP 管"Agent 与工具/数据"的纵向连接，A2A 管"Agent 与 Agent"的横向协作，**互补不竞争**；自建消息总线（Q7505）适合同团队紧耦合编排，A2A 适合跨组织/跨厂商的松耦合委托——评价维度是"信任边界"：跨边界用协议（标准化认证与发现），边界内用编排框架。
- **取舍**：协议化互操作的代价：抽象层漏抽象（A2A 的任务模型对简单调用是过重负担）、版本协商与兼容负担（Q7578 MCP 版本演进的同款问题）、以及"能力发现"的信任问题——Agent Card 自描述不可信，需要注册中心或签名。收益：供应商可替换、跨团队标准接口、长任务与 HITL 的一等支持。
- **实战**：① 评估时先问"协作方是否跨信任边界"——边界内硬上 A2A 是抽象税；② Agent Card 的技能描述质量决定被调用率（同 Q7559 工具描述问题的 Agent 版）；③ 客户端实现要处理 input-required 状态：把"补充输入"路由回用户或上游 Agent，超时策略明确。

```python
# A2A 任务生命周期模型: 发现(Agent Card) -> 委托 -> 状态机 -> input-required 处理
# 基线: Python 3.9+ 标准库 (协议语义演示, 生产用 a2a SDK)
from dataclasses import dataclass, field


@dataclass
class AgentCard:
    name: str
    skills: list[str]
    endpoint: str
    auth: str


@dataclass
class A2ATask:
    task_id: str
    state: str = "submitted"      # submitted/working/input-required/completed/failed
    artifacts: list[str] = field(default_factory=list)


class A2AClient:
    def discover(self, card: AgentCard, needed_skill: str) -> bool:
        """能力发现: Agent Card 是否声明所需技能。"""
        return needed_skill in card.skills

    def send(self, task: A2ATask, reply_input: str | None = None) -> str:
        if task.state == "input-required":
            if reply_input is None:
                return "WAIT: 被调方需要补充输入, 路由回用户或上游"
            task.state = "working"
        if task.state == "working":
            task.state = "completed"
            task.artifacts.append("result.json")
        return f"DONE: {task.state} artifacts={task.artifacts}"


def main() -> None:
    card = AgentCard("travel-agent", ["book-flight", "plan-trip"],
                     "https://a.example", "oauth2")
    client = A2AClient()
    assert client.discover(card, "book-flight")       # 发现
    assert not client.discover(card, "pay-tax")
    task = A2ATask("t-1")
    task.state = "input-required"                     # 长任务中间态: 要补充输入
    assert client.send(task).startswith("WAIT")
    assert client.send(task, reply_input="depart=2026-12-01") == \
        "DONE: completed artifacts=['result.json']"
    # 与 MCP 分工: MCP 连工具(纵向), A2A 委托 Agent(横向长任务)
    assert task.state == "completed"
    print("OK: AgentCard 发现 + 任务状态机(含 input-required HITL) + Artifact 回传")


if __name__ == "__main__":
    main()
```

**追问 1**：A2A 为什么把"调用"建模成任务而不是函数调用？
→ 一句话提示：Agent 工作常是分钟级长任务且可能要补充输入（input-required）或中途失败，函数调用的同步短事务语义装不下——任务状态机 + Artifact + 流式订阅是对长交互的原生建模。

**追问 2**：Agent Card 自描述的信任问题怎么解？
→ 一句话提示：能力声明可以夸大（同 Q7559 描述质量问题的恶意版），需要可信注册中心/签名卡/调用后评级闭环；纯自描述只适用于低风险内部场景。

## 背诵要点
- A2A = Agent 间横向互操作协议（Agent Card 发现 + 任务状态机 + Artifact），MCP = Agent 与工具的纵向连接——互补不竞争。
- 状态机关键态：working / **input-required**（HITL 在协议层有一等位置）/ completed / failed；支持 SSE 流式与长任务。
- 选型维度是信任边界：跨边界用协议（标准认证/发现），边界内用编排框架（Q7505）；Card 自描述需注册中心/签名兜信任。

## 复盘追问
- 为什么说"边界内硬上 A2A 是抽象税"？提示：内部紧耦合编排需要低延迟强类型与共享状态，A2A 的发现/协商/长任务模型全是多余开销；协议价值只在跨边界标准化。
- A2A 客户端遇到 failed 状态的重试语义是什么？提示：与 HTTP 重试不同——任务可能已部分执行，重试要带幂等键与上游确认（同 Q7509 SAGA/补偿问题），盲目重发会重复副作用。
