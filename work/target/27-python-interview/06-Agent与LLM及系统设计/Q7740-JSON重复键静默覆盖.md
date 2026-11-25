---
title: "[Q7740] 模型吐了重复键：json.loads 静默保留最后一个，金额被改大 10 倍"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7740 · 模型吐了重复键：json.loads 静默保留最后一个，金额被改大 10 倍

难度：P6 ｜ 标签：LLM、结构化输出、JSON、重复键

基线：Python 3.12；`json.loads` 的 `object_pairs_hook`；流式拼接后的文本校验。

**问**：抽取接口让模型输出 `{"amount": 100, "currency": "CNY"}`，`json.loads` 之后写库。对账发现有些单据金额是原值的 10 倍，回看原始响应，模型输出过长被重试拼接成了 `{"amount": 100, "amount": 1000, "currency": "CNY"}`。`json.loads` 没报错，直接返回了 `amount=1000`。为什么重复键不报错？怎么防？

**答**：
- **结论**：JSON 规范（RFC 8259）说对象内的名字"应当"唯一，但**没有规定重复时怎么办**；Python 的 `json` 采用"后者覆盖前者"，静默丢弃先出现的值。所以语法完全合法、解析不报错，语义却取决于"哪一次写入在后面"。流式拼接、多轮修复、把两次生成的片段拼起来，都会产生重复键。
- **取舍**：① 解析阶段就用 `object_pairs_hook` 检测重复并在**写库前失败**——这是唯一能发现重复键的时机，解析成 dict 之后就再也看不出来了；② 用 `pydantic`/`jsonschema` 做结构校验救不了，因为它们拿到的已经是去重后的 dict；③ 流式场景不要"字符串拼接后一次性 parse"，而是按完整 JSON 边界切分（或等服务端给完整对象），避免半截拼接。
- **实战**：① 统一封装 `strict_json_loads(text)`：`object_pairs_hook` 检重 + `parse_constant` 拒绝 `NaN/Infinity` + 顶层必须是对象/数组；② 重复键视为**可重试错误**：把"存在重复键"回灌给模型重新生成（并降低温度），而不是自己挑一个；③ 金额/数量这类字段加范围断言（0 < amount < 阈值），作为第二道闸；④ 记录原始响应文本（脱敏后）用于复盘，别只存解析后的 dict。

```python
"""json.loads 的重复键：默认后者覆盖，用 object_pairs_hook 才拦得住。"""
import json


class DuplicateKey(ValueError):
    pass


def strict_loads(text: str) -> dict:
    """检测重复键 + 拒绝 NaN/Infinity + 顶层必须是对象。"""

    def no_duplicates(pairs: list[tuple[str, object]]) -> dict:
        seen: dict[str, object] = {}
        for key, value in pairs:
            if key in seen:
                raise DuplicateKey(f"duplicate key: {key!r}（先 {seen[key]!r}，后 {value!r}）")
            seen[key] = value
        return seen

    def reject_constant(name: str):
        raise ValueError(f"非法常量: {name}")

    obj = json.loads(text, object_pairs_hook=no_duplicates,
                     parse_constant=reject_constant)
    if not isinstance(obj, dict):
        raise ValueError("顶层必须是对象")
    return obj


if __name__ == "__main__":
    bad = '{"amount": 100, "amount": 1000, "currency": "CNY"}'

    loose = json.loads(bad)
    print("默认解析:", loose, "-> 先出现的 100 被静默丢弃")

    try:
        strict_loads(bad)
    except DuplicateKey as e:
        print("严格解析:", e)

    # 嵌套对象同样会被检测
    nested = '{"order": {"id": 1, "id": 2}}'
    try:
        strict_loads(nested)
    except DuplicateKey as e:
        print("嵌套重复:", e)

    # NaN / Infinity：Python 默认能解析，但不是合法 JSON
    try:
        strict_loads('{"score": NaN}')
    except ValueError as e:
        print("非法常量:", e)

    # 正常输出仍然可用
    ok = strict_loads('{"amount": 100, "currency": "CNY"}')
    print("\n正常:", ok, "| 金额校验:", 0 < ok["amount"] < 10_000)

    # 解析成 dict 之后就再也看不到重复键了
    parsed = json.loads(bad)
    print("对 dict 做 schema 校验:", parsed, "-> 校验器无法知道曾经有两个 amount")
    print("结论：重复键只在解析那一刻可见，必须在 object_pairs_hook 里拦")
```

**追问一**：为什么"让模型重试"比"自己保留第一个/最后一个"更好？

→ 解析：重复键说明模型对"这个字段该是什么"存在**内部冲突**（两轮生成、思维链里改过主意）。保留最后一个只是碰运气：金额场景下可能取到幻觉值，也可能取到正确值，无法区分。正确做法是把"存在重复键"当作校验失败的一种，把错误信息与原始片段一起回灌，要求模型重新输出**一个**确定值；同时降低温度、缩短输出长度（重复常出现在长输出/截断重试时）。重试仍有重复，就 fail-closed 转人工，而不是替模型做决定。

**追问二**：流式输出（SSE）里怎么避免"拼出重复键"？

→ 解析：流式的 `delta` 是**文本增量**，不是可靠的 JSON 片段边界，累加时如果重连/重试就会把同一段前缀拼两次，产生重复键甚至重复对象。稳妥的做法：① 用服务端的 `response.completed` 事件拿完整对象，流式只用于展示；② 自己维护"已接收字节偏移"，重连时按 id 去重续传；③ 对拼接结果做增量解析（如 `ijson`）并在遇到重复键时立刻中断，而不是等全部结束再 parse；④ 宁可多花一次请求拿完整结果，也不要在文本层面"修补"。
