---
title: [VIZ-342] 透视投影矩阵的推导与 Near/Far 的取舍
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-342：透视投影矩阵的推导与 Near/Far 的取舍

**答**：
- 透视矩阵把视锥压成裁剪盒：x/y 按深度缩放（fov 与 aspect），z 非线性映射到 [-1,1]。
- Near/Far 比例决定深度精度：比值越大远处 z-fighting 越严重（24bit 深度下 ratio > 5000 常见冲突）。
- 取舍：Near 尽量大（0.1 → 0.5 精度显著提升），Far 尽量小或用 logarithmic depth buffer。

```javascript
// 透视投影矩阵
function perspective(fovyDeg, aspect, near, far) {
  const f = 1 / Math.tan(fovyDeg * Math.PI / 360);
  const nf = 1 / (near - far);
  return [f/aspect, 0, 0, 0,
          0, f, 0, 0,
          0, 0, (far+near)*nf, -1,
          0, 0, 2*far*near*nf, 0];
}
// 深度精度估算：非线性导致远处精度 ~ near²/z
function depthPrecision(z, near) {
  return (z * z) / (near * (2 ** 24));       // 24bit 深度下的近似精度
}
console.log(depthPrecision(100, 0.1));   // ~0.46m：太粗，near 提到 0.5 后 ~0.0018m
```
