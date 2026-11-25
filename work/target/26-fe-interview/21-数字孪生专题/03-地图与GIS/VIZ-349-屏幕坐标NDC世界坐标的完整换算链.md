---
title: [VIZ-349] 屏幕坐标、NDC、世界坐标的完整换算链
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-349：屏幕坐标、NDC、世界坐标的完整换算链

**答**：
- 链路：世界 → View（V）→ Clip（P）→ NDC（透视除法）→ 屏幕（viewport 变换：*0.5+0.5 × 宽高）。
- 反向拾取：屏幕 → NDC（逆 viewport）→ Clip（w=1）→ 世界（invVP）；Ray 方向 = far point - near point。
- 注意 DPR 与 canvas 尺寸/视口尺寸不一致（rect 缩放）是拾取偏移的最常见原因。

```javascript
// 拾取射线
function pickRay(mx, my, canvas, invVP) {
  const ndc = [
    (mx / canvas.clientWidth) * 2 - 1,
    1 - (my / canvas.clientHeight) * 2,      // y 翻转
  ];
  const unproject = (z) => {
    const v = mul4(invVP, [ndc[0], ndc[1], z, 1]);
    return [v[0]/v[3], v[1]/v[3], v[2]/v[3]];
  };
  const near = unproject(-1), far = unproject(1);
  const dir = far.map((v, i) => v - near[i]);
  const len = Math.hypot(...dir) || 1;
  return { origin: near, dir: dir.map(x => x/len) };
}
function mul4(m, v) { /* 同 337 */ return [0,0,0,1]; }
```
