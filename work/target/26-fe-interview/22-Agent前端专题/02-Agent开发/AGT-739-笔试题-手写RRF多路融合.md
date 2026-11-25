---
title: [AGT-739] 手写 rrfFuse：倒数排名融合、路权重、可配k、空路容错？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-739：手写 rrfFuse：倒数排名融合、路权重、可配k、空路容错

**需求与边界**：
- 实现 rrfFuse(lists, { k = 60, weights })。
- 边界要求：① 每路贡献 = weight / (k + rank)，rank 从 1 计；② 权重缺省 1，负权重/零权重抛错；③ 某一路为空不影响其他路；④ 相同 id 跨路累加，输出按分排序并带各路命中明细。

**答**：
```javascript
function rrfFuse(lists, { k = 60, weights = {} } = {}) {
  if (k <= 0) throw new Error('K_POSITIVE');
  const acc = new Map();
  lists.forEach((list, li) => {
    const w = weights[li] ?? 1;
    if (w <= 0) throw new Error('WEIGHT_POSITIVE');
    list.forEach((item, i) => {
      const rec = acc.get(item.id) ?? { id: item.id, score: 0, hits: [] };
      rec.score += w / (k + i + 1);                // rank 从 1 计
      rec.hits.push({ route: li, rank: i + 1 });
      acc.set(item.id, rec);
    });
  });
  return [...acc.values()]
    .sort((a, b) => b.score - a.score)
    .map(r => ({ ...r, s: r.score }));             // hits 留归因
}
```

**评分点**:
- RRF 公式正确（rank 从 1、k 平滑），跨路累加。
- 权重与 k 校验显式抛错；空路容错不崩。
- 输出带各路命中明细（排序可归因，便于调权重）。

