---
title: [SCN-1162] SCADA 大屏的能耗与产量联动分析（单位能耗）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1162：SCADA 大屏的能耗与产量联动分析（单位能耗）

**答**：
- 联动：单位产量能耗（kWh/件）趋势——能耗上升产量不变即异常。
- 分析：能耗构成分解（主设备/辅助/待机）。
- 目标：单位能耗目标线对比（超目标偏差预警）。

```javascript
// 单位能耗
function unitEnergy(energyKWh, output, target) {
  const unit = output > 0 ? energyKWh / output : null;
  return { unit: unit && +unit.toFixed(3), target,
    over: unit > target,
    breakdown: { main: energyKWh * 0.7, aux: energyKWh * 0.2, idle: energyKWh * 0.1 },
    advice: unit > target ? `单位能耗超目标 ${((unit / target - 1) * 100).toFixed(1)}%` : null };
}
```
