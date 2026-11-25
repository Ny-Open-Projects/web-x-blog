---
title: [NODE-858] 笔试题——实现灰度指标看板聚合器（对比+门槛+放量建议）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-858：手写灰度看板

**需求与边界**：
- 需求：灰度看板数据（SCN-OPS-239）——① 硬指标自动判定（错误率/延迟/CPU——SCN-OPS-239 分区）；② 软指标趋势（转化——不下结论）；③ 放量建议（下一档门槛达成状态——SCN-OPS-242）；④ 降级聚合（SCN-NODE-690）。
- 边界：① 对比基线动态（SCN-OPS-304）；② 样本量下限（SCN-OPS-203）；③ 汇总为 IM 卡片（SCN-OPS-325 日报联动）。

**答**：
```javascript
async function grayDashboard(releaseId) {
  const canary = await versionMetrics(release.canaryVer);
  const stable = await versionMetrics(release.stableVer);
  const hard = {
    errorRate: verdict(canary.errorRate, stable.errorRate, { max: 1.5 }),
    p99: verdict(canary.p99, stable.p99, { max: 1.3 }),   // SCN-OPS-239 分区
    cpu: verdict(canary.cpu, stable.cpu, { max: 1.4 }),
  };
  const soft = { conversion: trendOnly(canary.conversion, stable.conversion) };   // 不下结论
  const ready = Object.values(hard).every(v => v === 'OK') &&
    canary.samples >= minSamples;                      // SCN-OPS-203/242 门槛
  return {
    hard, soft, ready,
    rampSuggest: ready ? '可放量' : `等待: ${fails(hard)}`,   // SCN-OPS-242
    degraded: degradeSummary(releaseId),               // SCN-NODE-690
    card: grayCardIM({ hard, ready }),                 // SCN-OPS-325 IM 卡片
  };
}
```

**评分点**:
- 硬/软分区（SCN-OPS-239）。
- 门槛判定 + 放量建议（SCN-OPS-242）。
- 样本量下限（SCN-OPS-203）。
- 降级聚合 + IM 卡片（SCN-NODE-690/OPS-325）。
