---
title: [Q262] RAG 系统如何评估
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q262 · RAG 系统如何评估

> 难度:★★★★ | 标签:RAG, 评估

**问**:RAG 的效果怎么量化?离线评估集怎么建?

**答**:分两层评估。检索层:命中率 Recall@k、MRR(第一个相关结果的排名倒数),需要"问题→相关文档"标注。生成层:忠实度 faithfulness(答案是否只基于检索证据,反幻觉)、答案相关性 answer relevance(是否答到点上)、上下文精度 context precision(检索片段是否都是相关的)。评估集构建:从真实查询抽样 + 人工标注,或用 LLM 从文档反向生成 QA 对再人工校验;规模 50-200 条即可起步,重点保证覆盖典型 query 类型。线上看引用点击率、用户负反馈率。

```python
# file: code/06_Agent与LLM及系统设计/q262_rag_eval.py
"""实现 Recall@k、MRR 与忠实度检查(答案句子是否被证据支撑)。"""


def recall_at_k(retrieved: list[str], relevant: set[str], k: int) -> float:
    hit = sum(1 for d in retrieved[:k] if d in relevant)
    return hit / len(relevant) if relevant else 0.0


def mrr(retrieved: list[str], relevant: set[str]) -> float:
    for rank, d in enumerate(retrieved, start=1):
        if d in relevant:
            return 1.0 / rank
    return 0.0


def faithfulness(answer: str, evidence: list[str]) -> float:
    """伪忠实度:答案中每句是否能被某条证据的字面重叠支撑。"""
    sents = [s for s in answer.split("。") if s]
    supported = 0
    for s in sents:
        words = set(s)
        ok = any(len(words & set(ev)) / max(1, len(words)) > 0.3 for ev in evidence)
        supported += ok
    return supported / len(sents) if sents else 1.0


if __name__ == "__main__":
    retrieved = ["文档A", "文档B", "文档C"]
    relevant = {"文档A", "文档C"}
    print(f"Recall@2={recall_at_k(retrieved, relevant, 2):.2f} "
          f"Recall@3={recall_at_k(retrieved, relevant, 3):.2f} "
          f"MRR={mrr(retrieved, relevant):.2f}")
    ans = "RAG 检索文档后生成答案。 completely hallucinated sentence"
    ev = ["RAG 检索相关文档"]
    print(f"忠实度={faithfulness(ans, ev):.2f}")
```

**追问**:
- LLM 从文档反向生成 QA 对有什么坑?——生成的问题分布与真实 query 不一致(太书面、太规范);必须抽样人工校验并混入真实 badcase。
- faithfulness 怎么自动评?——把答案拆成断言,逐条问「证据里有没有」;LLM-as-judge 要给评分细则并抽样人工对齐。
- 线上指标看什么?——引用点击率、负反馈率、转人工率;离线指标好线上差,通常是 query 分布漂移。
