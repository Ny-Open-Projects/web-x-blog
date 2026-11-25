---
title: [AGT-202] RAG 重排序——召回之后为什么还要 rerank？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-202：RAG 为什么召回后还要重排序——rerank 怎么选型？

**答**:
- 两阶段逻辑：向量召回（ANN）追求"快和高召回率"，牺牲精度；rerank 用 cross-encoder 逐对精算 query 与候选的相关性，追求"准"——召回 100 选 5，精度提升直接减少幻觉源。
- 召回与 rerank 的配比：召回 top 50~100 → rerank 取 top 3~8 进上下文；召回不足再准的 rerank 也救不了（漏检），所以先保证召回率再谈精度。
- 选型梯度：bge-reranker 这类开源 cross-encoder（低成本）/ Cohere Rerank、Jina reranker（API，效果好）/ LLM 打分 rerank（最贵最灵活，用小模型即可）——按成本与延迟预算选。
- 工程细节：rerank 是逐对计算，候选越多延迟越高，生产上控制候选数（≤100）+ 并行打分 + 对高频 query 做结果缓存。

```javascript
// 两阶段检索管线
async function retrieve(query) {
  const candidates = await vectorSearch(query, 100);  // 快召回
  const scored = await Promise.all(
    candidates.map(c => rerank(query, c))             // cross-encoder 精排
  );                                                  // 生产可用 batch API
  return scored.sort((a, b) => b.score - a.score)
               .slice(0, 6);                          // top6 进上下文
}
// 评估 rerank 收益：对比 rerank 前后的
// hit@k / MRR，没有提升就别白加延迟。
```
