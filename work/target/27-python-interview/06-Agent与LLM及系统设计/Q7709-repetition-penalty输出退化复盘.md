---
title: "[Q7709] repetition_penalty 与输出退化事故复盘"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7709 · repetition_penalty 与输出退化事故复盘

难度：P6 ｜ 标签：事故复盘、解码参数、repetition_penalty、输出质量

基线：Python 3.12；纯 Python 演示重复惩罚对词概率的重排。

**问**：客服 Agent 上线后出现一种怪现象：遇到不确定的问题，回答会陷入循环，反复出现同一句话；开发把 `repetition_penalty` 从 1.0 调到 1.5，结果代码类回答里正常的 `if`、`return` 等高频词被过度惩罚，输出变得语法混乱。为什么调个惩罚因子会两头出问题？怎么治理？

**答**：
- **结论**：`repetition_penalty`（及 frequency/presence penalty）通过降低**已出现 token** 的概率来抑制循环重复，但它是"全局机械降权"：不区分这个词是"无意义的复读"还是"代码/术语里本就该高频出现的 legit token"。惩罚太大（1.5）会把合法高频词压垮，破坏语法和领域正确性；惩罚太小（1.0）又压不住真正的循环。而且它和 temperature/top_p 叠加时效果非线性，容易顾此失彼。
- **取舍**：重复治理有多层手段——根本上用更好的提示与上下文管理避免模型进入循环；用 `presence_penalty`/`frequency_penalty`（按"是否出现过/出现频率"惩罚，更温和）替代粗暴的 repetition_penalty；检测到输出陷入循环时**截断 + 重试**比调大惩罚更可控；代码/结构化输出任务应尽量关闭这类惩罚。
- **实战**：按任务分配置——对话可小幅惩罚，代码/JSON 任务关闭；设置重复检测（n-gram 重复率超阈值触发重试/降级）；把解码参数纳入版本管理，参数变更走回归评测；监控输出的重复率与"卡顿循环"率作为质量指标。

```python
def apply_repetition_penalty(
    probs: dict[str, float], seen: set[str], penalty: float
) -> dict[str, float]:
    """只对已出现过的 token 降权后重新归一化（penalty=1.0 不惩罚）。"""
    adjusted = {t: (p / penalty if t in seen else p) for t, p in probs.items()}
    total = sum(adjusted.values())
    return {t: v / total for t, v in adjusted.items()}


if __name__ == "__main__":
    probs = {"if": 0.5, "return": 0.3, "x": 0.2}
    print("无惩罚:", probs)
    penalized = apply_repetition_penalty(probs, seen={"if"}, penalty=1.5)
    print("惩罚已出现的 if 后:", {k: round(v, 3) for k, v in penalized.items()})
    # if 概率被压低、其余升高：合法高频词被误伤 -> 代码类任务应关闭该惩罚。
```

**追问一**：repetition_penalty 和 presence/frequency_penalty 有什么区别？
→ 解析：repetition_penalty 对已出现的每个 token 乘一个固定惩罚（出现次数越多累积越强）；presence_penalty 只要 token 出现过就惩罚一次、与次数无关；frequency_penalty 按出现次数线性惩罚。后两者更温和、可控，通常优先选它们。

**追问二**：为什么检测到循环用"截断重试"比调大惩罚更好？
→ 解析：调大惩罚是全局手段，会误伤合法输出且效果非线性；截断重试是针对已发生的循环做局部干预——检测到重复模式就停并重新生成（可换采样参数），影响范围可控、可观测，配合重试次数上限即可。
