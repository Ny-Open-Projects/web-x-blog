---
title: [NODE-996] 笔试题——实现 SLA 趋势预警与预防行动（预测→行动）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-996：手写趋势行动

**需求与边界**：
- 需求：趋势预警行动（SCN-SLA-990/996）——① 趋势预测（SCN-SLA-990 回归）；② 预警的触发（预测低于 SLO——SCN-SLA-990）；③ 预防行动清单（扩容/降级预案/SLA 修正——SCN-NODE-834/965）；④ 行动的执行与验证（SCN-OPS-960）。
- 边界：① 预测的置信（SCN-SLA-744）；② 行动的优先级（SCN-OPS-202）；③ 行动的审计（SCN-OPS-273）。

**答**：
```javascript
async function trendPrevention(sla) {
  const forecast = await slaTrendForecast(sla);        // 预测（SCN-SLA-990）
  if (!forecast.atRisk) return;
  const actions = [
    { priority: 1, run: () => scalePreemptively(sla) },      // 扩容（SCN-NODE-834）
    { priority: 2, run: () => verifyDegradeMatrix(sla) },    // 降级预案（SCN-OPS-329）
    { priority: 3, run: () => proposeSlaChange(sla, { to: forecast.ci[0] }) },   // SLA 修正（SCN-SLA-965）
  ];
  for (const a of actions.sort(byPriority)) {
    const r = await a.run();
    if (r.ok && a.priority === 1) break;               // 扩容解决即停止
    audit({ sla: sla.id, action: a.priority, result: r });   // 审计（SCN-OPS-273）
  }
}
```

**评分点**:
- 趋势预测复用（SCN-SLA-990）。
- 预防行动清单（扩容/降级/SLA 修正——SCN-NODE-834/OPS-329/965）。
- 优先级执行 + 审计（SCN-OPS-202/273）。
