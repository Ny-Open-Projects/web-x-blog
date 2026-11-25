---
title: "[Q7710] 流式 tool_calls 的 arguments 增量拼接"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7710 · 流式 tool_calls 的 arguments 增量拼接

难度：P6 ｜ 标签：流式、function calling、增量解析、并发工具

基线：Python 3.12；OpenAI Chat Completions 流式 delta 结构；纯 Python 模拟。

**问**：流式开启后，模型返回的 `tool_calls` 不是一个完整对象，而是很多 delta 片段，`arguments` 被切成碎片。有人按到达顺序把所有 `arguments` 字符串直接相加，单个工具时正常；一旦模型并行调用两个工具，拼出来的 JSON 就坏了，参数张冠李戴。流式工具调用到底该怎么聚合？

**答**：
- **结论**：流式 `tool_calls` 的每个 delta 带一个 **`index`**，标识它属于第几个并行调用；同一个 index 的片段才属于同一个工具。正确做法是**按 index 分组**：第一次见到某 index 时记录 `id`/`name`，后续只把 `arguments` 追加到该 index 的缓冲区；收到 `finish_reason=tool_calls` 后再对每个完整字符串做 JSON 解析。按到达顺序全局拼接，会把 index 0 和 index 1 的参数交叉合并，必然坏。
- **取舍**：边收边解析（增量 JSON parser）能更早开始执行，但实现复杂、要处理不完整字符串；收完再解析简单可靠，代价是增加一次工具启动延迟。并行工具越多，按 index 分组的必要性越高；单工具场景的顺序拼接只是"碰巧对"。
- **实战**：① 聚合器用 `dict[index] -> {id, name, arguments}`，name 可能只出现在第一个片段；② 对 `arguments` 做长度上限与 JSON 校验，解析失败要能定位到 index 与原始片段；③ 不要假设 index 连续或从 0 开始；④ 工具执行前校验 `name` 与参数 schema，避免"参数拼错但 JSON 合法"的静默错误。

```python
import json


def merge_tool_deltas(deltas: list[dict]) -> dict[int, dict]:
    calls: dict[int, dict] = {}
    for delta in deltas:
        idx = delta["index"]
        slot = calls.setdefault(idx, {"id": None, "name": None, "arguments": ""})
        if delta.get("id"):
            slot["id"] = delta["id"]
        if delta.get("name"):
            slot["name"] = delta["name"]
        slot["arguments"] += delta.get("arguments", "")
    return calls


if __name__ == "__main__":
    deltas = [
        {"index": 0, "id": "call_a", "name": "get_weather", "arguments": '{"city":'},
        {"index": 1, "id": "call_b", "name": "get_time", "arguments": '{"tz":'},
        {"index": 0, "arguments": '"杭州"}'},
        {"index": 1, "arguments": '"Asia/Shanghai"}'},
    ]
    merged = merge_tool_deltas(deltas)
    for idx, call in merged.items():
        print(idx, call["name"], json.loads(call["arguments"]))
    naive = "".join(d.get("arguments", "") for d in deltas)
    print("按到达顺序拼接:", naive, "-> 非法 JSON")
```

**追问一**：为什么不能等第一个片段拿到 `name` 就立刻执行工具？
→ 解析：此时 `arguments` 还不完整，JSON 无法解析；而且并行调用时后续片段可能仍在传输。必须等到该工具的 `arguments` 结束（`finish_reason=tool_calls` 或流结束）并校验通过后才能执行。

**追问二**：如果某个 index 的 `arguments` 一直拼不完整，怎么定位是模型问题还是传输问题？
→ 解析：记录每个 index 的片段数、累计长度、最后若干字符与原始 delta；对比正常完成的调用。若流正常结束但 JSON 不闭合，多半是模型生成问题；若流中断，则是传输/超时。两类要分别告警，不能都归为"解析失败"。
