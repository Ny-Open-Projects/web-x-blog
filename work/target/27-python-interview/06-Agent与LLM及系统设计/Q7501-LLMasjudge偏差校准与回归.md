---
title: [Q7501] LLM-as-judge 的偏差校准与固定集回归
date: 2026-11-18
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7501 · Agent 评估:LLM-as-judge 的偏差校准与固定集回归

> 难度:★★★ | 标签:Agent, 评估, LLM

**问**：我们用 GPT-4 级模型当评委给 Agent 输出打分，但发现评委偏爱长回答、偏爱自家模型风格的输出，分数随版本漂移。judge 的系统性偏差有哪些，怎么校准？怎么保证评估结果随时间可比？

**答**：结论：judge 的四大已知偏差——**位置偏差**（A/B 对比中偏好先出现的答案）、**长度/详尽偏差**（偏爱长而全）、**自我偏好**（偏爱同源模型风格）、**方差漂移**（模型版本/prompt 微调后评分尺度变化）。校准三件套：交换顺序取均值消位置偏差、rubric 锚定分数定义、用人工标注的固定校准集定期测 judge 本身的准确率。可比性靠**固定集回归**：一个冻结的评估集 + 冻结的 judge prompt/版本，任何变更跑同一集合，diff 才有意义。

校准与实战：
- 位置偏差校准：成对比较跑两遍（A先B后、B先A后），结论不一致记平局——这一步能把 judge 与人工一致率提升 5~15 个点。长度偏差用"分数对长度做回归"，若长度解释了大部分方差，说明 rubric 没写清楚质量维度。
- 固定集回归的工程化：评估集版本化（快照+指纹），judge 配置（模型版本、temperature=0、prompt hash）作为评估报告元数据落库；judge 换版本时先在校准集上重跑并出"尺度映射"，旧分数才能跨版本比较。
- 事故复盘：某次升级 judge 模型后所有 Agent 版本的分数普涨 0.6 分，团队误判为效果提升，实为评分尺度变化。修复：judge 变更纳入变更管理（同代码同评审），校准集上旧 judge 与新 judge 的分数 diff > 0.3 即阻断，先出映射再上线。

```python
# 基线:Python 3.10+ 标准库;judge 偏差校准与固定集回归骨架(可运行,judge 为 stub)
import random

def judge_pair(a: str, b: str) -> str:
    """stub judge:真实实现调 LLM,rubric 锚定 1-5 分或 A/B 选择。"""
    return "A" if len(a) >= len(b) else "B"   # 模拟长度偏差

def calibrated_pair(a: str, b: str) -> str:
    """交换顺序双评,不一致记 tie:消除位置偏差(本 stub 无位置偏差但结构完整)。"""
    r1 = judge_pair(a, b)
    r2 = judge_pair(b, a)
    if r1 == r2 == "A":
        return "A"
    if r1 == r2 == "B":
        return "B"
    return r1 if r1 == r2 else "TIE"

def regression_run(fixed_set: list[tuple[str, str]], scores: dict[str, float]) -> float:
    """固定集回归:与上次基线比较平均分漂移。"""
    base = {"task1": 4.2, "task2": 3.8}
    drift = sum(scores.get(t, 0) - base[t] for t in base) / len(base)
    return drift

if __name__ == "__main__":
    print(calibrated_pair("长回答" * 20, "短答"))   # A
    print(regression_run([], {"task1": 4.9, "task2": 4.4}))  # 漂移 +0.65 -> 阻断线
```

**追问**：
- 一层追问：为什么不用人工全量标注代替 judge？——成本：人工标注一条轨迹 5~10 分钟，日 badcase 上千条不可行；正确分工是人工标校准集（几百条，定期刷新），judge 量产，再抽样 5% 人工复核监控 judge 质量衰减。
- 二层追问：judge 的随机性怎么控制？——temperature=0 仍有非确定性（MoE/批处理效应），所以成对比较要 3 取 2 多数表决或报告分数置信区间；评估报告中必须带 judge 配置指纹，否则回归结论不可信。
- 三层追问：rubric 怎么写才不让分数通胀？——锚定式打分：每个分值给 1~2 个标准答案示例（badge），并强制 judge 先输出"依据"再给分（结构化输出约束）；纯开放打分必然通胀。
