---
title: [AGT-203] RAG 混合检索——BM25 与向量检索怎么融合？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-203：BM25 与向量检索怎么融合——混合检索怎么设计？

**答**:
- 为什么混合：向量擅长语义相似但弱于精确词（专有名词/错误码/API 名），BM25 擅长关键词精确匹配但不懂语义——两者互补，混合检索在大多场景显著优于单一检索。
- 融合方法：RRF（Reciprocal Rank Fusion）最常用——每路结果按排名取倒数加权融合，无需调分数归一；或分数归一后加权（需调参，对分数尺度敏感）。
- 权重与路由：常见配比 BM25 0.3~0.5 / 向量 0.5~0.7；进阶做查询路由——含专有名词/ID 的查询偏 BM25，自然语言问题偏向量，分类器或规则判断。
- 工程实现：ES/OpenSearch 的 hybrid query 或"向量库+BM25 双查再 RRF"，注意两路各自取足够深的候选（top 50×2）再融合，避免融合池太小。

```javascript
// RRF 融合示意
function rrf(rankLists, k = 60) {
  const score = new Map();
  for (const list of rankLists) {           // 每路按排名
    list.forEach((docId, rank) => {
      score.set(docId, (score.get(docId) || 0) + 1 / (k + rank + 1));
    });
  }
  return [...score].sort((a, b) => b[1] - a[1]);
}
// 最终 = rrf([bm25Top50, vectorTop50])
// 查询路由：/错误码|API_\d+/ → BM25 权重上调
```
