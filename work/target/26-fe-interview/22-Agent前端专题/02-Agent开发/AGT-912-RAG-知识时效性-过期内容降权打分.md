---
title: [912] 新闻/政策类知识库更新频繁，检索如何处理内容过期
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 时效性]
type: 面试题
---

## 912：新闻/政策类知识库更新频繁，检索如何处理内容过期

**答**：
- 打分引入时间因子：final_score = relevance × decay(published_at)，decay 用指数衰减，半衰期按内容类型配置（政策类 90 天、新闻类 7 天、规范类不衰减）。
- 「失效文档」显式标注：被新版本替代的文档打 superseded_by 字段，检索到旧文档时优先返回新版本链接，或直接从候选剔除。
- query 带时间意图时要识别：「最新」「2024」这类词触发时间过滤，而不是靠 decay 慢慢衰减。
- 追问钩子：衰减会不会误伤「历史公告」类合法查询？——会，所以 decay 只影响排序不影响过滤，且用户显式问历史时移除衰减。

```ts
function decayScore(hit, now) {
  const halfLife = HALF_LIFE[hit.meta.type] ?? Infinity;
  const days = (now - hit.meta.publishedAt) / 86400000;
  return hit.score * Math.pow(0.5, days / halfLife); // 半衰期模型
}
function retrieve(q, { historical = false } = {}) {
  let hits = hybridSearch(q, 30);
  if (!historical) hits = hits.map(h => ({ ...h, score: decayScore(h, Date.now()) }))
    .sort((a, b) => b.score - a.score);
  return hits.slice(0, 5);
}
```

