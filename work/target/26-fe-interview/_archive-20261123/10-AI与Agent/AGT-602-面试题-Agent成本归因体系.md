---
title: [AGT-602] 一个 Agent 任务花了 3 块钱，如何把成本归因到（模型调用/工具/检索/缓存命中），并支持按团队/租户分摊？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-602：一个 Agent 任务花了 3 块钱，如何把成本归因到（模型调用/工具/检索/缓存命中），并支持按团队/租户分摊

**答**：
- 成本只在「模型调用」与「外部 API」两个源头计量，其他 span 归零；每个 LLM span 记录 prompt/completion tokens × 单价（单价随模型版本走快照价，避免调价后历史账变脸）。
- 归因维度做成标签而不是独立链路：cost attach 到 span 后按任意维度聚合（租户/团队/任务类型/模型），一次采集多口径出账。
- 缓存命中要计入「节省成本」：命中语义缓存记 saved_tokens，报表区分毛成本与净成本——否则缓存优化在成本报表上看不见收益。

```javascript
function priceOf(modelVer, usage) {
  const p = PRICES[modelVer];            // 快照单价
  return usage.promptTokens * p.prompt + usage.completionTokens * p.completion;
}
function attachCost(span, usage, { cached = false } = {}) {
  span.attr('cost.usd', priceOf(span.attr('llm.model'), usage));
  if (cached) span.attr('cost.saved', priceOf(span.attr('llm.model'), usage));
}
// 报表聚合：按任意标签维度 groupBy
const byTenant = traces.groupBy(s => s.tags['tenant.id'])
  .map(g => ({ gross: sum(g, 'cost.usd'), saved: sum(g, 'cost.saved') }));
```

