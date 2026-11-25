---
title: [1027] 「A 和 B 什么关系」这类问题，向量检索效果差怎么办
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, GraphRAG]
type: 面试题
---

## 1027：「A 和 B 什么关系」这类问题，向量检索效果差怎么办

**答**：
- 向量检索对「多跳关系」天然弱：A->B->C 的关系分散在多个 chunk，单路 top-k 拼不出完整链条；GraphRAG 把实体关系抽成图，查询时图遍历 + 子图摘要回答。
- 落地做法：离线抽实体与关系（LLM 批量抽取 + 去重合并），查询时先实体识别 → 图上取 2 跳子图 → 子图内容与向量检索结果融合进 prompt。
- 成本现实：抽取成本是普通索引的 5~10 倍，只对「关系密集」语料（组织架构、产品依赖、法规引用）建图，普通 FAQ 不值得。
- 追问钩子：图数据怎么保鲜？——文档更新时增量更新关联子图（而不是全图重建），实体合并要处理「同名不同物」（歧义消解是最大坑）。

```ts
async function graphAnswer(q) {
  const ents = await ner(q);                        // 识别查询实体
  const subgraph = await graph.neighbors(ents, { hops: 2, limit: 20 });
  const vec = await hybridSearch(q, 10);            // 向量路并行
  const ctx = [summarizeGraph(subgraph), ...vec].join('\n---\n');
  return llm(genPrompt(q, ctx));
}
```
