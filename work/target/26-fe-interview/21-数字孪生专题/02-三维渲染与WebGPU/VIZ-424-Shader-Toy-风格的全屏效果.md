---
title: [VIZ-424] Shader Toy 风格的全屏效果：Raymarching 入门
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-424：Shader Toy 风格的全屏效果：Raymarching 入门

**答**：
- Raymarching：SDF 场景 + 步进求交（球体追踪：步长 = 当前 SDF 值）。
- 核心循环：while (t < maxDist && d > eps) { d = sceneSDF(ro + rd*t); t += d; }——步数 64~128。
- 用途：程序化艺术/体积云/实验图形；生产慎用（片元贵），适合加载页特效。

```javascript
// SDF 场景 + raymarch
function sceneSDF(p) {
  const sphere = Math.hypot(...p) - 1.0;
  const box = Math.max(Math.abs(p[0]) - 0.6,
    Math.max(Math.abs(p[1]) - 0.6, Math.abs(p[2]) - 0.6));
  return Math.min(sphere, box);               // 并集
}
function march(ro, rd, { maxSteps = 64, eps = 0.001, maxDist = 20 } = {}) {
  let t = 0;
  for (let i = 0; i < maxSteps; i++) {
    const d = sceneSDF(ro.map((v, j) => v + rd[j] * t));
    if (d < eps) return t;
    t += d;
    if (t > maxDist) break;
  }
  return null;
}
```
