---
title: [Q7606] 结构化输出 API 演进 JSON mode 到 schema 约束
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7606 · 结构化输出 API 演进：JSON mode 到 schema 约束解码

难度：P6 ｜ 标签：结构化输出 / JSON / 版本演进

**问**：团队三年前的代码用"prompt 里求模型输出 JSON + 正则提取"，后来演进到 JSON mode，再到现在的 structured outputs（schema 约束解码）。这三代的差别是什么？schema 约束解码为什么能"保证"合法 JSON，它又解决不了什么问题？

**答**：
- **结论**：三代演进：① prompt 工程 + 正则——纯祈祷，失败率随输出长度上升，截断即残废；② JSON mode——API 层约束输出是合法 JSON，但不保证符合任何 schema，字段名/类型仍靠模型自觉；③ structured outputs——schema 作为约束解码（constrained decoding）条件传入，解码器在每一步 token 采样时把不满足 schema 的候选 mask 掉（如该出 `"name":` 的位置只允许特定 token），可从机制上保证语法与结构合法。约束解码解决不了的是**语义正确性**：类型对了、值可以是幻觉（编造的 ID、错误的数值、字段语义张冠李戴）；还有约束的反作用——过度严格的 schema（required 全开、枚举过窄）会让模型被逼着填垃圾值，质量反而下降。
- **取舍**：schema 设计的松紧交换：required 字段越多，模型被迫编造的概率越高——把"可能不知道"的字段设为 optional 并在 prompt 里授权 null；枚举值过窄会把模糊现实硬塞进错误桶。性能代价：约束解码每步做 mask 有开销（供应商侧承担），且部分供应商在 schema 复杂（深嵌套/长枚举）时拒绝或限长——复杂 schema 要拆多步工具调用而不是一个巨型 schema。Python 侧配套：Pydantic v2 的 `model_json_schema()` 生成 schema + `model_validate_json()` 校验是标准管线（基线 Pydantic 2.x / Python 3.9+），校验失败重试要带上次错误信息（self-heal）。
- **实战**：步骤：① 迁移顺序：先 JSON mode（改造成本低）→ 评估失败率 → 高价值路径上 structured outputs；② schema 版本化管理（字段演进要向后兼容，旧记录要能被新 schema 读）；③ 校验失败率做指标，>2% 触发 schema/模型复审；④ 复盘项：semantic 抽查抽样人工 review——语法合法不等于内容正确，这一层只有评测集与抽检能兜。

```python
# 结构化输出管线：schema 生成 + 校验 + 自愈重试（基线 Pydantic 2.x）
# 基线：Python 3.9+ / Pydantic 2.x；缺库自动降级为手写校验演示

from typing import Literal, Optional

try:
    from pydantic import BaseModel, ValidationError
    HAVE_PYDANTIC = True
except ImportError:
    HAVE_PYDANTIC = False


if HAVE_PYDANTIC:
    class Ticket(BaseModel):
        id: str
        priority: Literal["low", "normal", "high"] = "normal"
        estimate_hours: Optional[float] = None  # 允许"不知道" -> None


def fake_model_output(bad: bool) -> str:
    if bad:
        return '{"id": "T-1", "priority": "URGENT", "estimate_hours": "3天"}'
    return '{"id": "T-1", "priority": "high", "estimate_hours": 3.5}'


def pipeline(raw: str, max_retry: int = 1) -> dict:
    """校验失败 -> 把错误信息喂回模型（自愈）重试一次"""
    for attempt in range(max_retry + 1):
        try:
            return Ticket.model_validate_json(raw).model_dump()
        except ValidationError as e:
            if attempt == max_retry:
                raise
            # 真实场景: 将 e.errors() 摘要拼进下一次 prompt
            raw = fake_model_output(bad=False)
    raise RuntimeError


def main() -> None:
    if not HAVE_PYDANTIC:
        print("pydantic 未安装，降级演示仅打印 schema 意图")
        return
    out = pipeline(fake_model_output(bad=True))
    print(out)
    assert out["estimate_hours"] == 3.5
    try:
        Ticket.model_validate_json('{"id": "T-2", "priority": "weird"}')
        raise AssertionError("should fail")   # Literal 枚举外的值
    except ValidationError:
        pass
    print("OK: 校验失败自愈重试一次即恢复")


if __name__ == "__main__":
    main()
```

**追问 1**：约束解码的 token mask 机制为什么强于"生成后校验重试"？
→ 一句话提示：mask 在采样时排除非法 token，从生成过程根除语法错误，重试的期望次数为 1（零浪费）；后校验重试期望多付整次生成成本且不保证收敛，二者成本差随输出长度放大。

**追问 2**：schema 版本演进时，存量数据与新 schema 的兼容怎么处理？
→ 一句话提示：只增不改不删（新增字段 optional + 默认值），读侧用宽容解析（未知字段忽略、缺失字段默认），加 schema_version 字段；破坏性变更走新版本字段 + 双读迁移，与 API 版本化同一套纪律。

## 背诵要点
- 三代演进：prompt+正则（祈祷）→ JSON mode（语法合法）→ structured outputs（schema 约束解码，机制保证结构）。
- 约束解码保证语法不保证语义：幻觉值、语义错位仍需评测与抽检；required 过多逼模型编造，"不知道"字段设 optional+null。
- 管线标准件：Pydantic v2 model_json_schema 生成 + model_validate_json 校验 + 失败信息回喂自愈重试；校验失败率 >2% 复审。

## 复盘追问
- 为什么巨型嵌套 schema 常被供应商拒绝或限长？提示：约束解码要为整个 schema 构建语法掩码，复杂度随嵌套与枚举规模爆炸，供应商用 schema 大小限制保护自身延迟；拆成多次小 schema 的工具调用链是标准解法。
- 从 JSON mode 升到 structured outputs 有什么"静默收益/静默代价"？提示：收益是失败率下降不再被监控发现（没人注意重试消失）；代价是模型自由度下降，某些开放式任务质量可能变差——切换要跑任务级 A/B 而不是只看 JSON 解析成功率。
