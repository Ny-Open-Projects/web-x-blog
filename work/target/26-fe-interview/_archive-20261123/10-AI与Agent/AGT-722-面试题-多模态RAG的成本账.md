---
title: [AGT-722] 多模态知识库的成本构成与优化点（解析/索引/查询三阶段）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-722：多模态知识库的成本构成与优化点（解析/索引/查询三阶段）

**答**：
- 三阶段成本：解析期（vision 描述+OCR，一次性但最贵）、索引期（embedding 便宜但量大）、查询期（vision 重提取/judge 调用，持续发生）。
- 优化杠杆：解析期结果全缓存（哈希幂等，重跑不重复付费）；查询期优先用「入库时提取好的数据」而非每次读原图（查询期 vision 调用砍 90%）；索引期只对有价值资产建跨模态索引。
- 成本看板按文档/模态维度拆，识别"贵而不被用"的资产（索引成本高、引用为零）做下线。

```javascript
function mmCostReport(month) {
  const byPhase = groupBy(costs(month), 'phase');  // parse/index/query
  const byAsset = costs(month).reduce((m, c) => {
    m[c.assetId] = (m[c.assetId] ?? 0) + c.usd;
    return m;
  }, {});
  return { byPhase,
    waste: Object.entries(byAsset)
      .filter(([id, usd]) => usd > P90 && citations(id) === 0)
      .map(([id]) => id),                          // 贵而不被用
    lever: '查询期优先用预提取数据' };
}
```

