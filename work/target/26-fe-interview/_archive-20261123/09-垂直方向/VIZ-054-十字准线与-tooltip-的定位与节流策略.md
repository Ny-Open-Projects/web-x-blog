---
title: [VIZ-054] 十字准线与 tooltip 的定位与节流策略？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-054：十字准线与 tooltip 的定位与节流策略？
**答**：tooltip 是最高频的交互路径，三个优化点：① **节流**——mousemove 不直接渲染，用 rAF 合帧（一帧至多更新一次），数据查找用二分而不是遍历；② **定位策略**——默认出现在指针右上方，靠近右边界翻转到左侧、靠近上下边界夹回可视区，避免遮挡与出界；③ **十字准线**——垂直/水平参考线 + 轴向跟随，trigger: 'axis' 模式下显示同 x 的所有系列值。数据量大时 tooltip 内容本身也要聚合（见 VIZ-096）。

```javascript
// tooltip 高频更新必须节流：rAF 合帧 + 二分查找最近数据点
let rafId = 0;
canvas.addEventListener('mousemove', e => {
  if (rafId) return;                       // 同帧只排一次任务
  rafId = requestAnimationFrame(() => {
    rafId = 0;
    const idx = d3.bisectCenter(xs, e.offsetX); // O(log n) 找最近点
    drawCrosshair(xs[idx], ys[idx]);            // 十字准线跟随数据点
    showTooltip(e.offsetX, e.offsetY, data[idx]);
  });
});
// 定位策略：距边 < tooltip 尺寸时翻转，上下夹回可视区
function tipPos(px, py, tw, th, vw, vh) {
  return {
    x: px + 16 + tw > vw ? px - tw - 16 : px + 16,
    y: Math.min(Math.max(py - th / 2, 8), vh - th - 8),
  };
}
```
