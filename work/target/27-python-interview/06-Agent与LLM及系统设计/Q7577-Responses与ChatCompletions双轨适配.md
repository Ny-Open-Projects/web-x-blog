---
title: "[Q7577] Responses API 与 Chat Completions 双轨适配"
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7577 · Responses API 演进与 Chat Completions 的双轨适配

难度：P6 ｜ 标签：版本演进 / OpenAI / API 演进 / 适配层

**问**：OpenAI 推出 Responses API 作为 Chat Completions 的演进方向（状态化会话、内置工具、多模态统一入口），团队老代码全在 Chat Completions 上。怎么设计双轨适配与迁移路线，避免被单一供应商 API 绑死？

**答**：

**结论**：两套 API 的实质差异：Chat Completions 是无状态的"消息进出"，状态（历史、工具结果）由调用方管理；Responses API 把会话状态服务端化（previous_response_id 链）、工具执行循环内建、输入输出统一为 items 模型。迁移的正确姿势不是"改调用点"，而是先建适配层：业务代码只依赖自家抽象（消息、工具、流式事件三种协议对象），适配层向下实现两套 API。这样迁移变成"适配层内切换"而不是全代码库改写，同时天然获得多供应商能力（Anthropic/Gemini 的消息模型又不同）。风险点：Responses 的服务端状态化与自家会话存储冲突（状态两份，一致性谁管）——迁移期必须选边：要么继续无状态模式（Responses 也支持一次性传全历史），要么整体切服务端状态并下线自家存储，不能双写。

**取舍**：早迁 vs 观望：Responses 上的新能力（内置 web search/file search、服务端工具编排）不迁移就用不到；但新 API 生态（第三方网关、开源推理服务 vLLM 兼容层）仍以 Chat Completions 为主——适配层是唯一能两头吃的架构。成本面：服务端状态化省去重传历史的 token（配合服务端缓存），但要付状态存储费；账按"会话平均轮数"算，轮数多的 Agent 场景 Responses 状态化更省，单轮场景无差别。

**实战**：适配层设计三原则：① 流式事件模型统一（两 API 的 SSE 事件粒度不同，适配层归一为 start/delta/tool_call/done 四类）；② 工具调用往返统一（tool_call id、参数 JSON、错误结构归一）；③ 能力探测降级（provider 不支持服务端状态时自动退回无状态模式）。CI 用录制的响应回放（cassette）测试两套后端行为一致性。

```python
# 双轨适配层：统一协议 + 能力探测降级（仅标准库，Python 3.9+）
from __future__ import annotations

from typing import Any, Callable


class UnifiedClient:
    def __init__(self, backend: str) -> None:
        self.backend = backend
        self.capabilities = {
            "openai-responses": {"server_state": True, "builtin_tools": True},
            "openai-chat": {"server_state": False, "builtin_tools": False},
        }[backend]

    def chat(self, messages: list[dict], state_id: str | None = None) -> dict:
        if state_id and not self.capabilities["server_state"]:
            # 能力缺失 → 降级为无状态：带上全量历史
            return {"backend": self.backend, "mode": "stateless",
                    "sent_messages": len(messages)}
        if self.backend == "openai-responses":
            return {"backend": self.backend,
                    "mode": "stateful" if state_id else "stateless",
                    "prev_id": state_id}
        return {"backend": self.backend, "mode": "stateless",
                "sent_messages": len(messages)}


def monthly_state_cost(avg_turns: int, tokens_per_turn: int,
                       state_price_per_1k: float = 0.0001) -> tuple[float, float]:
    """服务端状态省重传 vs 付存储费。"""
    resend = avg_turns * (avg_turns - 1) / 2 * tokens_per_turn  # 平方级重传
    storage = avg_turns * tokens_per_turn * state_price_per_1k / 1000 * 30
    return resend * 0.00015, storage  # 重传 token 费 vs 状态存储费


def main() -> None:
    msgs = [{"role": "user", "content": "hi"}] * 20
    c1 = UnifiedClient("openai-responses").chat(msgs, state_id="r1")
    c2 = UnifiedClient("openai-chat").chat(msgs, state_id="r1")
    assert c1["mode"] == "stateful"
    assert c2["mode"] == "stateless" and c2["sent_messages"] == 20  # 降级带全历史
    print(c1, c2)

    resend_cost, storage_cost = monthly_state_cost(avg_turns=15,
                                                   tokens_per_turn=3000)
    print(f"重传 token 费 ${resend_cost:.2f} vs 状态存储费 ${storage_cost:.2f}")
    assert resend_cost > storage_cost, "多轮会话状态化应更省"
    print("结论：适配层 + 能力探测降级，迁移是切后端不是改业务码")


if __name__ == "__main__":
    main()
```

**追问链**：

- 追问 1：服务端状态化后，自家的会话审计与风控怎么办？——审计不能依赖服务端黑盒状态：关键节点（工具调用、敏感输出）仍要自家 trace 落库（与 Q7558 trace 治理衔接）；风控读自家 trace 而不是 API 状态。这也是"状态可以托管、审计必须自持"的分界。
- 追问 1.1：两套 API 的流式事件粒度不同，适配层归一到四类会丢什么？——细粒度差异（token 级权重、reasoning 摘要事件、引用标注事件）在归一时要么丢弃要么进 extension 字段；丢弃前必须确认业务没消费它们，做法是适配层加"未处理事件"计数告警，上线头两周盯零。
- 追问 2：第三方网关/vLLM 只兼容 Chat Completions，双轨适配层怎么统一测试？——cassette 回放录制真实响应做两后端的行为断言（同输入同语义输出结构）；供应商差异面（限流头、错误码、幂等键）在适配层错误归一化里对齐成统一错误分类。

**背诵要点**：

1. 实质差异：Chat Completions 无状态调用方管状态，Responses 服务端状态化（previous_response_id）+ 内建工具；适配层让迁移变成切后端。
2. 状态迁移不能双写：要么无状态模式（Responses 也支持全历史），要么整体切服务端状态并下线自家存储。
3. 账按会话轮数算：多轮场景服务端状态省平方级重传 token 费；单轮无差别；审计 trace 必须自持不依赖服务端黑盒。

**复盘追问**：

1. 适配层上线后出现"未处理事件"告警激增，你的排查与收敛流程？
2. 如果供应商两年后下线 Chat Completions，你的适配层迁移预案里最耗时的三件事是什么？
