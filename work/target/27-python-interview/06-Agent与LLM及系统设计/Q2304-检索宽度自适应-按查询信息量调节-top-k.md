---
title: [Q2304] 检索宽度自适应:按查询信息量调节 top_k
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2304 · 检索宽度自适应:按查询信息量调节 top_k

> 难度:★★★☆ | 标签:RAG, 检索, 成本

**问**:top_k 固定取 5,简单问题浪费生成 token,复杂问题又召不全,有没有办法按查询自动调?

**答**:用查询自身的分布特征估信息量:对分词后的查询算香农熵,词少且集中熵低,说明意图聚焦,用最小 top_k 就够;词多且分散熵高,意图模糊或多主题,自动加宽到最大 top_k 多召回一些,留给重排去筛。宽度必须受预算封顶,再模糊的查询也不能把窗口撑爆。这是个粗粒度启发式,胜在零标注零训练、可解释可配置——工程上比训练一个查询复杂度分类器性价比高得多。上限之外还可以叠加多路召回配额:高熵查询每路多分一点,低熵查询集中预算给单路。

```python
# file: code/06_Agent与LLM及系统设计/q2304_adaptive_topk.py
"""检索宽度自适应:短窄问题用小 top_k,模糊多义问题自动加宽,预算封顶。"""
import math
from collections import Counter


def query_entropy(query_tokens):
    c = Counter(query_tokens)
    total = len(query_tokens)
    ent = 0.0
    for v in c.values():
        p = v / total
        ent -= p * math.log2(p)
    return ent


def pick_topk(query_tokens, k_min=2, k_max=8, cap=6):
    ent = query_entropy(query_tokens)
    if ent <= 1.0:
        k = k_min
    elif ent <= 1.8:
        k = k_min + 2
    else:
        k = k_max
    return min(k, cap), ent


def retrieve(index, query, k):
    return index[:k]


if __name__ == "__main__":
    index = ["d%d" % i for i in range(10)]
    k1, e1 = pick_topk(["退货", "政策"])
    k2, e2 = pick_topk(["那个", "东西", "怎么", "弄", "帮忙", "看看"])
    k3, e3 = pick_topk(["退货"])
    assert k1 == 2 and k3 == 2, "聚焦查询用最小宽度"
    assert k2 > k1, "高熵模糊查询自动加宽"
    k4, _ = pick_topk(["模糊", "查询", "很", "发散", "完全", "没有", "重点"], cap=5)
    assert k4 == 5, "宽度受预算封顶"
    assert e2 > e1 >= 0
    assert retrieve(index, "q", k2) == index[:k2]
    print("自适应宽度通过:低熵收窄 高熵加宽 预算封顶")
```

**追问**:
- 熵高但其实是闲聊怎么办? 答:前置意图分类,闲聊直接走零检索路径,不进宽度调节
- 宽度调了效果怎么验证? 答:离线用评估集对比固定宽度与自适应的命中率与生成成本,线上灰度看同指标
