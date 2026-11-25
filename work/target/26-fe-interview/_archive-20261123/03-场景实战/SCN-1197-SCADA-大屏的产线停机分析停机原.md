---
title: [SCN-1197] SCADA 大屏的产线停机分析（停机原因帕累托与 MTTR）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1197：SCADA 大屏的产线停机分析（停机原因帕累托与 MTTR）

**答**：
- 分析：停机次数/时长按原因分类（帕累托），MTTR（平均修复时长）趋势。
- 根因：Top 停机原因根因树（5Why 记录）。
- 改进：改进措施与停机率对比验证。

```javascript
// 停机分析
function downtimeAnalysis(stops) {
  const pareto = defectPareto(stops.map(s => ({ type: s.reason })));   // 1184 复用
  const mttr = avg(stops.map(s => s.durationMin));
  return { pareto, mttr: Math.round(mttr) + 'min',
    topCause: pareto[0]?.type,
    fiveWhy: (stopId) => api('/downtime/5why', { stopId }),
  };
}
function avg(a) { return a.reduce((s, v) => s + v, 0) / (a.length || 1); }
```
