---
title: [NODE-824] 笔试题——实现服务依赖图健康度检查（级联故障预警）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-824：手写依赖健康

**需求与边界**：
- 需求：服务依赖图健康（SCN-NODE-669/703）——① 依赖图建模（服务 → 依赖服务——拓扑）；② 级联预警（下游熔断 → 上游熔断概率预警——图传播）；③ 依赖冗余度评估（单点依赖检测——bus factor，SCN-ENG-314）；④ 健康度输出（全图状态 + 风险点）。
- 边界：① 图数据来源（部署声明 + 调用统计——SCN-OPS-261 影响面）；② 预警的阈值（下游熔断 → 上游请求失败率上升——传导检测）；③ 图变更检测（依赖变化即审计——SCN-OPS-260）。

**答**：
```javascript
function dependencyHealth(depsGraph, liveStatus) {
  // 1. 级联预警：下游 open → 依赖它的上游失败率上升预测
  const cascade = [];
  for (const [svc, deps] of Object.entries(depsGraph)) {
    const broken = deps.filter(d => liveStatus[d]?.breaker === 'open');
    if (broken.length) cascade.push({ svc, broken,
      predictedImpact: broken.flatMap(b => liveStatus[b]?.latencyDelta ?? 0) });
  }
  // 2. 单点依赖（bus factor——SCN-ENG-314 同构）
  const singlePoints = Object.entries(depsGraph)
    .filter(([svc, deps]) => deps.length === 1)
    .map(([svc, [d]]) => ({ svc, single: d, risk: liveStatus[d]?.criticality ?? 'low' }));
  return {
    cascade,                                           // 级联预警（SCN-NODE-669 传播）
    singlePoints,                                      // 单点依赖清单
    health: 1 - cascade.length / Object.keys(depsGraph).length,
    drillSuggest: singlePoints.map(s => `演练 ${s.svc} 依赖 ${s.single} 故障（SCN-OPS-281 注入）`),
  };
}
```

**评分点**:
- 级联预警（下游熔断 → 上游影响预测——图传播）。
- 单点依赖检测（bus factor——SCN-ENG-314 同构）。
- 演练建议联动（注入器——SCN-OPS-281）。
- 全图健康分（可视化）。
