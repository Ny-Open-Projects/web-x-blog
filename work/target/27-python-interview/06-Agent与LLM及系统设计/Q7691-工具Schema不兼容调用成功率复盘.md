---
title: [Q7691] 工具 Schema 不兼容导致调用成功率为零复盘
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7691 · 工具 Schema 不兼容导致调用成功率为零复盘

难度：P6 ｜ 标签：事故复盘、function calling、JSON Schema、兼容性

基线：Python 3.9+；OpenAI tools API（1.x SDK）/ 其他兼容网关。

**问**：接入某网关后，模型的工具调用成功率从 95% 掉到 0——模型从不发起 tool_calls，或参数永远校验失败。Schema 层面有哪些"人眼看没问题、模型读不懂"的坑？这类事故怎么定位和防住？

**答**：
- **结论**：工具调用成功率的分母是"该调用的场景数"，归零常见四类 schema 坑：(1) **嵌套过深/anyOf 复杂结构**——很多兼容网关只支持扁平的对象 schema，嵌套 anyOf/oneOf 被静默忽略，模型按自由文本输出；(2) **缺 required/description**——参数没有描述，模型只能猜语义，猜错就过不了校验；(3) **默认值与 nullable 语义不一致**——schema 声明 required 但运行时又允许缺省，模型输出与校验器各说各话；(4) **枚举值里混中文/特殊字符**或 JSON Schema 方言不被支持。定位方法：把模型原始输出（不做校验拦截）打出来看它是"没调"还是"调错参数"，两者修法不同。
- **取舍**：schema 写得越严格（约束越多）模型越稳，但跨供应商兼容性越差；生产做法是"对外一套规范 schema + 按供应商做方言转换层"，并用 JSON Schema 校验器（jsonschema 库）在本地先校验一遍再报错，错误信息回喂模型让它自纠（一次重试修复大部分格式问题）。
- **实战**：上线前的"工具健康检查"：对每个工具跑固定评测集（10~20 个应调用场景），统计调用率/参数校验通过率；schema 变更走评审（description 是 prompt 的一部分，改 schema 等于改 prompt）。

```python
# 工具 Schema 健康检查：静态 lint + 调用结果归类（标准库可运行）。
def lint_tool_schema(schema: dict) -> list[str]:
    issues = []
    if schema.get("type") == "object":
        props = schema.get("properties", {})
        if not schema.get("required"):
            issues.append("无 required 字段：模型可能漏传关键参数")
        for name, p in props.items():
            if not p.get("description"):
                issues.append(f"参数 {name} 缺 description：模型只能猜语义")
            if p.get("type") == "object" and "properties" not in p:
                issues.append(f"参数 {name} 是无 schema 的自由 object："
                              f"兼容网关易静默丢弃")
            if any(k in p for k in ("anyOf", "oneOf", "allOf")):
                issues.append(f"参数 {name} 用了 {set(p) & {'anyOf','oneOf','allOf'}}："
                              f"部分网关不支持，需扁平化")
    else:
        issues.append("顶层不是 object：多数网关只支持 object 根 schema")
    return issues or ["schema 检查通过"]

def classify_calls(raw_outputs: list[str], validator) -> dict[str, int]:
    """把模型原始输出归类：没调 / 参数错 / 成功。"""
    bucket = {"no_call": 0, "bad_args": 0, "ok": 0}
    for out in raw_outputs:
        if '"name"' not in out:
            bucket["no_call"] += 1
        elif not validator(out):
            bucket["bad_args"] += 1
        else:
            bucket["ok"] += 1
    return bucket

if __name__ == "__main__":
    schema = {"type": "object",
              "properties": {"city": {"type": "string"},
                             "date_range": {"anyOf": [{"type": "string"}]}}}
    for line in lint_tool_schema(schema):
        print("-", line)
    # - 无 required 字段...
    # - 参数 city 缺 description...
    # - 参数 date_range 用了 {'anyOf'}：部分网关不支持，需扁平化
```

**追问**：
- 一层："模型不调用"和"参数总错"分别怎么修？→ 提示：不调用通常是描述/示例缺失或网关把 tools 字段丢了（看请求日志）；参数错是 schema 语义问题，用校验错误回喂重试。
- 二层：为什么 schema 变更要当 prompt 变更管理？→ 提示：description 直接进上下文影响模型行为；schema 改动要有评测集回归，防止其他工具调用质量劣化。

**背诵要点**：
1. Schema 四坑：anyOf/嵌套不兼容、缺 description/required、nullable 语义不一致、顶层非 object。
2. 定位先分类：原始输出是"没调"（描述/网关问题）还是"参数错"（校验回喂重试能修大半）。
3. 防线：上线前工具健康检查（调用率+校验通过率）、schema 评审当 prompt 管理、本地 jsonschema 预校验。

**复盘追问**：
1. 为什么上线前没发现成功率是 0？提示：评测集可能只测了"直接问答"，没有覆盖应调用工具的场景。
2. 多供应商接同一个 agent 时 schema 怎么管？提示：单一规范 schema + 供应商方言转换层 + 每供应商独立评测基线。
