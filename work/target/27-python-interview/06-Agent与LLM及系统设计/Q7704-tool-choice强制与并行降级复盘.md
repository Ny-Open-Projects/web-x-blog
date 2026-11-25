---
title: "[Q7704] tool_choice 强制与并行调用降级事故复盘"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7704 · tool_choice 强制与并行调用降级事故复盘

难度：P6 ｜ 标签：事故复盘、工具调用、tool_choice、协议兼容

基线：Python 3.12；OpenAI tools / tool_choice 字段；纯 Python 模拟调用归一化。

**问**：Agent 里为了"必须调用某个工具"用了 `tool_choice` 强制指定，结果遇到多工具并行时行为异常：要么模型忽略强制、要么返回的并行调用被应用按单调用处理丢了几个。为什么？怎么设计才稳？

**答**：
- **结论**：两个独立问题叠加。(1) `tool_choice` 的强制值通常只接受**单个具体工具**（`{"type":"function","function":{"name":"x"}}`），与"允许并行多工具"的上层诉求冲突——强制某工具时模型很难同时合理发起其他工具的并行调用；(2) 应用侧若按"一次一个 tool_call"写循环，遇到返回的**多个 `tool_calls`** 就会漏执行或串行化，回填时又必须按 `tool_call_id` 一一对应，否则结果张冠李戴。
- **取舍**：需要"必须调工具"时用 `tool_choice="required"`（要求至少调一个，不指定具体哪个）而非强制某个具体工具，保留并行能力；只有确实只能调一个的场景才强制具体工具。并行调用要按 id 批量执行、按 id 回填。
- **实战**：协议层归一化——把不同供应商的 tool choice 语义抹平到内部统一表示；对返回的 `tool_calls` 一律按列表处理（即使只有一个）；回填做 id 一致性断言；把"强制某工具 + 并行"这种组合列为不推荐的反模式，用测试固化。

```python
def normalize_calls(raw: list[dict] | dict | None) -> list[dict]:
    """把单调用/多调用/空 统一成列表，避免按'一次一个'处理漏掉并行。"""
    if raw is None:
        return []
    if isinstance(raw, dict):
        return [raw]
    return raw


def backfill_by_id(messages: list[dict], calls: list[dict], results: dict[str, str]) -> list[dict]:
    """按 tool_call_id 回填，保证并行调用结果不串位。"""
    return messages + [
        {"role": "tool", "tool_call_id": c["id"], "content": results[c["id"]]}
        for c in calls
    ]


if __name__ == "__main__":
    calls = normalize_calls([{"id": "c1"}, {"id": "c2"}])
    msgs = backfill_by_id([], calls, {"c1": "A结果", "c2": "B结果"})
    print("回填条数:", len(msgs), "id:", [m["tool_call_id"] for m in msgs])
```

**追问一**：为什么 `tool_choice` 强制具体工具会破坏并行？
→ 解析：强制具体工具把决策空间收敛到单个工具，模型难以在同一轮再合理发起其他工具调用；且部分实现对强制模式下的并行支持不一致。要"至少调一个且可并行"用 `required`，别指定具体工具。

**追问二**：并行调用回填错位会有什么后果？
→ 解析：结果按消息顺序而非 id 回填时，A 工具的结果会被塞进 B 工具的上下文，模型基于错误结果继续推理，产出错误答案且难排查。必须用 tool_call_id 关联并加断言。
