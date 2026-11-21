---
title: [Q2582] embedding 归一化的必要性实测:余弦等价归一后点积
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2582 · embedding 归一化的必要性实测:余弦等价归一后点积

> 难度:★★★☆ | 标签:RAG, 嵌入, 向量检索

**问**:为什么向量入库前都要归一化?不归一会怎样,能实测出来吗?

**答**:数学上归一化后的点积严格等于余弦:cos 等于 dot 除以两个模长,模长归一后商恒等于积,这就是所有向量库默认归一的原因。不归一的后果是点积被模长主导:方向完全相同的两个向量,模长翻倍点积翻倍,近正交的向量对也可能因为模长悬殊点积为正,相似度语义整个失真。实测三件事就能讲清:同方向不同模长的对,余弦恒为 1 而点积随模长任意大;归一后模长恒为 1;归一后点积与直接算余弦在浮点误差内相等。另一个实测收获是性能:归一后用内积索引,比原始向量算带除法的余弦快且可走底层加速。归一化是检索正确性的地基,比换模型提升的排序质量便宜得多。

```python
# file: code/06_Agent与LLM及系统设计/q2582_embed_norm.py
"""Q2582 embedding 归一化的必要性实测:余弦等价于归一后的点积。

数学事实:cos(a,b) = dot(norm(a), norm(b));工程后果:检索库若
没归一化,点积被模长主导,方向完全相同的两向量点积可以任意大。
本实验用小向量实测定量关系。
"""
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def normalize(v):
    n = norm(v) or 1.0
    return [x / n for x in v]


def cosine_raw(a, b):
    return dot(a, b) / (norm(a) * norm(b))


def main():
    a = [3.0, 4.0]
    b = [6.0, 8.0]      # 与 a 同方向,模长翻倍
    c = [-0.8, 0.6]     # 与 a 近似正交
    assert abs(cosine_raw(a, b) - 1.0) < 1e-12          # 方向完全相同
    assert abs(dot(normalize(a), normalize(b)) - cosine_raw(a, b)) < 1e-12
    assert abs(norm(normalize(a)) - 1.0) < 1e-12        # 归一后模长恒为 1
    raw_same = dot(a, b)          # 未归一点积:被模长放大
    raw_ortho = dot(a, c)         # 未归一点积:近正交仍可能为正
    assert abs(raw_same - 50.0) < 1e-12
    assert raw_ortho < 0.5 and cosine_raw(a, c) < 0.1
    print("dot a b =", raw_same, "但真实余弦 = 1.0,点积虚高 50 倍")
    print("dot a c =", round(raw_ortho, 4), "而余弦 =", round(cosine_raw(a, c), 4))
    print("结论:入库前统一归一化,点积才严格等价余弦。")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:所有嵌入模型都建议归一吗?答:绝大多数;个别模型输出本身在单位球上,归一不改变结果,统一做也无害。
- 追问二:混合检索里稀疏稠密分数怎么可比?答:各自归一到可比分位再融合,归一的思想从向量层一路用到分数融合层。
