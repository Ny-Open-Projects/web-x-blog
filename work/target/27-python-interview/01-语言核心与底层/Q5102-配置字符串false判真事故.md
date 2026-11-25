---
title: [Q5102] 配置字符串 false 判真事故复盘
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题

**问**:环境变量 `FEATURE_NEW=false`，代码里 `if flag:` 却走了新逻辑，为什么？

**答**:结论：环境变量永远是字符串，非空字符串恒为真——`bool("false")` 是 `True`。这是"类型边界"事故：入口处（env/CLI/HTTP query）都是文本，业务层却按布尔消费。取舍：不要散落各处手写 `== "true"`，收敛到一个 parse 函数；能用 tomllib/json 等结构化配置时优先结构化（配合 Q5107 tomllib）。实战上要约定显式真值表（如 `1/true/yes/on` 大小写不敏感），并在解析失败时 fail-fast 而不是静默判假——静默判假会把"配置写错"伪装成"功能关闭"。

```python
def parse_bool(raw: str | None, *, default: bool, name: str = "?") -> bool:
    if raw is None or raw == "":
        return default
    low = raw.strip().lower()
    if low in {"1", "true", "yes", "on"}:
        return True
    if low in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"{name}={raw!r} 不是合法布尔")   # fail-fast，不静默

import os
os.environ["FEATURE_NEW"] = "false"
print(bool(os.environ["FEATURE_NEW"]))        # True   —— 事故现场
print(parse_bool(os.environ["FEATURE_NEW"], default=False, name="FEATURE_NEW"))  # False
try:
    parse_bool("2", default=False, name="X")
except ValueError as e:
    print(e)
```

**追问一层**:`if flag:` 与 `if flag is True:` 的区别？后者在 `flag="false"` 时的行为？
**追二层**:HTTP 查询串 `?debug=0` 经框架解析后拿到什么类型？为什么 FastAPI 用类型注解能解掉这类事故？

**背诵要点**
- 非空字符串恒为真，`bool("false")` 是 True。
- 类型边界处必须显式解析：真值表 + 未知值 fail-fast。
- 结构化配置（toml/json）从根上消灭字符串布尔。

**复盘追问**
- 前端把布尔序列化成字符串再回传，这个坑如何在序列化层拦掉？提示：Pydantic 严格模式。
- 开关默认值应该是 True 还是 False？提示：结合"未配置"与"配置为空"的语义差。
