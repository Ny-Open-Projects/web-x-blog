---
title: [ALG-425] 手写 AC 自动机 fail 树性质：敏感词归属去重
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-425：手写 AC 自动机 fail 树性质：敏感词归属去重

**答**：
- 题目：敏感词库有包含关系（「赌博」与「网络赌博」），匹配时同一文本段会被多词命中，要去重归属（最长匹配优先）。
- 思路：fail 树性质：节点 v 在 u 的 fail 子树内 ⟺ v 是 u 的后缀模式。去重规则：命中区间被更长命中覆盖则丢弃——按 end 排序后保留最长 start 覆盖。
- 评分点：fail 树后缀包含关系；区间覆盖去重；最长匹配语义的确定。

```javascript
function dedupeHits(text, hits) {                          // hits: [{pattern, end, len}]
  const withRange = hits.map(h => ({ ...h, start: h.end - h.pattern.length + 1 }));
  withRange.sort((a, b) => a.start - b.start || b.pattern.length - a.pattern.length);
  const kept = [];
  let coverTo = -1;
  for (const h of withRange) {
    if (h.start < coverTo) continue;                       // 被前一个更长命中覆盖
    kept.push(h);
    coverTo = h.end + 1;                                   // 最长匹配优先
  }
  return kept;
}
// fail 树含义：fail[v] 的 out 包含 v 的所有后缀模式——「网络赌博」的 fail 链会带出「赌博」
// 去重策略由业务定：最长匹配（本例）或全部保留计数
```
