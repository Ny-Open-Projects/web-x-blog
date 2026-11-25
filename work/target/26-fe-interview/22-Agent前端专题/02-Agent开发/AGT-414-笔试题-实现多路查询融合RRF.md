---
title: [AGT-414] 笔试题——实现多路检索 RRF 融合（含查询路由与去重）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-414：手写混合检索融合：BM25+向量 RRF、专名路由加权、文档级去重

**需求与边界**：
- 输入：query、两路检索函数、路由规则；输出：融合排序 top-k。
- 边界要求：① RRF 公式正确（1/(k+rank)）；② 含专有名词（错误码/API 名）的查询提升 BM25 权重；③ 同文档多 chunk 命中合并（文档级聚合取最高）；④ 两路结果数不足时仍可融合（不假设等长）。

**答**：
```javascript
async function hybridSearch(query, { bm25, vector, k = 10, K = 60 }) {
  const hasProperNoun = /([A-Z]{2,}[-_]\d+|API[\w_]*|\w+Error)/.test(query);
  const weightB = hasProperNoun ? 0.6 : 0.3;      // 专名偏词法
  const weightV = 1 - weightB;
  const [r1, r2] = await Promise.all([bm25(query, 50), vector(query, 50)]);
  const score = new Map(); const chunkOf = new Map();
  r1.forEach((d, rank) => score.set(d.docId,
    (score.get(d.docId) ?? 0) + weightB / (K + rank + 1)));
  r2.forEach((d, rank) => score.set(d.docId,
    (score.get(d.docId) ?? 0) + weightV / (K + rank + 1)));
  // 文档级聚合：同 docId 的 chunk 取最高分，合并命中块引用
  const docBest = new Map();
  for (const d of [...r1, ...r2]) {
    const cur = docBest.get(d.docId);
    if (!cur || d.score > cur.score) docBest.set(d.docId, d);
  }
  return [...docBest.entries()]
    .sort((a, b) => b[1].rrfScore ?? score.get(b[0]) - score.get(a[0]))
    .slice(0, k)
    .map(([docId, d]) => ({ docId, rrf: score.get(docId), chunk: d.id,
      sources: { bm25Rank: r1.findIndex(x => x.docId === docId),
                 vecRank: r2.findIndex(x => x.docId === docId) } }));
  // sources 保留两路排名（可解释可调试）。
}
```

**评分点**:
- RRF 公式正确（rank 从 0 起算 +K 平滑），权重随专名路由动态调整。
- 文档级聚合去重（同文档多 chunk 取最高）而非 chunk 级堆叠。
- 不等长两路也能融合（Map 累加天然支持）；保留双路排名用于解释。
- 专名正则路由只是示意——能说明规则路由的局限与升级方向（分类器路由）。
