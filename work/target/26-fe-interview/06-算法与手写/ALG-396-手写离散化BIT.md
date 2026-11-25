---
title: [ALG-396] 手写离散化+BIT：大值域排名统计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-396：手写离散化+BIT：大值域排名统计

**答**：
- 题目：交易金额范围 [1, 1e12]，实时插入金额，查「小于 X 的交易笔数」（分位数统计）。BIT 建在 rank 上（离散化后最多 n 个不同值）。
- 思路：收集所有可能查询值（插入值+查询端点）离散化 → BIT 按 rank 计数；查 < X 的笔数 = sum(rank(X) - 1)。
- 评分点：查询端点也要离散化；rank 边界（等值处理）；值域 1e12 下 BIT 不可直接建的认知。

```javascript
function rankStats(inserts, queries) {
  const all = [...inserts, ...queries.flatMap(q => [q.x])];
  const sorted = [...new Set(all)].sort((a, b) => a - b);
  const rank = new Map(sorted.map((v, i) => [v + 1, i + 1]));
  const bit = new BIT(sorted.length);
  const out = [];
  const events = [...inserts.map(v => ({ t: 'ins', v })),
    ...queries.map(q => ({ t: 'q', q }))].sort((a, b) => a.t - b.t ?? 0);   // 实际按到达序
  for (const e of inserts) bit.add(rank.get(e), 1);
  for (const q of queries) {
    const r = rank.get(q.x) ?? lowerBound(sorted, q.x);     // 端点离散化
    out.push(bit.sum(r - 1));                               // 小于 X 的笔数
  }
  return out;
}
const lowerBound = (a, x) => { let lo = 0, hi = a.length;
  while (lo < hi) { const m = (lo + hi) >> 1; a[m] < x ? lo = m + 1 : hi = m; } return lo; };
```
