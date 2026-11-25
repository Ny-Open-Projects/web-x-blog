---
title: [VIZ-423] 软粒子（Soft Particles）的深度衰减实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-423：软粒子（Soft Particles）的深度衰减实现

**答**：
- 问题：粒子穿插几何时硬边裁切明显——用场景深度与粒子深度差做 alpha 衰减。
- 实现：粒子 shader 采样场景深度图，差值 < 软边距时线性衰减 alpha。
- 依赖：深度纹理可读（depth texture 采样或 depth->color prepass）。

```javascript
// 软粒子
`float softDepthFade(vec2 uv, float particleViewZ, sampler2D sceneDepth,
                    float near, float far, float softDist = 1.0) {
  float sceneZ = linearizeDepth(texture(sceneDepth, uv).r, near, far);
  float diff = sceneZ - particleViewZ;
  return clamp(diff / softDist, 0.0, 1.0);
}`
// color.a *= softDepthFade(screenUV, viewZ, ...);
```
