---
title: [NODE-1023] 笔试题——实现 SLA 趋势预警闭环（预测→行动→验证→复盘）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1023：手写预警闭环

**需求与边界**：
- 需求：预警闭环（SCN-SLA-996/1023）——① 预测（SCN-SLA-990）；② 行动（SCN-SLA-996）；③ 行动验证（SCN-联想-865）；④ 复盘（SCN-OPS-248）。
- 边界：① 预测的置信（SCN-SLA-744）；② 行动的优先级（SCN-OPS-202）；③ 审计（SCN-OPS-273）。

**答**：
```javascript
async function trendClosedLoop(sla) {
  const forecast = await slaTrendForecast(sla);        // 预测（SCN-SLA-990）
  if (!forecast.atRisk) return;
  const actions = await trendPrevention(sla);          // 行动（SCN-SLA-996）
  const verified = await Promise.all(actions.map(a => verifyAction(a)));   // 验证（SCN-联想-865）
  await slaPostmortem({ forecast, actions, verified });   // 复盘（SCN-OPS-248）
  return { forecast, verified };
}
```

**评分点**:
- 预测→行动→验证→复盘四步（SCN-SLA-990/996/865/248）。
- 置信（SCN-SLA-744）+ 审计（SCN-OPS-273）。
