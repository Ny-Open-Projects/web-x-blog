---
title: [Q7659] Responses API 与 Chat Completions 演进迁移
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7659 · Responses API 与 Chat Completions 的演进迁移

难度：P6-P7 | 标签：Responses API、版本演进、迁移

**问**：2025 年供应商把 Responses API 定为推荐主路径（替代 Chat Completions + 已弃用的 Assistants API，见 Q7624）。Responses 的增量价值是什么？存量 Chat Completions 代码迁移要动哪些核心概念？

**答**：结论：Responses 的核心变化是把"多轮状态"从客户端搬回服务端：① `previous_response_id` 让服务端托管对话历史，客户端不必每次重放全量 messages；② 内建工具（web_search、file_search、code_interpreter）声明即用，不用自己写工具循环；③ `input` 从"消息数组"泛化为"内容项列表"（文本/图片/工具输出混合）。增量价值集中在**有状态多轮与内建工具**场景；纯单轮无状态调用两者几乎等价，迁移收益低。

实战要点：
1. 概念映射：`messages` → `input`；`assistant` 历史 → `previous_response_id` 链；`tools` + 自写执行循环 → `tools` 声明 + 响应里的内建执行（自定 function 工具仍是"声明→等 output→回传"循环）。
2. 有状态化的代价：服务端托管历史意味着**状态不在你手里**——导出、审计、自建摘要（Q7514）、成本核算（Q7614 多轮重复计费口径变化）都要重新设计；数据驻留合规也要重审。
3. 迁移判据矩阵：单轮/低频 → 不动；多轮对话+需要服务端缓存 → 迁；Agent 重度自控（自写循环、自管状态） → 保留 Chat Completions 也很合理，别为迁而迁。

```python
"""两种 API 请求形态对照与迁移判据（标准库模拟，可运行）"""
from dataclasses import dataclass, field


@dataclass
class ChatCompletionsReq:
    """无状态：每轮重放全量历史"""
    messages: list[dict]

    def token_input_estimate(self, per_msg: int = 50) -> int:
        return len(self.messages) * per_msg


@dataclass
class ResponsesReq:
    """服务端托管历史：只发增量 + previous_response_id"""
    input: list[dict]
    previous_response_id: str | None = None

    def token_input_estimate(self, per_item: int = 50) -> int:
        return len(self.input) * per_item  # 历史在服务端


@dataclass
class MigrationJudge:
    multi_turn: bool
    server_side_history_needed: bool
    custom_agent_loop: bool

    def verdict(self) -> str:
        if self.custom_agent_loop and not self.server_side_history_needed:
            return "保留 Chat Completions：自管状态，迁移收益低"
        if self.multi_turn and self.server_side_history_needed:
            return "迁 Responses：服务端托管历史+内建工具"
        return "单轮为主：两者等价，不迁"

    def turn5_cost(self, hist_msgs: int = 10, per_msg: int = 50) -> dict:
        cc = ChatCompletionsReq([{}] * hist_msgs)
        rs = ResponsesReq([{}], previous_response_id="r4")
        return {"cc_input": cc.token_input_estimate(per_msg),
                "responses_input": rs.token_input_estimate(per_msg)}


j = MigrationJudge(multi_turn=True, server_side_history_needed=True,
                   custom_agent_loop=False)
print(j.verdict(), j.turn5_cost())

print(MigrationJudge(True, False, True).verdict())
```

**追问 1**：previous_response_id 的省 token 与 prompt 缓存有什么关系？
**提示**：服务端托管历史天然复用前缀（KV 缓存），计费按缓存价；但客户端自管历史也可以靠消息顺序稳定吃到前缀缓存——省的是"重放传输"和实现复杂度，不全是钱。

**追问 2**：服务端托管历史对"会话导出与审计"意味着什么？
**提示**：必须用专门的 retrieval 接口拉取完整对话，离线对账/合规导出变成异步依赖；数据驻留要求高的团队可能因此留在客户端自管。

## 背诵要点
- Responses 三增量：previous_response_id 服务端托管历史、内建工具、input 内容项泛化。
- 单轮调用两者等价；多轮+要托管 → 迁，自控 Agent 循环 → 可留 Chat Completions。
- 托管历史把状态交出去：导出/审计/合规驻留要重审，这是迁移的隐性成本。

## 复盘追问
- 你们的调用画像里，真正吃到 previous_response_id 收益的调用点占比多少？
- 迁移后成本核算口径（托管历史按缓存计）与旧对账逻辑怎么对齐？
