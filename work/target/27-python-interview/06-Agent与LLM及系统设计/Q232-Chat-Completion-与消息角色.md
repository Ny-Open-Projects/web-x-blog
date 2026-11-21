---
title: [Q232] Chat Completion 与消息角色
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q232 · Chat Completion 与消息角色

> 难度:★★ | 标签:Agent, Chat

**问**:Chat Completion 的三种消息角色分别是什么?它们如何影响模型行为?

**答**:三种核心角色是 system(设定身份、规则、边界,权重最高)、user(用户输入)、assistant(模型历史回复,用于多轮上下文)。模型把整个 messages 列表当作输入,assistant 历史让模型"看到自己说过什么",保持一致性;system 决定全局行为。很多 API 还支持 tool 角色表示工具返回结果。

```python
# file: code/06_Agent与LLM及系统设计/q232_chat_roles.py
"""演示消息角色的组织方式,并统计 token 预算(按简单切分模拟)。"""


class FakeChatModel:
    def chat(self, messages):
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        return f"遵守规则[{system[:6]}],回答你的问题"


def build_messages(system: str, history: list[tuple[str, str]], user: str) -> list[dict]:
    msgs = [{"role": "system", "content": system}]
    for u, a in history:
        msgs += [{"role": "user", "content": u}, {"role": "assistant", "content": a}]
    msgs.append({"role": "user", "content": user})
    return msgs


def approx_tokens(messages) -> int:
    return sum(len(m["content"]) for m in messages) // 2  # 简化估算


if __name__ == "__main__":
    msgs = build_messages(
        "你是客服,只用中文回答",
        history=[("怎么退货?", "在订单页点申请退货")],
        user="退款多久到账?",
    )
    for m in msgs:
        print(m["role"], "->", m["content"])
    print(FakeChatModel().chat(msgs), "| 估算 token:", approx_tokens(msgs))
```

**追问**:
- system 消息放多条会怎样?多数 API 允许但按顺序拼接生效,一般建议合并为一条避免语义冲突。
- tool 角色消息的语义?——工具执行结果的回传,与 tool_call id 对应;缺失或不匹配会让下一轮请求直接报错。
- 多轮对话为什么必须回传 assistant 历史?——模型无状态,「看到自己说过什么」才能保持一致;只回传 user 会答非所问。
- system 权重最高是什么意思?——训练时对齐让它主导行为,但不是不可覆盖(注入仍可能);安全不能只靠 system 一层。
