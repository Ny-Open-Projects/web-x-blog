---
title: [VIZ-114] 主题河流图（ThemeRiver / StreamGraph）的实现原理？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-114：主题河流图（ThemeRiver / StreamGraph）的实现原理？
**答**：展示**时序多序列的流量变化**：x 轴是时间，每个类目是一条上下对称的"河带"，厚度编码数值。要点：① 堆叠布局用 **wiggle 居中偏移**（d3 `stackOffsetWiggle`）+ `stackOrderInsideOut`（大序列放中间），整体基线波动最小，视觉最像河流；② 边界用 Catmull-Rom/单调三次曲线平滑，注意单调插值防止过冲；③ 颜色沿序列渐变，hover 高亮单条河带并 tooltip 显示该时刻值。适合话题/情绪/流量构成随时间演化，不适合精确读数。

```javascript
// StreamGraph：wiggle 居中堆叠 + CatmullRom 平滑（D3）
const stack = d3.stack()
  .keys(seriesKeys)
  .offset(d3.stackOffsetWiggle)    // 基线偏移使整体波动最小，河带上下对称
  .order(d3.stackOrderInsideOut);  // 大序列放中间形成主河道
const layered = stack(timeRows);   // layered[k] 为第 k 条河的上下边界点列
const area = d3.area()
  .x(d => xScale(d.data.t))
  .y0(d => yScale(d[0]))
  .y1(d => yScale(d[1]))
  .curve(d3.curveCatmullRom.alpha(0.5)); // 平滑边界
svg.selectAll('path').data(layered).join('path')
  .attr('d', area)
  .attr('fill', (d, i) => colorScale(seriesKeys[i]))
  .on('mousemove', (e, d) => showRiverTooltip(e, d));
```
