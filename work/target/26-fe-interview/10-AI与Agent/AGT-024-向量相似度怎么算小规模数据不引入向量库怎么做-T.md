---
title: [AGT-024] 向量相似度怎么算？小规模数据不引入向量库怎么做 TopK 检索？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-024：向量相似度怎么算？小规模数据不引入向量库怎么做 TopK 检索？
**答**：
- 常用余弦相似度：只看方向不看模长，范围 -1~1，越大越相似。
- 小规模（几百到几万条）直接内存暴力算余弦 + 排序即可，几毫秒级，不必上向量库。
- 数据量大了用 HNSW 等近似索引（向量库内置），用召回率换速度。
- 注意预处理归一化：向量归一化后余弦等价于点积，可提速。

```typescript
// 余弦相似度 + 内存 TopK 检索
function cosineSimilarity(a: number[], b: number[]): number {
  let dot = 0;
  let normA = 0;
  let normB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

function topK(
  query: number[],
  documents: Array<{ id: string; vector: number[] }>,
  k = 5,
): Array<{ id: string; score: number }> {
  return documents
    .map((d) => ({ id: d.id, score: cosineSimilarity(query, d.vector) }))
    .sort((x, y) => y.score - x.score)
    .slice(0, k);
}
```
