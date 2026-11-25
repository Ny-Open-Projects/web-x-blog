---
title: [1161] 高频 query 的答案要不要「固化」，怎么固化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 缓存]
type: 面试题
---

## 1161：高频 query 的答案要不要「固化」，怎么固化

**答**：
- 固化收益：高频 query（日均 >100 次且分布稳定）每次走全管线浪费明显；固化为「审校过的标准答案」——成本趋零、答案质量稳定（人工审校过）。
- 固化的前提与风险：答案必须有时效管理（附「最后审校时间」，过期自动退回动态管线）、必须可溯源（固化答案仍带来源引用，否则变「死答案」）、变体归一（同一意图的多种问法映射到同一固化条目）。
- 固化流程：高频 query 聚类 → 生成标准答案 → 人工审校 → 入「固化层」→ 上线监控负反馈率（固化答案的负反馈升高即回退）。
- 追问钩子：固化答案和语义缓存的区别？——语义缓存是机器自动缓存（风险是错误固化），固化层是人工审校的编辑行为（质量有保证）；两者互补，敏感意图只允许固化层不允许语义缓存。

```ts
async function maybeFixed(q) {
  const norm = normalizeIntent(q);                  // 变体归一
  const fixed = await fixedKb.get(norm);
  if (fixed && !expired(fixed.reviewedAt)) {
    return { ...fixed.answer, source: 'curated', asOf: fixed.reviewedAt };
  }
  return dynamicPipeline(q);                        // 退回动态管线
}
```
