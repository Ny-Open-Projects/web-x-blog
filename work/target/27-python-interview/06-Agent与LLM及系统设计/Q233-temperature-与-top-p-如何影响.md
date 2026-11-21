---
title: [Q233] temperature 与 top_p 如何影响生成
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q233 · temperature 与 top_p 如何影响生成

> 难度:★★ | 标签:Agent, 采样

**问**:面试常问 temperature 和 top_p 的区别,以及任务中该各自取什么值?

**答**:两者都是控制采样随机性的手段:temperature 对 logits 做缩放,越低分布越尖锐、输出越确定;top_p(nucleus sampling)只在累积概率前 p 的候选里采样,动态截断长尾。调参时一般只调其中一个。经验值:分类/抽取/SQL/代码≈0-0.3,常规对话≈0.7,创意写作≈0.9+。Agent 里做工具决策的步骤建议低温,保证行为可复现。

```python
# file: code/06_Agent与LLM及系统设计/q233_sampling.py
"""用纯标准库演示 temperature 缩放与 top_p 截断对采样分布的影响。"""
import random

LOGITS = {"北京": 4.0, "上海": 3.0, "广州": 1.5, "乌鲁木齐": 0.1}


def softmax_temp(logits: dict, temp: float) -> dict:
    scaled = {k: v / temp for k, v in logits.items()}
    m = max(scaled.values())
    exp = {k: 2.718281828 ** (v - m) for k, v in scaled.items()}
    total = sum(exp.values())
    return {k: v / total for k, v in exp.items()}


def sample_top_p(probs: dict, top_p: float) -> str:
    items = sorted(probs.items(), key=lambda x: -x[1])
    kept, acc = [], 0.0
    for k, p in items:
        kept.append((k, p))
        acc += p
        if acc >= top_p:
            break
    total = sum(p for _, p in kept)
    r, cur = random.random() * total, 0.0
    for k, p in kept:
        cur += p
        if r <= cur:
            return k
    return kept[-1][0]


if __name__ == "__main__":
    random.seed(42)
    for t in (0.2, 1.0, 2.0):
        probs = softmax_temp(LOGITS, t)
        picks = [sample_top_p(probs, 1.0) for _ in range(5)]
        print(f"temp={t} 北京概率={probs['北京']:.3f} 采样={picks}")
    low = softmax_temp(LOGITS, 1.0)
    print("top_p=0.6 采样:", [sample_top_p(low, 0.6) for _ in range(5)])
```

**追问**:
- 两者都设 0 就完全确定吗?多数实现下近似确定,但仍受浮点与后端非确定性(如 MoE 路由)影响,不能依赖完全复现。
- temperature=0 为什么仍可能不确定?——浮点并行归约的顺序、MoE 路由、批处理动态性都会引入抖动;工程上要复现就固定种子+单请求。
- top_k 和 top_p 的关系?——都是截断采样:top_k 固定候选数,top_p 按累计概率动态;现代 API 多用 top_p,top_k 作补充。
- 工具决策为什么建议低温?——「调不调、调哪个」需要稳定可复现;温度高会让同一输入产生不同工具序列,评估和调试都困难。
