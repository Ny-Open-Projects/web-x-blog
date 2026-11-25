---
title: [SCN-1140] IoT 设备的能耗异常检测（用电设备专项）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1140：IoT 设备的能耗异常检测（用电设备专项）

**答**：
- 检测：待机能耗异常（夜间基线偏高）、能效比恶化（同产量能耗上升）。
- 看板：异常设备列表（偏差率排序）+ 节能建议（关停/检修）。
- 成本：异常设备折算电费损失（量化运维价值）。

```javascript
// 能耗异常
function energyAnomaly(device, baseline) {
  const nightAvg = avg(device.nightPowerKW);
  const dev = (nightAvg - baseline.nightKW) / baseline.nightKW;
  return {
    deviation: +(dev * 100).toFixed(1) + '%',
    costLoss: +(dev * baseline.nightKW * 12 * ELECTRICITY_PRICE).toFixed(2),
    advice: dev > 0.2 ? '待机能耗异常，建议检修或关停' : null,
  };
}
const ELECTRICITY_PRICE = 0.8;
```
