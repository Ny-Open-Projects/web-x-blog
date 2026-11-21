---
title: [AGT-026] 什么是 rerank 重排序？为什么向量检索后还要精排？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-026：什么是 rerank 重排序？为什么向量检索后还要精排？
**答**：
- 向量检索是"双塔"式：query 与文档各自独立编码，快但粗，容易召回字面相近语义不相关的结果。
- rerank 用 cross-encoder 把 query 和每个候选拼在一起逐对打分，精度高但慢，只能对少量候选做。
- 标准做法是两阶段：向量粗召回 TopN（如 50）→ rerank 精选 TopK（如 5），兼顾召回率与精度。
- 常用方案：Cohere Rerank API、bge-reranker 自部署，或让 LLM 自己做 listwise 精排。

```typescript
// 两阶段检索：向量粗召回 50 条，rerank 精选 5 条
async function twoStageSearch(
  query: string,
  store: VectorStore,
  { recallK = 50, finalK = 5 }: { recallK?: number; finalK?: number } = {},
): Promise<RetrievedChunk[]> {
  // 第一阶段：向量粗召回，只算相似度，快但粗
  const candidates = await store.search(await embedQuery(query), recallK);

  // 第二阶段：cross-encoder 逐对计算 query 与候选的相关性
  const res = await fetch('https://api.example.com/v1/rerank', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.RERANK_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'rerank-v2',
      query,
      documents: candidates.map((c) => c.text),
      top_n: finalK,
    }),
  });
  if (!res.ok) throw new Error(`rerank 失败：${res.status}`);
  const data = await res.json();

  return data.results.map((r: { index: number; relevance_score: number }) => ({
    ...candidates[r.index],
    score: r.relevance_score,
  }));
}
```

---

## 六、MCP 协议
