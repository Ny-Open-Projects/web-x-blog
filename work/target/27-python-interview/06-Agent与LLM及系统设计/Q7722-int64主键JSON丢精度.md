---
title: "[Q7722] 结构化输出的 int64 主键：前端为什么少了一"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7722 · 结构化输出的 int64 主键：前端为什么少了一

难度：P6 ｜ 标签：结构化输出、JSON、int64、精度

基线：Python 3.12；JSON Schema `integer`、OpenAI structured outputs；纯 Python 模拟 IEEE 754 double。

**问**：让模型按 schema 输出订单信息，`order_id` 定义为 `integer`。后端 Python 解析出来是 `9007199254740993`，前端页面显示 `9007199254740992`，点"查看详情"查不到订单；批量对账时两个不同订单还被合并成一条。Python 的 int 是任意精度，为什么到了前端会变？

**答**：
- **结论**：JSON 规范只规定 number，没规定精度；JavaScript/大多数前端运行时用 **IEEE 754 double** 解析，安全整数上限是 `2^53 - 1 = 9007199254740991`。超过这个值的 int64 ID 会被舍入到最近的 double，`...993` 变成 `...992`，不同 ID 可能撞成同一个数。Python 的 `json.loads` 保留任意精度 int，所以"后端对、前端错"，问题在**跨语言表示**而不是模型。
- **取舍**：把 ID 序列化成**字符串**是最稳的（schema 用 `type: "string"`，约定 `format: "int64"`），代价是所有比较/排序要按字符串或转 BigInt，索引设计要一致；用 BigInt/自定义 parser 能保留数字语义，但要求链路每一跳（网关、日志、缓存、前端框架）都支持，漏一处就前功尽弃。让模型直接生成超长数字还多一层风险：模型可能自己就数错位。
- **实战**：① 对外 JSON 的 ID 一律 string，包括 LLM 结构化输出 schema；② 内部 DB 用 bigint，出口做显式 `str()` 转换，别依赖框架默认；③ 契约测试覆盖 `2^53-1`、`2^53`、`2^63-1` 边界；④ 日志/埋点里的 ID 也要按字符串处理，否则 ELK 里同样丢精度。

```python
"""模拟 JS Number 解析：超过 2^53-1 的整数被舍入。"""
import json

MAX_SAFE_INTEGER = 2**53 - 1


def to_js_number(value: int) -> float:
    """JS 的 Number 就是 IEEE 754 double。"""
    return float(value)


def parse_like_js(payload: str) -> dict:
    data = json.loads(payload)
    return {k: to_js_number(v) if isinstance(v, int) else v
            for k, v in data.items()}


if __name__ == "__main__":
    ids = [9007199254740991, 9007199254740992, 9007199254740993]
    print("安全上限:", MAX_SAFE_INTEGER)
    for i in ids:
        js = to_js_number(i)
        print(f"{i} -> double {js:.0f}  相等? {int(js) == i}")

    payload = json.dumps({"order_id": 9007199254740993})
    print("Python 解析:", json.loads(payload))
    print("前端解析  :", parse_like_js(payload))

    a, b = 9007199254740992, 9007199254740993
    merged = {to_js_number(a): "A", to_js_number(b): "B"}
    print("两个 ID 作为 key:", merged, "-> 后写覆盖前写")

    safe = json.dumps({"order_id": str(b)})
    print("ID 转字符串:", safe, "-> 全链路无损")
```

**追问一**：为什么 Protobuf 的 `int64` 在 JSON 映射里也建议用 string？
→ 解析：Proto3 的 JSON 映射规定 64 位整数用**字符串**表示，正是因为 JSON number 在被 JS 等语言解析时会丢精度。`int32` 可以安全用 number，`int64/uint64/fixed64` 必须 string。自定义 schema 时应遵循同样的边界约定，而不是等前端踩坑。

**追问二**：让模型输出 `integer` 类型的 ID，除了精度还有什么风险？
→ 解析：模型可能把长数字**数错位/补零/截断**（tokenizer 对长数字不友好），也可能把前导零丢掉；即使 schema 校验通过，值本身也可能是幻觉。ID 这类"必须来自系统"的字段不应由模型生成，应在工具层注入或生成后由服务端回填，模型只负责引用占位符。
