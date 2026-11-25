---
title: [1037] RAG 端到端 3 秒预算怎么分配到各环节
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 延迟预算]
type: 面试题
---

## 1037：RAG 端到端 3 秒预算怎么分配到各环节

**答**：
- 预算分配示例（总 3s）：改写 300ms、检索 500ms、rerank 400ms、生成首 token 800ms（流式后正文不占等待）、组装与网络 200ms；余量 800ms 给重试与抖动。
- 分段埋点是前提：没有分段数据谈不上预算分配；每段设独立超时，超时的段走降级（rerank 超时 → 直接用融合结果）。
- 预算漂移治理：月度回顾各段实际耗时分布，某段长期逼近上限就加资源或降复杂度（如 rerank 恒定 400ms 说明候选数要减）。
- 追问钩子：用户感知的「慢」主要在等待首字，所以预算优化的优先级是「压缩首字前所有环节」，正文生成速度反而次要（流式掩盖）。

```ts
const BUDGET = { rewrite: 300, retrieve: 500, rerank: 400, firstToken: 800 };
async function pipeline(q, sse) {
  const rw = await step(rewrite(q), BUDGET.rewrite, { fallback: q }); // 超时降级用原 query
  const hits = await step(retrieve(rw), BUDGET.retrieve, { fallback: cached(q) });
  const ranked = await step(rerank(rw, hits), BUDGET.rerank,
    { fallback: fuse(hits) });                       // rerank 超时用融合结果
  return streamAnswer(ranked, q, sse);               // 流式：正文不阻塞感知
}
```
