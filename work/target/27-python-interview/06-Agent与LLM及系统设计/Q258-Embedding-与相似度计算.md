---
title: [Q258] Embedding 与相似度计算
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q258 · Embedding 与相似度计算

> 难度:★★★ | 标签:RAG, Embedding

**问**:Embedding 是什么?cosine 和内积、欧氏距离怎么选?为什么检索要用 ANN?

**答**:Embedding 把文本映射为高维向量,语义相近的文本向量距离更近,它是 RAG 检索的基石。相似度选择:cosine 归一化方向差异,适合文本语义;内积在向量已归一化时与 cosine 等价且算得更快,是向量库默认;欧氏距离在高维文本上很少用。ANN(近似最近邻,如 HNSW、IVF)是因为暴力比对 O(N) 在千万级向量下不可接受,ANN 用图/量化索引换取亚线性查询,代价是有极小的召回损失。

```python
# file: code/06_Agent与LLM及系统设计/q258_embedding_sim.py
"""实现 cosine、内积、欧氏距离并对比;演示归一化后内积等于 cosine。"""
import math


def cosine(a: list[float], b: list[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    return num / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def euclid(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def normalize(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


if __name__ == "__main__":
    q = [1.0, 2.0, 3.0]
    good = [1.2, 2.1, 2.9]   # 语义相近
    bad = [3.0, 1.0, 0.5]    # 语义无关
    for name, fn in [("cosine", cosine), ("inner", inner), ("euclid", euclid)]:
        print(f"{name}: 相关={fn(q, good):.3f} 无关={fn(q, bad):.3f}")
    print("归一化后 inner(q,good) =", round(inner(normalize(q), normalize(good)), 3),
          "== cosine:", round(cosine(q, good), 3))
```

**追问**:
- 不同模型的 embedding 能混用吗?绝对不能,不同模型的向量空间不兼容,必须同一模型生成库内向量和 query 向量。
- 为什么向量要归一化?——归一化后内积=cosine 且计算快,向量库默认按此优化;混用未归一化向量会让排序失真。
- HNSW 的参数怎么权衡?——M/ef_construction 影响构建(内存、时间),ef_search 影响查询召回与延迟;按评估集调参而非默认值。
- embedding 维度越高越好吗?——表征更细但存储/计算成本线性上涨;选模型主要看领域适配与榜单召回,不是维度。
