---
title: [VIZ-442] Overdraw 的度量与治理
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-442：Overdraw 的度量与治理

**答**：
- 度量：overdraw pass（输出叠加计数），热点区域=颜色亮度；目标 < 2.5x。
- 来源：透明粒子堆叠、UI 层层叠加、无深度写入的大面积特效。
- 治理：降透明物分辨率、排序后 early-z、特效改为 additive（免排序但叠加仍贵）。

```javascript
// overdraw 统计 pass
`// fs: 输出叠加次数
outColor = vec4(0.5, 0.5, 0.5, 1.0) * 0.1 + outColor * 0.0;   // 累加式
// 或 blend ONE,ONE 累加，读回统计均值`
function overdrawReport(readback) {
  const avg = readback.reduce((s, v) => s + v, 0) / readback.length;
  return { avgOverdraw: +avg.toFixed(2),
    hot: avg > 2.5 ? '有热点，检查透明物' : 'ok' };
}
```
