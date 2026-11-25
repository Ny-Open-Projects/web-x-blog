---
title: [VIZ-367] 阴影贴图（Shadow Map）的数学与 acne 处理
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-367：阴影贴图（Shadow Map）的数学与 acne 处理

**答**：
- 原理：从光源视角渲染深度图，主渲染时比较片元深度 vs 阴影图深度，大于则阴影。
- Shadow acne：自阴影误判（深度浮点误差）——加 bias（深度偏移）或 normal offset（沿法线偏移采样点）。
- 质量：PCF（百分比渐近滤波）多次采样软化边缘；级联阴影（CSM）近处高分辨率。

```javascript
// 阴影采样 + bias
function shadowFactor(depthMap, uv, fragDepth, normal, lightDir, texel) {
  const bias = Math.max(0.0005 * (1 - dot(normal, lightDir)), 0.0002);
  let sum = 0;
  for (let i = -1; i <= 1; i++)
    for (let j = -1; j <= 1; j++) {
      const d = depthMap(uv[0] + i * texel, uv[1] + j * texel);   // PCF 3x3
      sum += fragDepth - bias > d ? 0 : 1;
    }
  return sum / 9;
}
const dot = (a, b) => a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
```
