---
title: [902] 混合检索（BM25 + 向量）上线的决策过程与踩坑
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 混合检索]
type: 面试题
---

## 902：混合检索（BM25 + 向量）上线的决策过程与踩坑

**答**：
- 纯向量检索在「精确词」场景失灵：错误码、型号名、专有名词，向量把它们泛化了；BM25 在「同义改写」场景失灵。生产知识库两类 query 都存在，所以混合检索几乎是必选项。
- 融合用 RRF（倒数排名融合）比加权分数稳：两路分数分布不同（BM25 无上界），加权调参要归一化且随语料漂移；RRF 只用排名，天然免调参。
- 踩坑案例：上线初期 BM25 的中文分词器按字切分，精确词反而召回一堆碎片；换词级分词后错误码类 query 命中率提升 40%。
- 追问钩子：什么时候只用一路？——查询模式单一且评估证明两路无增量时，减少一路就少一份索引维护成本。

```ts
function rrfFuse(rankedList: Doc[][], k = 60): Doc[] {
  const score = new Map<Doc, number>();
  for (const list of rankedList) {
    list.forEach((doc, i) => {
      score.set(doc, (score.get(doc) || 0) + 1 / (k + i + 1)); // 排名越靠前贡献越大
    });
  }
  return [...score.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, TOP_K)
    .map(([doc]) => doc);
}
const fused = rrfFuse([bm25Search(q, 50), vectorSearch(q, 50)]);
```

