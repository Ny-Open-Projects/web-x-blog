---
title: "[Q7707] strict 模式结构化输出的 schema 子集限制"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7707 · strict 模式结构化输出的 schema 子集限制

难度：P6 ｜ 标签：版本迁移破坏点、结构化输出、strict、schema

基线：Python 3.12；OpenAI structured outputs（strict=true）；json 标准库演示。

**问**：把结构化输出切到 `strict: true` 后，原本能用的 schema 突然被接口拒绝，报"unsupported keyword"。strict 不是"更严格地遵守 schema"吗？为什么会拒绝合法 JSON Schema？

**答**：
- **结论**：`strict: true` 启用的是**约束解码**，要求 schema 必须是解码器能编译成有限状态约束的**子集**，而不是完整 JSON Schema。被拒的常见原因：`additionalProperties` 的某些用法、正则 `pattern`、递归 `$ref`、某些 `oneOf`/`anyOf` 组合、`minimum`/`maximum` 等数值约束——这些语义无法在 token 级解码时高效强制。所以要改写 schema（如把 `pattern` 改成枚举、把递归展开为有限深度）才能用。它保证的是"输出 100% 符合这个受限 schema"，代价是表达力下降。
- **取舍**：strict 大幅减少"输出不合格式"的重试，适合字段固定、类型明确的结构化抽取；复杂/动态结构要么降级到非 strict（靠提示 + 校验重试），要么重构 schema 适配子集。还要注意 strict 下 `required` 必须包含所有属性（不允许可选字段缺失），这与旧习惯不同。
- **实战**：迁移时先用 schema 校验器跑一遍子集检查；把 `pattern`/数值范围等约束移到**下游业务校验层**；对必填字段全部列入 required；保留一个非 strict 的降级路径作为兜底，并监控 schema 被拒的次数。

```python
UNSUPPORTED = {"pattern", "minimum", "maximum"}


def check_strict_schema(schema: dict) -> list[str]:
    """模拟 strict 子集校验：列出解码器不支持的关键字。"""
    bad = []
    for key in schema:
        if key in UNSUPPORTED:
            bad.append(key)
    props = schema.get("properties", {})
    for name, sub in props.items():
        if isinstance(sub, dict):
            bad += [f"{name}.{k}" for k in sub if k in UNSUPPORTED]
    return bad


if __name__ == "__main__":
    schema = {
        "type": "object",
        "properties": {"code": {"type": "string", "pattern": "^[A-Z]{3}$"}},
        "required": ["code"],
    }
    problem = check_strict_schema(schema)
    print("strict 不支持:", problem)
    print("改法: 把 pattern 移到下游校验，schema 用枚举或纯 string")
```

**追问一**：strict 模式为什么要求所有属性都在 required 里？
→ 解析：约束解码器需要为每个位置确定性地生成合法 token，"字段可缺省"会让状态机分支难以在解码层表达；所以 strict 下对象属性要求全部必填，可选语义用 `null` 类型表达。

**追问二**：`pattern`/`minimum` 这类约束被拒后，怎么保证业务规则仍被满足？
→ 解析：把它们移到解码后的业务校验层——strict 保证结构和类型合法，业务层再校验格式和范围，不合法则触发有限次重试或降级。约束解码与业务校验是两层，不要混为一谈。
