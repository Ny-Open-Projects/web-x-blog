---
title: [TST-668] RAG 检索的召回与重排怎么优化精度？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-668：RAG 检索的召回与重排怎么优化精度？

**答**：
- 结论：先扩大召回（向量 top50 + BM25 top50 合并去重），再用 rerank 模型精排到 top5。
- 切块策略按语义段落而非固定字数，保留标题路径作为上下文前缀。
- 重排特征加入「来源可信度 + 时间新鲜度 + 历史有效性」。
- 追问钩子：rerank 模型本身也会出错，如何在回答中暴露不确定性？

```javascript
function rerank(candidates, signals) {
  return candidates.map(c => ({
    ...c,
    final: c.sim * 0.5
      + (signals.trust[c.source] || 0.5) * 0.2
      + freshness(signals.date[c.id]) * 0.2
      + (signals.helpful[c.id] || 0) * 0.1,
  })).sort((a, b) => b.final - a.final);
}
function freshness(date) {
  const days = (Date.now() - new Date(date)) / 86400000;
  return Math.max(0, 1 - days / 365);
}
```
