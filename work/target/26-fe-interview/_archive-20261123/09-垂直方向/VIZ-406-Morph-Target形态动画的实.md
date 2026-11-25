---
title: [VIZ-406] Morph Target（形态动画）的实现
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-406：Morph Target（形态动画）的实现

**答**：
- 数据：每形态一组位移 delta（或完整目标位置），shader 加权叠加：pos = base + Σ w_i × delta_i。
- 限制：WebGL attribute 数有限——形态多时用纹理存储（morph 纹理）按帧采样。
- 用途：面部表情（blendshape）、缩放动画、扭曲特效。

```javascript
// morph shader
`in vec3 aBase;
uniform sampler2D uMorphTex;   // 每行一个形态
uniform float uWeights[8];
vec3 morph() {
  vec3 p = aBase;
  for (int i = 0; i < 8; i++) {
    if (uWeights[i] == 0.0) continue;
    vec3 d = texelFetch(uMorphTex, ivec2(gl_VertexID, i), 0).xyz;
    p += d * uWeights[i];
  }
  return p;
}`
```
