---
title: [Q2305] 多路召回的分数归一:min-max 与 z 分数融合
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2305 · 多路召回的分数归一:min-max 与 z 分数融合

> 难度:★★★★ | 标签:RAG, 融合, 检索

**问**:BM25 分数动辄十几二十,向量相似度只有零点几,两路结果怎么合一个排名?直接相加行不行?

**答**:直接相加是经典错误:量纲差一个数量级,词面分完全淹没语义分,排序等于只看 BM25。正确做法是先各自归一再加权:min-max 把每路分数拉到零一区间,简单直观但对离群分敏感;z-score 减均值除标准差,对分布更稳,适合分数分布未知的路。归一后按可调权重线性融合,权重就是两路的"话语权",由评估集调出。要处理退化情况:某一路内所有分数相等时无区分度,归一应退化为中性分而不是除零报错。若两路分数分布极端偏斜,还可以退到 RRF 只用排名不算分——Q1190 的方案,这里是分数版对偶。

```python
# file: code/06_Agent与LLM及系统设计/q2305_score_normalization.py
"""多路召回融合:两路分数量纲不同,先各自归一再加权融合,量纲直加是经典错误。"""


def minmax(scores):
    lo, hi = min(scores), max(scores)
    if hi == lo:
        return [0.5] * len(scores)
    return [(s - lo) / (hi - lo) for s in scores]


def zscore(scores):
    n = len(scores)
    mean = sum(scores) / n
    var = sum((s - mean) ** 2 for s in scores) / n
    std = var ** 0.5 or 1.0
    return [(s - mean) / std for s in scores]


def fuse(bm25, vec, w=(0.4, 0.6), method="minmax"):
    norm = minmax if method == "minmax" else zscore
    a, b = norm(bm25), norm(vec)
    return [round(w[0] * x + w[1] * y, 4) for x, y in zip(a, b)]


if __name__ == "__main__":
    ids = ["d0 双路都好", "d1 只有词面", "d2 只有语义"]
    bm25 = [18.0, 19.0, 2.0]
    vec = [0.90, 0.10, 0.95]
    naive = [round(a + b, 3) for a, b in zip(bm25, vec)]
    assert ids[max(range(3), key=lambda i: naive[i])] == "d1 只有词面", "量纲直加被词面分淹没"
    fused = fuse(bm25, vec)
    order = [ids[i] for i in sorted(range(3), key=lambda i: -fused[i])]
    assert order[0] == "d0 双路都好", "归一后融合 双好文档登顶"
    assert fused[2] > fused[1], "语义强于纯词面命中"
    fused_z = fuse(bm25, vec, method="z")
    assert [ids[i] for i in sorted(range(3), key=lambda i: -fused_z[i])][0] == "d0 双路都好"
    flat = fuse([5.0, 5.0], [0.3, 0.3])
    assert flat == [0.5, 0.5], "单一路内无区分度时归一退化为中性分"
    print("分数归一通过:量纲问题复现 min-max 与 z 分数融合 等值退化")
```

**追问**:
- 归一在候选并集上做还是每路独立做? 答:每路独立做,归一目的是路内可比,跨路比较交给融合权重
- 上线前怎么定权重? 答:评估集网格搜索少量取值,看命中率与 MRR,权重进配置可热更
