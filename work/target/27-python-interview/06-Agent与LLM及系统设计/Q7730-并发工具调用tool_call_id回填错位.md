---
title: "[Q7730] 并发工具调用回填错位：tool_call_id 对不上，模型答非所问"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7730 · 并发工具调用回填错位：tool_call_id 对不上，模型答非所问

难度：P7 ｜ 标签：function calling、tool_call_id、asyncio、消息契约

基线：Python 3.12；OpenAI 兼容 chat completions 的 `tool_calls` / `role="tool"` 契约；`asyncio.gather`。

**问**：一次 assistant 消息里并行发起 3 个工具调用（`search`、`weather`、`calc`），用 `asyncio.gather` 并发执行，按**完成顺序**回填成 3 条 `role="tool"` 消息。模型经常把天气结果当搜索结果回答；有时直接 400 `messages with role 'tool' must be a response to a preceding message with 'tool_calls'`。消息顺序到底有什么契约？

**答**：
- **结论**：协议要求三条：① assistant 里每个 `tool_call` 必须有**且仅有一条** `role="tool"` 消息响应，`tool_call_id` 精确匹配；② tool 消息必须**紧跟在**带 `tool_calls` 的 assistant 消息之后，中间不能插 user/assistant；③ 多条的先后协议上按 id 匹配、不强制顺序，但大量实现（含部分网关）按**位置**配对，错序就会串结果。`asyncio.gather` 的完成顺序 ≠ 声明顺序，直接 append 必然错位。
- **取舍**：并发把 3 次 RTT 压成 1 次，但必须建 `tool_call_id -> result` 映射再按 `tool_calls` 原序回填；串行最稳但慢。某个工具超时：要么补一条结构化错误（`{"error": "timeout"}`）保持配对完整，要么整轮重来——**不能只回填成功的两条**，缺失响应直接非法。
- **实战**：① `{tc.id: future}` 建映射，`gather(return_exceptions=True)`，最后按 `tool_calls` 原序生成消息；② 校验 id 集合：数量相等、无重复、无缺失；③ 失败工具回填 `is_error` 字段而不是丢弃；④ 测试断言"tool 消息数 == tool_calls 数 且 id 集合相等"；⑤ 日志记录每个 id 的耗时，便于定位是哪个工具拖慢。

```python
"""并发工具结果回填：按完成顺序 append 会错位，按 id 映射才不会。"""
import asyncio
from dataclasses import dataclass, field


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict


@dataclass
class ToolMessage:
    role: str
    tool_call_id: str
    content: str


@dataclass
class Tool:
    name: str
    delay: float
    output: str
    should_fail: bool = False

    async def run(self, args: dict) -> str:
        await asyncio.sleep(self.delay)
        if self.should_fail:
            raise TimeoutError(f"{self.name} timed out")
        return self.output


async def execute_all(calls: list[ToolCall], registry: dict[str, Tool]) -> dict[str, str]:
    completed: list[tuple[str, str]] = []          # 按真实完成顺序追加

    async def one(tc: ToolCall) -> None:
        try:
            out = await registry[tc.name].run(tc.arguments)
        except Exception as e:                     # 失败也要有结果，不能缺配对
            out = f'{{"error": "{type(e).__name__}: {e}"}}'
        completed.append((tc.id, out))

    await asyncio.gather(*(one(tc) for tc in calls))
    return dict(completed)                         # 字典顺序 = 完成顺序


def build_tool_messages(calls: list[ToolCall], results: dict[str, str]) -> list[ToolMessage]:
    missing = [tc.id for tc in calls if tc.id not in results]
    if missing:
        raise ValueError(f"缺少工具结果: {missing}")
    if len(results) != len(calls):
        raise ValueError(f"结果数 {len(results)} != 调用数 {len(calls)}")
    return [ToolMessage("tool", tc.id, results[tc.id]) for tc in calls]   # 按声明顺序


if __name__ == "__main__":
    calls = [
        ToolCall("call_a", "search", {"q": "退款政策"}),
        ToolCall("call_b", "weather", {"city": "上海"}),
        ToolCall("call_c", "calc", {"expr": "1+1"}),
    ]
    registry = {
        "search": Tool("search", 0.03, "退款需 7 个工作日"),
        "weather": Tool("weather", 0.01, "上海 18 度"),
        "calc": Tool("calc", 0.02, "2"),
    }

    results = asyncio.run(execute_all(calls, registry))
    print("完成顺序（按耗时）:", list(results))          # dict 保持插入顺序 = 完成顺序

    msgs = build_tool_messages(calls, results)
    for m in msgs:
        print(f"  tool_call_id={m.tool_call_id} -> {m.content}")
    print("回填顺序 = 声明顺序:", [m.tool_call_id for m in msgs] == [c.id for c in calls])

    # 错误示范：直接按完成顺序 append
    naive = [ToolMessage("tool", cid, out) for cid, out in results.items()]
    print("按完成顺序 append:", [m.tool_call_id for m in naive], "-> 与声明顺序不一致")

    # 某个工具失败：仍要占位
    bad = {"search": Tool("search", 0.01, "", should_fail=True)}
    r2 = asyncio.run(execute_all(calls[:1], bad))
    print("失败工具回填:", r2)

    # 缺配对直接非法
    try:
        build_tool_messages(calls, {"call_a": "ok"})
    except ValueError as e:
        print("缺配对:", e)
```

**追问一**：为什么"只回填成功的"会 400 而不是被忽略？
→ 解析：协议要求 assistant 的 `tool_calls` 全部被响应，缺失属于非法消息序列，多数实现直接拒绝。即使某些实现容忍，模型也会把随后的 user 消息当作对"未完成调用"的回应，行为完全不可预期。

**追问二**：同一个工具被调用两次（同名不同 id）怎么处理？
→ 解析：必须按 `id` 区分，不能按 `name`。可以对 `(name, arguments)` 相同的调用做结果缓存减少重复执行，但回填仍要两条独立消息，各自用自己的 id；用 name 当键会把两次结果合并成一条，另一个调用就缺失了。
