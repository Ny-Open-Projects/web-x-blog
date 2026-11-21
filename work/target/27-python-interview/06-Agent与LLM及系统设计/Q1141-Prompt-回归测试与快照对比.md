---
title: [Q1141] Prompt 回归测试与快照对比
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1141 · Prompt 回归测试与快照对比

> 难度:★★★★ | 标签:prompt 管理, 测试

**问**:改了 prompt 怎么知道没把别的场景改坏?

**答**:把 prompt 测试做成三层:单测(变量替换正确、约束词存在)、快照测试(固定输入下输出结构指纹对比)、评估集回归(打分不降级)。快照对生成类任务不适用的原因是不确定性,所以快照的是"结构指纹"而非全文:比如输出 JSON 的键集合、必含关键词、长度区间。评估回归必须设门禁:核心指标不低于基线 -2%,新场景指标允许波动但老场景不许崩。

```python
# file: code/06_Agent与LLM及系统设计/q1141_prompt_regression.py
"""Prompt 回归:结构指纹快照 + 评估集打分门禁,新旧版本自动对比。"""


class FakeLLM:
    def __init__(self, behavior):
        self.behavior = behavior

    def generate(self, prompt):
        if "v2" in prompt:  # 模拟新版 prompt 的行为变化
            return '{"answer": "重试后再试", "intent": "售后", "confidence": 0.7}'
        return self.behavior


def fingerprint(output):
    """结构指纹:键集合 + intent 字段值,忽略易变的 confidence 数值。"""
    import json
    obj = json.loads(output)
    return {"keys": sorted(obj.keys()), "intent": obj.get("intent")}


EVAL_SET = [
    ("退货怎么操作", "intent=售后"),
    ("发票怎么开", "intent=售后"),
    ("今天天气如何", "intent=闲聊"),
]


def score(llm):
    ok = 0
    for q, expect in EVAL_SET:
        out = llm.generate(q)
        fp = fingerprint(out)
        want = expect.split("=")[1]
        ok += fp["intent"] == want
    return ok / len(EVAL_SET)


if __name__ == "__main__":
    v1 = FakeLLM('{"answer": "请联系客服", "intent": "售后", "confidence": 0.9}')
    v2 = FakeLLM('{"answer": "重试后再试", "intent": "售后", "confidence": 0.7}')
    base_fp = fingerprint(v1.generate("退货怎么操作"))
    new_fp = fingerprint(v2.generate("退货怎么操作"))
    print("v1 指纹:", base_fp)
    print("v2 指纹:", new_fp)
    assert base_fp["keys"] == new_fp["keys"], "输出 schema 漂移,拒绝上线"
    s1, s2 = score(v1), score(v2)
    print(f"回归分: v1={s1:.0%} v2={s2:.0%}")
    gate = s2 >= s1 - 0.02
    print("门禁结论:", "放行" if gate else "阻断")
    assert gate
```

**追问**:
- 评估集多大才够?答:按场景分层,每层至少 20-50 条覆盖 badcase,总量 200+ 就能拦住大多数回归,贵在持续维护。
- 输出措辞变了但语义没变,快照误报怎么办?答:指纹只取结构语义(键、枚举值、关键词),自由文本不进指纹;语义级等价交给评估集的 LLM-as-Judge。
