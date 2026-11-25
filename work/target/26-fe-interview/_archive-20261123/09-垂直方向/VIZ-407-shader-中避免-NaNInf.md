---
title: [VIZ-407] shader 中避免 NaN/Inf 的防御写法
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-407：shader 中避免 NaN/Inf 的防御写法

**答**：
- 来源：除零（归一化零向量）、asin/acos 越界、sqrt 负数——传播后整屏变黑。
- 防御：normalize 前 max(len, epsilon)、clamp 到有效域、final color 校验（NaN 检测）。
- 调试：输出异常标记色（品红）定位 NaN 来源像素。

```javascript
// 防御模板
`vec3 safeNormalize(vec3 v) {
  float l = length(v);
  return l > 1e-6 ? v / l : vec3(0.0, 1.0, 0.0);   // 零向量兜底
}
float safeAcos(float x) { return acos(clamp(x, -1.0, 1.0)); }
// NaN 检测输出：
// if (isnan(color.r)) outColor = vec4(1, 0, 1, 1);   // 品红定位
```
