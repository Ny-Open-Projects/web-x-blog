---
title: [VIZ-345] 贝塞尔曲线的 de Casteljau 求值与导数
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-345：贝塞尔曲线的 de Casteljau 求值与导数

**答**：
- n 阶贝塞尔 = 控制点的伯恩斯坦多项式组合；de Casteljau 递归线性插值数值稳定，适合运行时求点。
- 导数 = (n) × (相邻控制点差构成的低阶贝塞尔)，用于匀速运动需弧长重参数化（速度 ≠ 参数速度）。
- 弧长参数化：预计算弧长表（采样 100 点），运行时按弧长二分查 t——匀速沿路径动画的标准做法。

```javascript
// de Casteljau + 弧长表
function deCasteljau(pts, t) {
  let p = pts.map(p => [...p]);
  while (p.length > 1) {
    p = p.slice(1).map((v, i) =>
      v.map((x, j) => x + (p[i][j] - x) * t));
  }
  return p[0];
}
function arcTable(pts, samples = 100) {
  const table = [{ t: 0, s: 0 }];
  let prev = deCasteljau(pts, 0), total = 0;
  for (let i = 1; i <= samples; i++) {
    const t = i / samples;
    const cur = deCasteljau(pts, t);
    total += Math.hypot(cur[0]-prev[0], cur[1]-prev[1]);
    table.push({ t, s: total });
    prev = cur;
  }
  return { table, total };
}
function byArcLength({ table, total }, s) {   // 匀速取 t
  const i = table.findIndex(e => e.s >= s * total);
  return table[Math.max(0, i)]?.t ?? 0;
}
```
