---
title: [VIZ-422] Fog（雾效）的数学与视空间实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-422：Fog（雾效）的数学与视空间实现

**答**：
- 线性雾：factor = (end - dist) / (end - start) clamp；指数雾：exp(-density² × dist²)（更真实）。
- 高度雾：密度随高度衰减（地平线雾），需要视空间高度参与。
- 实现注意：用视空间距离（length(viewPos)）而非 NDC z（非线性导致远处雾浓度错误）。

```javascript
// 雾效
function fogFactor(dist, type, { start = 10, end = 100, density = 0.02 } = {}) {
  if (type === 'linear')
    return Math.min(1, Math.max(0, (end - dist) / (end - start)));
  return 1 - Math.exp(-density * density * dist * dist);   // 指数
}
// shader 内联：
// float fog = 1.0 - exp(-uFogDensity * uFogDensity * dot(viewPos, viewPos));
// color = mix(color, uFogColor, fog);
```
