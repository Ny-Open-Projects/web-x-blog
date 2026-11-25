---
title: [VIZ-421] Shader 端的深度还原：从 depth buffer 到视空间 Z
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-421：Shader 端的深度还原：从 depth buffer 到视空间 Z

**答**：
- NDC z 非线性（透视）——线性化：z_view = 2nf / (f + n - z_ndc(f - n))（OpenGL 惯例）。
- 用途：SSR/Fog/粒子软边缘需要线性深度比较；WebGPU 常用反向 Z（near=1, far=0）提升精度。
- 实现：depthLinearize 函数进 common chunk 全局复用。

```javascript
// 深度线性化
function linearizeDepth(zNdc, near, far) {
  // OpenGL 风格 [-1,1]
  return (2 * near * far) / (far + near - zNdc * (far - near));
}
// WebGL 默认 [0,1]：
function linearizeD3D(z, near, far) {
  const zn = z * 2 - 1;
  return linearizeDepth(zn, near, far);
}
// 反向 Z（WebGPU 推荐）：
// proj[10] = far/(near-far); proj[14] = far*near/(near-far); depthCompare: 'greater'
```
