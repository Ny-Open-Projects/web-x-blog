---
title: [1158] 文档入库管道怎么版本化（谁改的/改了什么/何时生效）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 数据管道]
type: 面试题
---

## 1158：文档入库管道怎么版本化（谁改的/改了什么/何时生效）

**答**：
- 版本化三层：文档版本（内容 diff 可查）、索引版本（哪批 chunk 属于哪次构建）、策略版本（分块/清洗代码的版本）；三者组合才能回答「这条 chunk 是谁在何时用什么策略生成的」。
- 审计事件流：入库/更新/删除全记事件（操作者、来源、变更摘要），与检索结果可关联（答案引用的 chunk → 构建批次 → 策略版本）。
- 回滚能力：策略升级后发现问题，按「索引版本」整体回滚到上一构建（别名切换），文档级回滚用于单文档误改。
- 追问钩子：为什么「策略版本」最常被漏？——策略（清洗规则/分块参数）常被认为不是「数据」；但同一段文本在不同策略下 chunk 完全不同，出问题时无法复现，策略版本是复现的关键。

```ts
async function ingest(doc, { operator, source }) {
  const policy = policyRegistry.current();          // 策略版本
  const buildId = await builds.next();
  const chunks = chunkWith(policy, doc);            // 策略版本参与生成
  await index.add(chunks, { buildId, policy: policy.v });
  audit.emit({ type: 'ingest', doc: doc.id, operator, source,
    buildId, policy: policy.v, chunkCount: chunks.length });
}
function traceChunk(chunkId) {                      // 溯源：chunk -> 策略
  const m = meta.of(chunkId);
  return { build: m.buildId, policy: m.policy, operator: audit.who(m.buildId) };
}
```
