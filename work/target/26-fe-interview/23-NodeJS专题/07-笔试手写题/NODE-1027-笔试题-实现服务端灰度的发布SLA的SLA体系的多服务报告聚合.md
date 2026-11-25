---
title: [NODE-1027] 笔试题——实现多服务 SLA 报告聚合（SLA 全景）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1027：手写全景聚合

**需求与边界**：
- 需求：全景聚合（SCN-SLA-968/1024）——① 多服务报告聚合（SCN-SLA-995）；② 全景看板（SCN-SLA-968）；③ 跨服务一致性（SCN-SLA-1004）；④ 报告的消费（SCN-OPS-728）。
- 边界：① 聚合的完整性（SCN-OPS-850）；② 一致性（SCN-SLA-1004）；③ 报告（SCN-OPS-728）。

**答**：
```javascript
async function multiServiceSlaAggregate(services, month) {
  const byService = await Promise.all(services.map(s => slaTracking(s, month)));   // SCN-SLA-955
  const overall = weightedAverage(byService, { by: 'traffic' });   // 加权（SCN-OPS-850）
  const consistency = await crossServiceSlaCheck(depsGraph);   // 一致性（SCN-SLA-1004）
  return { byService, overall, consistency,
    drill: (s) => slaDetail(s), archive: archiveSlaReport(byService) };   // SCN-SLA-705/248
}
```

**评分点**:
- 多服务聚合 + 加权（SCN-SLA-955/850）。
- 跨服务一致性（SCN-SLA-1004）。
- 消费归档（SCN-OPS-728/248）。
