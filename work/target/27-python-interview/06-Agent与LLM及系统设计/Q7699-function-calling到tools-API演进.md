---
title: [Q7699] function calling 到 tools API 与 Responses 演进
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7699 · function calling 到 tools API 的接口演进

难度：P6 ｜ 标签：版本演进、function calling、tools API、协议设计

基线：Python 3.9+；OpenAI SDK 1.x（chat.completions tools 字段）；MCP 等标准协议为对照。

**问**：2023 年用 `functions` 参数写的 agent，现在 SDK 会警告"已弃用，请用 `tools`"。`functions → tools` 只是改了个字段名吗？后续的工具调用协议演进（并行调用、MCP 标准化）对应用层设计有什么要求？

**答**：
- **结论**：不只是改名，语义有三处演进：
  1. **单函数 → 多工具数组**：`functions`（单个或列表的函数定义）演进为 `tools=[{"type": "function", "function": {...}}]`，为多类型工具（function、代码解释器、自定义）预留了 `type` 维度——这个设计直接预示了后来的统一工具生态；
  2. **并行调用**：新协议下模型一次返回多个 `tool_calls`，老代码按"一次一个"写的循环会漏执行或串行化，必须按 `tool_call_id` 批量回填 role="tool" 消息；
  3. **严格模式**：`strict: true`（结构化输出约束）让 schema 真正被解码层强制，而不是"提示级约束"——老代码里"模型输出不符合 schema"类错误大幅减少，但 strict 下 schema 子集受限（不支持部分关键字）。
  对应用层的结构性要求：**工具协议要与应用解耦**——工具注册中心（名称/schema/处理器三元组）+ 与各家 API 方言的转换层，而不是把请求体直接拼进业务代码；这也是 MCP 这类标准协议出现的原因（把"工具在哪、怎么调"标准化，跨模型跨进程复用）。
- **取舍**：跟进新协议的收益（strict 输出、并行调用、原生工具生态）vs 绑定单一供应商的风险；工程上的平衡是"内部统一工具协议 + 供应商适配器"，迁移时只改适配器。
- **实战**：升级检查清单——`functions` → `tools` 批量替换；处理 `finish_reason == "tool_calls"` 的并行分支（按 tool_call_id 回填）；schema 过 strict 校验器；工具结果消息格式核对（content 必须是字符串或结构化 content blocks）。

```python
# 工具调用演进的自检与并行回填演示（标准库可运行）。
def adapt_request(old: dict) -> dict:
    """functions 请求体 -> tools 请求体。"""
    req = dict(old)
    if "functions" in req:
        req["tools"] = [{"type": "function", "function": f}
                        for f in req.pop("functions")]
        req.pop("function_call", None)
    return req

def backfill_tool_results(messages: list[dict],
                          tool_calls: list[dict],
                          executor) -> list[dict]:
    """并行 tool_calls：按 tool_call_id 批量执行并回填。"""
    import concurrent.futures as cf
    results = {}
    with cf.ThreadPoolExecutor() as pool:
        futs = {pool.submit(executor, tc["function"]["name"],
                            tc["function"]["arguments"]): tc["id"]
                for tc in tool_calls}
        for fut, call_id in futs.items():
            results[call_id] = str(fut.result())
    return messages + [{"role": "tool", "tool_call_id": cid, "content": r}
                       for cid, r in results.items()]

if __name__ == "__main__":
    old = {"functions": [{"name": "get_weather",
                          "parameters": {"type": "object",
                                         "properties": {"city": {"type": "string"}}}}],
           "function_call": "auto"}
    print(adapt_request(old)["tools"][0]["type"])
    msgs = [{"role": "user", "content": "查北京和上海天气"}]
    calls = [{"id": "c1", "function": {"name": "get_weather",
                                       "arguments": '{"city": "北京"}'}},
             {"id": "c2", "function": {"name": "get_weather",
                                       "arguments": '{"city": "上海"}'}}]
    out = backfill_tool_results(msgs, calls,
                                lambda name, args: f"{args} -> 晴 25 度")
    print(len(out), out[-2]["tool_call_id"], out[-1]["tool_call_id"])
    # tools 协议 + 并行回填：3 条消息，c1/c2 各自带 tool_call_id。
```

**追问**：
- 一层：为什么必须按 tool_call_id 回填而不是按顺序？→ 提示：并行调用下模型不保证顺序对应，回填错位会把结果给到错误的调用上下文；id 是唯一可靠关联。
- 二层：MCP 这类标准协议改变了什么？→ 提示：工具定义与执行从"每家 API 各一套"变为跨模型/跨进程的统一协议（服务器声明能力、客户端发现与调用），应用只需一次集成；代价是多一跳进程/网络间接层。

**背诵要点**：
1. functions→tools 三演进：type 维度的工具数组、并行 tool_calls（按 id 回填）、strict 结构化输出。
2. 结构性要求：内部统一工具协议 + 供应商适配器，禁止请求体直拼业务代码。
3. 升级检查清单：批量替换 functions、并行分支处理、strict schema 子集校验、tool 消息格式核对。

**复盘追问**：
1. 升级后为什么有的对话出现"工具结果张冠李戴"？提示：老代码按消息顺序回填，并行调用下 id 对不上；用 tool_call_id 断言做回归。
2. 接 MCP 时哪些老工具资产可以直接复用？提示：业务逻辑层可复用，schema 与传输层要按 MCP 规范重包装；这是适配层设计的回报。
