---
title: [Q7004] property-based testing(hypothesis)在序列化层的落地
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7004 · property-based testing(hypothesis)在序列化层的落地

> 难度:★★★ | 标签:测试, hypothesis, 质量

**问**：我们序列化层（Pydantic v2 模型 ↔ JSON ↔ DB 行）只写了十几条手写用例，线上出过 Unicode 边界和浮点精度 bug。用 hypothesis 做属性测试，该定义哪些"性质"？怎么避免它跑出不可复现的随机失败？

**答**：结论：序列化层的核心性质就三条——**round-trip（encode∘decode = identity）、不变式（输出满足 schema/长度/类型约束）、monotonic 资源（输出尺寸有上界）**。手写用例测的是"作者想到的点"，hypothesis 用策略生成器系统性地覆盖"作者没想到的点"（NUL 字符、代理对、-0.0、超大整数、前后导空格）。可复现靠 hypothesis 内置的数据库机制：失败案例自动存储并在后续运行重放，CI 里再固定 `derandomize=True`。

落地取舍：
- 策略设计是关键：`st.from_type(MyModel)` 自动从 Pydantic 模型生成（hypothesis 有 pydantic 插件支持），但默认策略会生成无意义字符串，要 `@given` 里显式 `st.text(min_size=1, max_size=64)` 约束到真实业务域，否则失败全是"垃圾输入被正确拒绝"的噪音。
- 成本控制：`max_examples` 默认 100，CI 用 50~100，夜间全量跑 1000+；健康检查 `@settings(suppress_health_check=[HealthCheck.too_slow])` 慎用，先修策略生成慢的问题。
- 事故复盘：round-trip 测试抓到 `json.dumps` 对 `float('inf')` 产出 `Infinity`（非标准 JSON），下游 Go 服务解析失败。修复：schema 层禁止非有限浮点（Pydantic `allow_inf_nan=False`），并把这条性质写成不变式测试固化。

```python
# 基线:Python 3.10+ / hypothesis 6+ / pydantic 2.x;缺库降级:核心性质用标准库演示
try:
    from hypothesis import given, settings, strategies as st
    HAS_HYP = True
except ImportError:
    HAS_HYP = False

def encode(items: list[dict]) -> bytes:
    import json
    return json.dumps(items, ensure_ascii=True, allow_nan=False).encode()

def decode(data: bytes) -> list[dict]:
    import json
    return json.loads(data.decode())

def check_roundtrip(items: list[dict]) -> bool:
    """核心性质:encode∘decode == identity。"""
    return decode(encode(items)) == items

if HAS_HYP:
    items_st = st.lists(st.fixed_dictionaries(
        {"name": st.text(min_size=1, max_size=64),
         "qty": st.integers(min_value=0, max_value=10**9)}),
        max_size=20)

    @given(items_st)
    @settings(max_examples=200, derandomize=True)   # CI 可复现
    def test_roundtrip(items):                      # type: ignore[misc]
        assert check_roundtrip(items)

if __name__ == "__main__":
    demo = [{"name": "a\x00b", "qty": 5}]
    print("roundtrip ok:", check_roundtrip(demo))
    if HAS_HYP:
        test_roundtrip()
        print("hypothesis 200 例通过")
```

**追问**：
- 一层追问：round-trip 什么时候"identity"不成立但代码是对的？——信息有损的序列化（浮点精度、时区归一、去重语义）：性质要改写为"语义等价"（规范化后再比较），或限定输入策略到无歧义子集。分清"bug"与"约定"是设计性质的第一步。
- 二层追问：hypothesis 找到反例后怎么处理 shrink 结果？——它会自动最小化到最小反例并持久化（`.hypothesis/examples` 目录），修复前每次运行都会重放；把最小反例固化成一条显式回归用例进单测，防止未来删掉 hypothesis 依赖后丢失。
- 三层追问：和 fuzzing（如 atheris）的分工？——hypothesis 是结构化、性质驱动的（测正确性），fuzz 是无结构覆盖率驱动的（测崩溃/安全）；序列化层通常 hypothesis 为主，入口边界解析再叠一层 fuzz。
