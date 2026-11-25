---
title: [VIZ-369] 环境光照：IBL（基于图像的光照）为什么用预滤波
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-369：环境光照：IBL（基于图像的光照）为什么用预滤波

**答**：
- 实时对环境贴图做全卷积太贵——预滤波分两层：漫反射辐照度图（低频）+ 高光预滤波（按 roughness 分 mip）。
- split-sum：specular = 预滤波色 × 环境_BRDF 查找表（LUT 2D：NdotV × roughness）。
- Web 端 PMREM（three.js）即此方案：离线/启动时一次生成，运行时只是两次纹理采样。

```javascript
// split-sum 概念实现
function iblSpecular(envPrefiltered, brdfLUT, N, V, roughness, F0) {
  const R = reflect(V, N);
  const mip = roughness * envPrefiltered.maxMip;
  const preColor = envPrefiltered.sample(R, mip);        // 预滤波部分
  const [NoV, r] = [Math.max(0, dot(N, V)), roughness];
  const [scale, bias] = brdfLUT.sample(NoV, r);          // LUT 部分
  return preColor.map((c, i) => c * (F0[i] * scale + bias));
}
const dot = (a, b) => a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
function reflect(I, N) { return I.map((v, i) => v - 2*dot(I,N)*N[i]); }
```
