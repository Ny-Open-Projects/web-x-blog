---
title: "[Q7702] logprobs 置信度校准与低置信拒答"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7702 · logprobs 置信度校准与低置信拒答

难度：P7 ｜ 标签：事故复盘、可靠性、logprobs、置信度校准

基线：Python 3.12；LLM logprobs 字段；math 标准库演示概率与校准。

**问**：想用模型返回的 `logprobs` 做"低置信就拒答/转人工"，直接把 token 的对数概率平均一下当置信度，上线后发现该拒的没拒、不该拒的乱拒。问题出在哪？

**答**：
- **结论**：logprobs 是**token 级**的对数概率，把整句 token 的 logprob 简单平均既不是句子级置信度，也不是"答案正确性"概率。几个坑：(1) 长句子 token 多，平均会被大量高概率虚词/标点稀释，看起来"很自信"；(2) 采样（temperature/top_p）会改变概率分布，logprob 反映的是采样后分布，不等于模型对事实的确信；(3) **校准问题**——现代 LLM 常过度自信，logprob 高不代表答案对，直接当 0~1 概率用会系统性偏差。正确用法是把它当**相对信号**：用答案 token 的平均 logprob 或序列联合概率做阈值，但要在本任务标注数据上标定阈值（画出置信-正确率曲线，即可靠性图/ECE）。
- **取舍**：logprobs 成本低（随响应返回），适合做粗粒度路由（高置信直接答、低置信走 RAG 复核或人工）；关键决策不要单靠它，结合自洽性（multiple sampling 一致性）、外部验证。
- **实战**：按任务分别标定阈值，不要跨任务复用；用 ECE（expected calibration error）度量校准程度；把 logprobs 与拒答率/准确率一起监控，阈值漂移要报警。

```python
import math


def mean_logprob_conf(logprobs: list[float]) -> float:
    """token logprob 均值 -> 0~1 的粗略置信信号（需按任务标定，非真实概率）。"""
    if not logprobs:
        return 0.0
    avg = sum(logprobs) / len(logprobs)
    return math.exp(avg)  # 几何平均概率


if __name__ == "__main__":
    confident = [-0.05, -0.08, -0.03, -0.06]   # 每 token 概率约 0.95
    unsure = [-1.2, -0.9, -2.0, -1.5]
    print("高置信信号:", round(mean_logprob_conf(confident), 3))
    print("低置信信号:", round(mean_logprob_conf(unsure), 3))
    # 注意：这只是相对信号，阈值必须在标注数据上标定后才能用于拒答。
```

**追问一**：为什么采样参数（temperature/top_p）会影响 logprobs 的含义？
→ 解析：logprob 是在采样后（经 temperature 缩放、top_p 截断）的分布上算的。temperature 越高分布越平，logprob 越低，但答案未必更错；因此不同采样配置下的 logprob 阈值不可直接比较。

**追问二**：什么是校准（calibration），怎么衡量？
→ 解析：校准指"模型说 0.8 置信时，实际约 80% 正确"。用可靠性图（分桶看置信与准确率）和 ECE（各桶 |置信-准确率| 的加权平均）衡量。LLM 常过度自信，需在具体任务上重新标定。
