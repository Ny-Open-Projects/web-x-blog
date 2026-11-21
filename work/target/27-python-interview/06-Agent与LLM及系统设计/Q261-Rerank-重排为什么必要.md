---
title: [Q261] Rerank 重排为什么必要
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q261 · Rerank 重排为什么必要

> 难度:★★★ | 标签:RAG, 检索

**问**:向量检索已经排好序了,为什么还要 rerank?

**答**:向量检索是"双塔"结构——query 和文档分别独立编码再算相似度,快但粗糙;top-k 里常有语义擦边、主题相近但不对题的噪声。Rerank 用交叉编码器把 query 和每个候选拼接后联合编码,能捕捉细粒度交互,精度高但慢,因此只能对少量候选(如 50 条)重排,最终取 top-3~5 进 Prompt。两阶段设计本质是"召回求全、精排求准"的经典检索架构在 RAG 的复用。

```python
# file: code/06_Agent与LLM及系统设计/q261_rerank.py
"""两阶段检索:向量召回 50 条中的 5 条演示,再用伪交叉编码器重排。"""
import random


def vector_recall(query: str, docs: list[str], top_k: int) -> list[str]:
    # 假设向量召回把目标文档排在第 3 位,返回 top_k
    shuffled = docs[:]
    random.Random(42).shuffle(shuffled)
    return shuffled[:top_k]


def cross_encoder_score(query: str, doc: str) -> float:
    """伪交叉编码:query 词与 doc 词的交集占比越高越相关。"""
    q_terms = set(query)
    d_terms = set(doc)
    return len(q_terms & d_terms) / max(1, len(q_terms))


def rerank(query: str, candidates: list[str], top_n: int = 2) -> list[str]:
    scored = sorted(candidates, key=lambda d: -cross_encoder_score(query, d))
    return scored[:top_n]


if __name__ == "__main__":
    docs = ["Python GIL 限制多线程并行",
            "RAG 通过检索增强回答准确性",
            "向量数据库支持 ANN 检索",
            "重排模型提升检索精度",
            "今天中午吃什么好",
            "检索增强生成 RAG 的完整链路"]
    query = "RAG 检索"
    recall = vector_recall(query, docs, top_k=4)
    print("召回:", recall)
    print("重排后:", rerank(query, recall, top_n=2))
```

**追问**:
- rerank 模型怎么选?——专用交叉编码器(bge-reranker 类)延迟和成本远低于通用 LLM 打分;LLM-as-reranker 留给精调场景。
- rerank 的候选窗口多大?——50-100 条进 rerank,最终 3-5 条进 prompt;窗口从 top-50 扩到 top-200 的边际收益要靠评估集验证。
- 没有 rerank 的退路?——混合检索+RRF 已经能压掉大半噪声;小流量阶段可先上两阶段再补 rerank,但要预留接入位。
