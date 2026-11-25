---
title: [VIZ-355] 颜色空间：sRGB 与线性空间的转换为什么必须做
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-355：颜色空间：sRGB 与线性空间的转换为什么必须做

**答**：
- 渲染光照计算必须在线性空间（物理正确），而纹理存储/显示是 sRGB（伽马 2.2 压缩）。
- 转换：sRGB → linear ≈ pow(c, 2.2)，linear → sRGB ≈ pow(c, 1/2.2)；WebGL 用 SRGB8_ALPHA8 纹理格式由硬件自动转。
- 不做转换的症状：光照偏暗/过曝、混合（透明叠加）颜色错误、渐变出现色带。

```javascript
// sRGB <-> Linear
function srgbToLinear(c) {
  c /= 255;
  return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
}
function linearToSrgb(c) {
  return c <= 0.0031308 ? c * 12.92 : 1.055 * Math.pow(c, 1/2.4) - 0.055;
}
// 半混合验证：50% 灰叠 50% 灰
// sRGB 空间直接混合 -> 0.5（视觉正确）
// linear 混合后未转回 -> 0.214（过暗）——必须最后转 sRGB 输出
```
