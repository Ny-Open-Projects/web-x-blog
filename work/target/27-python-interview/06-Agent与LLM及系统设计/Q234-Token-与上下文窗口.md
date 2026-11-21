---
title: [Q234] Token 与上下文窗口
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q234 · Token 与上下文窗口

> 难度:★★★ | 标签:Agent, Token

**问**:什么是 token 和上下文窗口?超限了怎么办?

**答**:token 是模型的最小文本单元,英文约 1 token≈4 字符,中文约 1 字≈1-2 token,计费与限额都按 token 计算。上下文窗口是模型单次能处理的最大 token 数(input+output 共享),超限会直接报错或截断。超限的工程手段:滑动窗口截断旧消息、历史摘要压缩、RAG 只塞检索片段而非全文档、长任务拆分为多轮子任务。

```python
# file: code/06_Agent与LLM及系统设计/q234_context_window.py
"""实现一个带 token 预算的滑动窗口消息管理器,超限时丢最旧的非 system 消息。"""


class ContextWindow:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.messages: list[dict] = [{"role": "system", "content": ""}]

    @staticmethod
    def _tokens(text: str) -> int:
        return max(1, len(text) // 2)  # 演示用估算

    def _total(self) -> int:
        return sum(self._tokens(m["content"]) for m in self.messages)

    def add(self, role: str, content: str) -> None:
        self.messages.append({"role": role, "content": content})
        while self._total() > self.max_tokens and len(self.messages) > 1:
            removed = self.messages.pop(1)  # 保留 system,丢最旧一条
            print(f"  [裁剪] 丢弃旧消息:{removed['content'][:10]}...")

    def render(self) -> int:
        return self._total()


if __name__ == "__main__":
    cw = ContextWindow(max_tokens=30)
    cw.messages[0]["content"] = "你是助手"
    for i in range(5):
        cw.add("user", f"这是第{i}条比较长的用户消息,用来占 token")
        print(f"添加消息{i}后总 token ≈ {cw.render()},消息数 {len(cw.messages)}")
```

**追问**:
- 窗口越大越好吗?不是,长上下文有成本(按 token 计费)、延迟上升、"lost in the middle"中间信息注意力下降问题,该短则短。
- 中文的 token 估算怎么做?——同系列 tokenizer 离线计算最准(如 tiktoken 对应模型);按 1 字≈1-2 token 估算用于容量规划。
- 截断从哪里截?——优先丢最旧的低价值消息,system 与当前任务指令永不丢;工具原始大结果最先牺牲。
- 历史摘要压缩的代价?——丢细节(数字、名字),重要实体要走结构化槽位;摘要质量本身要用评估集验证。
