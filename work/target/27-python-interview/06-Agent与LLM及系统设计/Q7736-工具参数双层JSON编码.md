---
title: "[Q7736] 工具参数被双层编码：arguments 里是一段“字符串里的 JSON”"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7736 · 工具参数被双层编码：arguments 里是一段"字符串里的 JSON"

难度：P6 ｜ 标签：function calling、arguments、JSON 解析、schema 设计

基线：Python 3.12；OpenAI 兼容 `tool_calls[].function.arguments` 为字符串；schema 用 `object` 而非 `string`。

**问**：解析 tool_calls 时 `json.loads(tc.function.arguments)` 得到 `{"query": "{\"city\": \"上海\"}"}`——`query` 的值**又是一段 JSON 字符串**。工具把这整段当查询词，检索全空。模型为什么把参数套两层？怎么防？

**答**：
- **结论**：协议层 `arguments` 本身就是**字符串**（内部是 JSON 文本，这样流式才能逐字符拼接），这是第一层，必须 `json.loads` 一次。第二层是模型"过度结构化"：schema 里字段类型声明成 `string` 而语义是结构化数据（`filter`、`payload`、`query`）时，模型会把 JSON 序列化后塞进字符串；也有客户端把已经是 dict 的参数又 `json.dumps` 一次。
- **取舍**：`arguments` 必须解析一次（协议）；字段内要不要再解析取决于 schema。把结构化字段声明成 `object`（带 `properties`）能从源头避免模型自行编码，但部分供应商对嵌套 object 支持差、strict 模式限制多。解析侧做"受控展开一层 + 类型校验"最稳，但要防止把用户本来就想要的字符串误解析。
- **实战**：① schema 能用 object/array 就别用 string 装 JSON；② `unwrap(v, depth=1)` 只在"字符串以 `{`/`[` 开头且能解析"时展开；③ 用 pydantic 校验，失败回灌错误让模型重试（带上期望 schema）；④ 保留原始 `arguments` 便于复盘；⑤ 单测覆盖单层/双层/非法 JSON/正常字符串四种输入。

```python
"""tool_calls 参数解析：协议层一次 loads，字段层受控展开一层。"""
import json


def parse_arguments(raw: str) -> dict:
    """协议层：arguments 是字符串，必须解析一次。"""
    if not isinstance(raw, str):
        raise TypeError("arguments 应为字符串（即使客户端已经给了 dict）")
    if not raw.strip():
        return {}
    return json.loads(raw)


def unwrap_json_string(value, depth: int = 1):
    """字段级展开：只展开一层，且必须像 JSON。"""
    if depth <= 0 or not isinstance(value, str):
        return value
    s = value.strip()
    if not (s.startswith("{") and s.endswith("}")) and not (s.startswith("[") and s.endswith("]")):
        return value                        # 普通字符串，原样保留
    try:
        inner = json.loads(s)
    except json.JSONDecodeError:
        return value                        # 解析不了就保留原文，交给校验层
    if isinstance(inner, (dict, list)):
        return inner
    return value


def normalize(args: dict, structured_fields: set[str]) -> dict:
    out = dict(args)
    for field in structured_fields & out.keys():
        out[field] = unwrap_json_string(out[field])
    return out


if __name__ == "__main__":
    # 1) 单层：正常情况
    raw1 = '{"city": "上海", "days": 3}'
    print("单层:", parse_arguments(raw1))

    # 2) 双层：query 里又套了 JSON
    raw2 = '{"query": "{\\"city\\": \\"上海\\", \\"days\\": 3}"}'
    args2 = parse_arguments(raw2)
    print("双层原始:", args2)
    fixed = normalize(args2, {"query"})
    print("展开一层:", fixed, "| query 类型:", type(fixed["query"]).__name__)

    # 3) 用户本来就想要一个 JSON 形式的字符串：不能被误展开
    raw3 = '{"text": "{\\"a\\": 1}"}'
    print("不在结构化字段里，保持原样:", normalize(parse_arguments(raw3), {"query"}))

    # 4) 非法 JSON：展开失败保留原文
    raw4 = '{"query": "{city: 上海}"}'
    print("非法内层:", normalize(parse_arguments(raw4), {"query"}))

    # 5) 协议层错误：arguments 为空串
    print("空 arguments:", parse_arguments(""))

    # 6) 已经给 dict 的客户端：直接报错，避免静默双编码
    try:
        parse_arguments({"city": "上海"})       # type: ignore[arg-type]
    except TypeError as e:
        print("类型错误:", e)

    print("结论：协议层解析一次；字段层只展开白名单字段一层；未知一律保留并校验")
```

**追问一**：为什么协议不直接让模型返回对象？
→ 解析：`arguments` 固定为 string 是为了**流式增量拼接**——参数是逐 token 到达的，客户端先把片段拼成完整字符串，最后才解析。即使模型"想"返回对象，传输层也是字符串，客户端必须自己 `json.loads`。

**追问二**：`arguments` 是非法 JSON 怎么处理？
→ 解析：不能静默丢弃。应回一条 tool 消息说明"参数解析失败 + 期望的 schema"，让模型重发；同时设重试上限（如 2 次），超限降级为向用户澄清。直接抛异常会让整轮对话失败，用户只看到"系统错误"。
