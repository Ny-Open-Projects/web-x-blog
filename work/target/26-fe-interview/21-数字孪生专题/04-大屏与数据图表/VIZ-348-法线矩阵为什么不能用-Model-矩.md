---
title: [VIZ-348] 法线矩阵为什么不能用 Model 矩阵直接变换
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-348：法线矩阵为什么不能用 Model 矩阵直接变换

**答**：
- 非均匀缩放下，Model 变换法线会不再垂直于表面（剪切破坏正交性）。
- 正确做法：法线矩阵 = Model 的逆转置（对 3×3 部分）；均匀缩放时归一化即可兜底。
- 成本：逆转置每帧每物体算一次（均匀缩放可跳过），shader 里只传矩阵不传逆。

```javascript
// 法线矩阵 = inverse-transpose(M) 的 3x3
function normalMatrix(m) {   // 列主序 4x4，取左上 3x3
  const a = [m[0], m[1], m[2], m[4], m[5], m[6], m[8], m[9], m[10]];
  const inv = invert3(a);
  return transpose3(inv);     // 逆转置
}
function invert3(m) {
  const [a, b, c, d, e, f, g, h, i] = m;
  const A = e*i - f*h, B = -(d*i - f*g), C = d*h - e*g;
  const det = a*A + b*B + c*C || 1;
  return [A/det, -(b*i - c*h)/det, (b*f - c*e)/det,
          B/det, (a*i - c*g)/det, -(a*f - c*d)/det,
          C/det, -(a*h - b*g)/det, (a*e - b*d)/det];
}
function transpose3(m) { return [m[0], m[3], m[6], m[1], m[4], m[7], m[2], m[5], m[8]]; }
```
