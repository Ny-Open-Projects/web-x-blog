---
title: [VIZ-339] 四元数：为什么 q 与 -q 表示同一旋转
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-339：四元数：为什么 q 与 -q 表示同一旋转

**答**：
- 四元数 q = [w, x, y, z]，单位四元数表示三维旋转；q 和 -q 旋转结果相同（双重覆盖）。
- 含义：旋转轴 n、角度 θ 对应 q = [cos(θ/2), n·sin(θ/2)]——半角是四元数的本质特征。
- 注意点：插值前要检查 dot(q1, q2) < 0 时翻转一个（最短路径），否则 slerp 会绕远路。

```javascript
// 四元数基础
function quatFromAxisAngle(axis, deg) {
  const [x, y, z] = axis;
  const len = Math.hypot(x, y, z) || 1;
  const h = deg * Math.PI / 360;               // 半角
  return [Math.cos(h), x/len*Math.sin(h), y/len*Math.sin(h), z/len*Math.sin(h)];
}
function slerp(a, b, t) {
  let d = a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3];
  if (d < 0) { b = b.map(v => -v); d = -d; }   // 最短路径翻转
  const th = Math.acos(Math.min(1, d));
  if (th < 1e-6) return a;
  const s = Math.sin(th);
  const ka = Math.sin((1-t)*th)/s, kb = Math.sin(t*th)/s;
  return a.map((v, i) => v*ka + b[i]*kb);
}
```
