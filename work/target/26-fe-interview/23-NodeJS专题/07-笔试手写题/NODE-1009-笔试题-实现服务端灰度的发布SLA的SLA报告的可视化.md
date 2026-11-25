---
title: [NODE-1009] 笔试题——实现 SLA 报告可视化（达标率热力 + 趋势）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1009：手写 SLA 可视化

**需求与边界**：
- 需求：SLA 可视化（SCN-SLA-968/1009）——① 热力矩阵（指标×月份达标率——SCN-联想-751 分级）；② 趋势线（SCN-SLA-708）；③ 违约标注（SCN-OPS-716）；④ 下钻（SCN-SLA-705）。
- 边界：① 分级色阶（SCN-联想-751）；② 标注联动（SCN-SLA-708）；③ 下钻链接（SCN-SLA-705）。

**答**：
```javascript
function slaHeatmap(metrics, months) {
  const cells = metrics.flatMap(m =>
    months.map(month => {
      const rate = compliance(m, month);
      return { metric: m, month, rate, level: levelOf(rate, thresholds()),   // 分级（SCN-联想-751）
        drill: { metric: m, month, status: 'BREACH' } };
    }));
  return { cells, annotations: eventsIn(months),       // 标注（SCN-SLA-708）
    trend: trendLine(metrics), drill: (c) => slaDetail(c) };   // 下钻（SCN-SLA-705）
}
```

**评分点**:
- 热力矩阵 + 分级色阶（SCN-联想-751）。
- 违约标注 + 下钻（SCN-SLA-708/705）。
