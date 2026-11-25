---
title: [VIZ-404] 光照循环：多光源的 shader 组织
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-404：光照循环：多光源的 shader 组织

**答**：
- 前向：循环全部光源（顶点少片元贵）；光源数据 UBO 一次绑定。
- 分簇（clustered）：屏幕空间分簇，每片元只算所在簇光源——百光源可行。
- 简化：光源按贡献排序截断（最近的 N 个），视觉损失小。

```javascript
// 光源循环
`uniform Light { vec4 posType[16]; vec4 colorRange[16]; } uL;
uniform int uLightCount;
vec3 lighting(vec3 N, vec3 P, vec3 albedo) {
  vec3 sum = vec3(0.0);
  for (int i = 0; i < uLightCount; i++) {
    vec3 L = uL.posType[i].xyz - P;
    float dist = length(L); L /= max(dist, 1e-4);
    float att = clamp(1.0 - dist / uL.colorRange[i].w, 0.0, 1.0);
    sum += albedo * max(dot(N, L), 0.0) * uL.colorRange[i].rgb * att * att;
  }
  return sum;
}`
```
