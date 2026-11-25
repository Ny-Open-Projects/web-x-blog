---
title: [NODE-990] 笔试题——实现 SLA 趋势预测（达标率回归预测）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-990：手写趋势预测

**需求与边界**：
- 需求：趋势预测（SCN-SLA-723/990）——① 回归模型（线性趋势——SCN-SLA-723 斜率）；② 预测输出（下月达标率预测——SCN-SLA-990）；③ 预测的消费（预防性扩容——SCN-NODE-834）；④ 预测的置信（SCN-SLA-744 区间）。
- 边界：① 历史数据排除事件（SCN-SLA-742）；② 预测的置信区间（SCN-SLA-744）；③ 预测的消费联动（SCN-NODE-834）。

**答**：
```javascript
async function slaTrendForecast(sla, { excludeEvents = true } = {}) {
  const history = await monthlyCompliance(sla, 12, { exclude: excludeEvents ? events : null });   // 排除事件（SCN-SLA-742）
  const reg = linearRegression(history.map((h, i) => ({ x: i, y: h })));
  const forecast = reg.slope * 12 + intercept(reg);    // 下月预测
  const ci = confidenceInterval(history, reg);         // 区间（SCN-SLA-744）
  return {
    forecast, ci,
    atRisk: forecast < sla.slo.compliance,             // 风险
    action: atRisk ? scalePreemptively(sla) : null,    // 预防性扩容（SCN-NODE-834）
  };
}
```

**评分点**:
- 回归模型 + 事件排除（SCN-SLA-723/742）。
- 置信区间（SCN-SLA-744）。
- 预防性扩容（SCN-NODE-834）。
