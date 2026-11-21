---
title: [Q1142] JSON Schema 约束解码的概念与校验桩
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1142 · JSON Schema 约束解码的概念与校验桩

> 难度:★★★★ | 标签:结构化输出, 解码

**问**:怎么让模型 100% 输出合法 JSON?约束解码是什么原理?

**答**:约束解码(constrained decoding)在推理时把 JSON schema 编译成语法状态机,每步生成只在"合法 token 子集"内采样,从根上保证语法合法。工程上即便没有约束解码支持,也要在客户端做三层校验:语法层 `json.loads`、schema 层(类型/必填/枚举/范围)、语义层(业务规则如"结束日期晚于开始日期")。下面的校验桩演示 schema 层,它是重试与修复策略的判据。

```python
# file: code/06_Agent与LLM及系统设计/q1142_schema_validator.py
"""JSON Schema 校验桩:支持 type/required/enum/minimum,供结构化输出管线判据使用。"""


def validate(obj, schema, path="$"):
    errors = []
    t = schema.get("type")
    type_ok = {
        "object": lambda x: isinstance(x, dict),
        "string": lambda x: isinstance(x, str),
        "integer": lambda x: isinstance(x, int) and not isinstance(x, bool),
        "number": lambda x: isinstance(x, (int, float)) and not isinstance(x, bool),
    }.get(t, lambda x: True)(obj)
    if not type_ok:
        return [f"{path}: 期望 {t} 实际 {type(obj).__name__}"]
    if t == "object":
        for k in schema.get("required", []):
            if k not in obj:
                errors.append(f"{path}.{k}: 必填缺失")
        for k, sub in schema.get("properties", {}).items():
            if k in obj:
                errors += validate(obj[k], sub, f"{path}.{k}")
    if "enum" in schema and obj not in schema["enum"]:
        errors.append(f"{path}: {obj!r} 不在枚举 {schema['enum']}")
    if "minimum" in schema and isinstance(obj, (int, float)) and obj < schema["minimum"]:
        errors.append(f"{path}: {obj} 小于下限 {schema['minimum']}")
    return errors


SCHEMA = {
    "type": "object",
    "required": ["city", "days"],
    "properties": {
        "city": {"type": "string"},
        "days": {"type": "integer", "minimum": 1},
        "grade": {"type": "string", "enum": ["low", "mid", "high"]},
    },
}


class FakeLLM:
    def __init__(self, outputs):
        self.outputs = iter(outputs)

    def generate(self, prompt):
        return next(self.outputs)


if __name__ == "__main__":
    cases = [
        ('{"city": "北京", "days": 3, "grade": "high"}', []),
        ('{"city": "北京", "days": 0}', ["$.days: 0 小于下限 1", "$.grade: 必填缺失"]),
        ('{"city": 123, "days": 2, "grade": "bad"}', []),
    ]
    import json
    for raw, _ in cases:
        errs = validate(json.loads(raw), SCHEMA)
        print(f"{raw[:34]:<36} -> {errs or '合法'}")
    assert validate({"city": "北京", "days": 3, "grade": "high"}, SCHEMA) == []
    assert len(validate({"city": 123, "days": 2, "grade": "bad"}, SCHEMA)) >= 2
    print("schema 校验桩通过")
```

**追问**:
- 约束解码为什么不能保证语义正确?答:它只约束语法与 schema 形状,值仍可以是错的,"days=999" 语法合法但业务非法,所以语义校验不可省。
- 枚举很多时状态机会膨胀怎么办?答:大枚举用 trie 前缀剪枝或先约束外层结构、枚举值改后置校验重试,兼顾性能与正确率。
