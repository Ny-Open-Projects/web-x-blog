---
title: [903] RAG 加 rerank 重排器：收益怎么量、延迟预算怎么分
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 重排]
type: 面试题
---

## 903：RAG 加 rerank 重排器：收益怎么量、延迟预算怎么分

**答**：
- rerank 的收益来源：向量召回是「双塔」粗排（query 和 doc 独立编码），rerank 是 cross-encoder 逐对精算，对 top-50 精排出 top-5，MRR 提升通常在 5%~15%。
- 延迟预算：rerank 耗时与候选数线性相关，50 条约 200~500ms。生产做法是压缩候选到 30 条内 + rerank 服务独立部署可水平扩容，端到端 P95 控制在 1.2s 内。
- 缓解方式：query 相似命中缓存时跳过 rerank；低风险场景（如导航推荐）砍掉 rerank 换响应速度。
- 追问钩子：rerank 提分但用户没感知？——分块太碎导致命中片段信息不完整，重排救不了源头，先修分块再谈 rerank。

```ts
async function retrieve(q: string) {
  const cands = await rrfFuse([bm25(q, 30), vector(q, 30)]); // 先混合召回 30 条
  if (await cacheHit(q)) return cacheGet(q);                 // 缓存命中跳过重排
  const t0 = performance.now();
  const ranked = await rerankService.score(q, cands);        // cross-encoder 精排
  metrics.observe('rerank_ms', performance.now() - t0);      // 延迟单独埋点，可独立降级
  return ranked.slice(0, 5);
}
```

