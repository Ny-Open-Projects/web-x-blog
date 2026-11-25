---
title: "[Q7713] LLM 的 JSON 修复链与降级边界"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7713 · LLM 的 JSON 修复链与降级边界

难度：P6 ｜ 标签：结构化输出、JSON 修复、schema 校验、降级

基线：Python 3.12；标准库 json/ast/re；结构化输出 API 为对照。

**问**：让模型输出 JSON，线上偶发解析失败：有时包了 json 代码围栏，有时带尾逗号，有时用单引号，还有一次输出到一半被 `max_tokens` 截断。团队写了"无限重试直到解析成功"的循环，结果高峰期重试把配额打满。JSON 修复应该修到什么程度、什么时候必须放弃？

**答**：
- **结论**：修复要分级、有界、可观测。**Level 0**：剥掉代码围栏、前后解释性文字，取第一个 `{` 到最后一个 `}`；**Level 1**：去尾逗号、把单引号/`True/False/None` 归一（可用 `ast.literal_eval` 兜底）；**Level 2**：括号不闭合时按栈补齐（仅限截断场景）；**Level 3**：以上都失败 → 带错误信息重试一次（修复提示），仍失败则降级到"人工/默认值/纯文本模式"。**不要无限重试**：修复失败往往意味着模型没按 schema 生成，重试只会重复消耗。
- **取舍**：宽松修复能提升解析成功率，但会掩盖模型的结构性错误（比如把字段名改错、类型写错），修复后的对象可能"能解析但语义错"。严格模式（供应商的 structured outputs / JSON Schema）在生成侧约束，解析几乎不会失败，但受 schema 子集限制、可能增加延迟。生产建议：能用严格模式就用；否则修复链 + schema 校验 + 有界重试。
- **实战**：① 修复后必须跑 **schema 校验**（字段、类型、枚举、必填），不能只看 `json.loads` 成功；② 每次修复记录 level 与原始片段，按 level 统计，Level 2 多说明 `max_tokens` 不足；③ 重试上限 1-2 次并计入总预算；④ 降级路径要明确：返回默认结构、转人工、或向前端返回可读错误。

```python
import ast
import json
import re


def strip_fence(text: str) -> str:
    start, end = text.find("{"), text.rfind("}")
    return text[start:end + 1] if start >= 0 and end > start else text


def repair(raw: str) -> tuple[dict | None, str]:
    text = strip_fence(raw)
    for level, candidate in (
        ("L0", text),
        ("L1", re.sub(r",\s*([}\]])", r"\1", text)),
        ("L1", re.sub(r"'([^']*)'", r'"\1"', text)),
    ):
        try:
            obj = json.loads(candidate)
            return obj, level
        except json.JSONDecodeError:
            continue
    try:
        obj = ast.literal_eval(text)          # 单引号/True/None 兜底
        if isinstance(obj, dict):
            return obj, "L1-ast"
    except (ValueError, SyntaxError):
        pass
    return None, "GIVE_UP"


if __name__ == "__main__":
    fence = chr(96) * 3
    samples = [
        fence + 'json\n{"name": "退款", "days": 7}\n' + fence,
        '{"name": "退款", "days": 7,}',
        "{'name': '退款', 'days': 7}",
        '{"name": "退款", "days": ',
    ]
    for s in samples:
        obj, level = repair(s)
        print(level, obj)
    print("结论：修复有边界，截断类需要补括号或直接重试/降级")
```

**追问一**：为什么 `json.loads` 成功不代表可以安全使用？
→ 解析：JSON 语法正确只保证结构合法，不保证字段存在、类型正确、枚举合法、数值范围合理。业务层必须做 schema 校验（Pydantic/JSON Schema），否则 `{"days": "七天"}` 也能解析，却会在下游炸掉。

**追问二**：`max_tokens` 截断导致的 JSON 不闭合，应该修复还是重试？
→ 解析：补齐括号只能救"只差最后几个字符"的情况，且可能补出一个语义不完整的对象（比如数组只写了一半）。更稳的是识别 `finish_reason=length` 后直接重试并提高 `max_tokens`，或让模型输出更短的结构；把截断当成"修复"会掩盖长度预算不足。
