---
title: [SCN-1144] IoT 设备控制台的设备对比功能（同型号横向对比）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1144：IoT 设备控制台的设备对比功能（同型号横向对比）

**答**：
- 对比：同型号多设备指标对比（同轴叠加/雷达图），找出离群设备。
- 离群：统计离群（z-score > 3）自动标注。
- 应用：离群设备优先维保（性能劣化早期发现）。

```javascript
// 设备对比
function deviceCompare(devices, metric) {
  const vals = devices.map(d => d.telemetry[metric]);
  const m = avg(vals), sd = std(vals) || 1;
  return devices.map(d => ({
    id: d.id, value: d.telemetry[metric],
    z: +((d.telemetry[metric] - m) / sd).toFixed(2),
    outlier: Math.abs((d.telemetry[metric] - m) / sd) > 3,
  })).sort((a, b) => Math.abs(b.z) - Math.abs(a.z));
}
function avg(a) { return a.reduce((s, v) => s + v, 0) / (a.length || 1); }
function std(a) { const m = avg(a); return Math.sqrt(avg(a.map(v => (v - m) ** 2))); }
```
