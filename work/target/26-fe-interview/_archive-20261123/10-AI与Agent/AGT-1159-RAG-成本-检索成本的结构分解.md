---
title: [1159] 一次 RAG 问答的成本构成怎么分解与优化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 成本]
type: 面试题
---

## 1159：一次 RAG 问答的成本构成怎么分解与优化

**答**：
- 成本五段：query 改写（小模型）、embedding（向量检索）、rerank（cross-encoder）、生成（大模型，通常占 60%+）、外围（引用校验/审查小模型）——分解埋点是优化的前提。
- 优化优先级经验：生成段（上下文裁剪 + 前缀缓存）> rerank（候选数收敛）> 改写（蒸馏小模型）> embedding（缓存命中率高，常被忽视但便宜且高频）。
- 结构性优化：意图路由把「闲聊/简单事实」分流到轻量管线（免 rerank 免重排），只让复杂问题走全量管线——整体成本可降 40%+。
- 追问钩子：为什么 embedding 缓存常被忽略？——单次便宜但请求量最大，累积可观；且实现简单（文本 hash → 向量），是典型的「低垂果实」。

```ts
async function costBreakdown(q, intent) {
  if (intent === 'chitchat') return lightPath(q);           // 意图分流
  const t = tracker();
  const rw = await t.track('rewrite', rewrite(q, 'small'));
  const vec = await t.track('embed', embedCached(rw));      // embedding 缓存
  const hits = await t.track('retrieve', knn(vec, 30));
  const ranked = await t.track('rerank', rerank(rw, hits.slice(0, 20)));
  return t.track('generate', answer(rw, ranked.slice(0, 5)));
}
```
