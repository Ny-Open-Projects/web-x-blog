---
title: "[Q7706] score_threshold 与 top_k 双门槛的召回质量账"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7706 · score_threshold 与 top_k 双门槛的召回质量账

难度：P6 ｜ 标签：容量成本账、RAG、召回质量、延迟

基线：Python 3.12；向量检索 top_k / score_threshold；纯 Python 模拟双门槛过滤。

**问**：RAG 检索配了 `top_k=20` 又加 `score_threshold=0.7`，结果有时召回为空、答案瞎编，有时塞满 20 条低质量片段、token 爆了。两个门槛怎么配合？怎么算这笔"召回质量-延迟-token"账？

**答**：
- **结论**：`top_k` 是**数量上限**（最多取 k 条），`score_threshold` 是**质量下限**（低于阈值的不要），二者是"与"关系：先取相似的再过滤，最终条数 ≤ top_k。常见误区：(1) 只用 top_k，向量库在低相似查询上也会硬凑 k 条垃圾，污染上下文；(2) 阈值设太高，召回为空，LLM 无证据就幻觉；(3) 阈值设太低等于没设。不同 embedding 模型的相似度分布不同（余弦 vs 点积、归一化与否），阈值不能跨模型照搬。
- **取舍**：召回是"宁可多不可漏"（漏了就没机会纠正），重排才是"精挑"；所以召回阶段 top_k 可放宽、阈值保守，靠 rerank 与 token 预算收敛。阈值定太高牺牲 recall、太低牺牲 precision——要在标注 query 上画 P/R 曲线选点。
- **实战**：按 embedding 模型分别标定阈值（用正/负样本看分数分布重叠区）；召回为空时走"拒答/改写重试"而不是让 LLM 裸答；监控每次召回的有效条数与分数分布漂移；把 top_k × 单条 token 控制在上下文预算内。

```python
def retrieve(scores: list[tuple[str, float]], k: int, threshold: float) -> list[str]:
    """先按分数排序取 top_k，再用阈值过滤：最终条数 <= k。"""
    ranked = sorted(scores, key=lambda x: -x[1])[:k]
    return [doc for doc, s in ranked if s >= threshold]


if __name__ == "__main__":
    scores = [("d1", 0.92), ("d2", 0.75), ("d3", 0.55), ("d4", 0.88)]
    print("k=3 th=0.7:", retrieve(scores, k=3, threshold=0.7))
    print("k=2 th=0.8:", retrieve(scores, k=2, threshold=0.8))
    print("阈值过高 -> 空召回:", retrieve(scores, k=4, threshold=0.99))
```

**追问一**：为什么召回为空时让 LLM 裸答很危险？
→ 解析：没有检索证据兜底，LLM 只能靠参数化知识生成，容易幻觉；正确做法是触发拒答模板、查询改写重试或转人工，把"无证据"显式处理。

**追问二**：换了 embedding 模型后阈值为什么必须重新标定？
→ 解析：不同模型/相似度度量的分数分布不同（余弦值域、是否归一化、校准程度），同一数值阈值在新模型上含义变了。要用标注样本重新看正负例的分数分布，重选阈值。
