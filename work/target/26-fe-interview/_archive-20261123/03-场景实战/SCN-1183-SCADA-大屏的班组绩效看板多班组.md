---
title: [SCN-1183] SCADA 大屏的班组绩效看板（多班组对比）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1183：SCADA 大屏的班组绩效看板（多班组对比）

**答**：
- 对比：班组产量/质量/能耗/安全多维度对比（雷达图），奖惩透明化。
- 公平：班组设备/订单差异修正（难度系数）。
- 周期：月度评比排名趋势。

```javascript
// 班组绩效
function shiftPerformance(shifts, difficulty) {
  return shifts.map(s => ({
    shift: s.name,
    score: Math.round(
      (s.output / difficulty[s.name].outputNorm) * 40 +
      s.quality * 40 + s.energyScore * 20),
    note: '按设备与订单难度系数修正',
  })).sort((a, b) => b.score - a.score);
}
```
