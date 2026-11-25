---
title: [VIZ-425] SDF 组合运算：并交差与平滑混合
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-425：SDF 组合运算：并交差与平滑混合

**答**：
- 布尔：min（并）、max（交）、max(sdfA, -sdfB)（差）。
- 平滑混合：smin 指数/多项式混合让并集有圆角过渡——有机形态的关键。
- 旋转/平移：SDF 空间变换（先逆变换输入点）。

```javascript
// SDF 组合
function smin(a, b, k = 0.2) {
  const h = Math.max(k - Math.abs(a - b), 0) / k;
  return Math.min(a, b) - h * h * k * 0.25;
}
function sdfSubtract(a, b) { return Math.max(a, -b); }
function sdfIntersect(a, b) { return Math.max(a, b); }
function sdfTranslate(p, t) { return p.map((v, i) => v - t[i]); }
function sdfRepeat(p, period) {   // 无限重复
  return p.map((v, i) => ((v + period[i] * 0.5) % period[i]) - period[i] * 0.5);
}
```
