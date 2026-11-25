---
title: [VIZ-419] Shader 端的时间与随机数：为什么不用 Math.random
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-419：Shader 端的时间与随机数：为什么不用 Math.random

**答**：
- shader 无全局随机——用 hash 函数（sin 大数取小数或 PCG hash）；同一像素每帧需一致 seed（时间驱动参数）。
- 质量：sin-hash 有网格伪影，正式项目用 PCG/白噪声纹理（蓝噪声最优）。
- 用途：抖动（TAA）、dither 消色带、粒子随机初速。

```javascript
// PCG hash（GLSL）
`float pcg(vec3 p) {
  p = fract(p * vec3(0.1031, 0.1030, 0.0973));
  p += dot(p, p.yxz + 33.33);
  return fract((p.x + p.y) * p.z);
}
// 使用：float r = pcg(vec3(gl_FragCoord.xy, uFrame));`
// 蓝噪声纹理：固定但空间低频差异小，dither 视觉最优
```
