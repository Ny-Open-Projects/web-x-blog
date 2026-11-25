---
title: [VIZ-340] slerp 与 lerp/nlerp 的差异与选型
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-340：slerp 与 lerp/nlerp 的差异与选型

**答**：
- lerp 分量线性插值后不再单位化（旋转会变形加速）；nlerp 归一化近似（角速度不均匀）；slerp 精确匀速但 trig 开销大。
- 选型：小角度（<10°）nlerp 与 slerp 视觉无差且便宜；大角度动画（相机转场）必须 slerp。
- 批量优化：骨骼动画上百关节逐帧 slerp 时预计算 sinθ 复用。

```javascript
// 三种插值对比
function lerpV(a, b, t) { return a.map((v, i) => v + (b[i]-v)*t); }
function nlerp(a, b, t) {
  const v = lerpV(a, b, t);
  const len = Math.hypot(...v) || 1;
  return v.map(x => x / len);
}
// slerp 见 339；验证角速度均匀性：
function angleBetween(a, b) {
  const d = Math.min(1, Math.abs(a[0]*b[0]+a[1]*b[1]+a[2]*b[2]+a[3]*b[3]));
  return Math.acos(d) * 2;                  // 旋转角
}
// nlerp 在 t=0.5 时角速度偏离 50%+（大角度时）
```
