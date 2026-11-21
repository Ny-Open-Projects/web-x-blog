---
title: [VIZ-018] 十万级点/线在 Canvas 上如何渲染优化？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-018：十万级点/线在 Canvas 上如何渲染优化？
**答**：分层递进：① **TypedArray**（Float32Array）存坐标，去掉对象与 GC 压力；② **视口裁剪**——框外点直接 continue；③ **批量绘制**——所有点收集进同一个 path，一次 fill/stroke（状态切换与 draw call 是大头）；④ **像素分桶聚合**——点数远超像素时按网格聚合，每格最多画一次，性能与点数解耦；⑤ 交互命中用 quadtree 索引而不是遍历。折线则用步长抽稀（相邻像素最多一个点）。

```javascript
// 10 万点：TypedArray 存储 + 视口裁剪 + 单 path 批量 fill
function drawScatter(ctx, xs, ys, view) {
  ctx.fillStyle = 'rgba(30,120,200,0.5)';
  ctx.beginPath();
  for (let i = 0; i < xs.length; i++) {
    const x = xs[i], y = ys[i]; // TypedArray 读取，无对象与 GC 开销
    if (x < view.x0 || x > view.x1 || y < view.y0 || y > view.y1) continue; // 裁剪
    ctx.rect(x, y, 2, 2);       // 收集进同一个 path
  }
  ctx.fill();                   // 一次 fill 画完所有点，draw call 唯一
}
// 点数 > 数万像素时升级为分桶聚合：性能与点数无关，只与像素有关
function binPoints(xs, ys, w, h, cell = 4) {
  const cols = Math.ceil(w / cell), rows = Math.ceil(h / cell);
  const bins = new Uint32Array(cols * rows);
  for (let i = 0; i < xs.length; i++) {
    bins[Math.min(((ys[i] / h) * rows) | 0, rows - 1) * cols +
         Math.min(((xs[i] / w) * cols) | 0, cols - 1)]++;
  }
  return { bins, cols, rows, cell };
}
```
