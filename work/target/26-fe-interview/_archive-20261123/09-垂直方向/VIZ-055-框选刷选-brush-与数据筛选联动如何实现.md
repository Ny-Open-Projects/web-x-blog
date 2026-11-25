---
title: [VIZ-055] 框选刷选（brush）与数据筛选联动如何实现？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-055：框选刷选（brush）与数据筛选联动如何实现？
**答**：刷选 = 用户在画布上拖出矩形/区间，把该区间换算成数据域，联动所有依赖视图。d3 提供 `d3.brushX / d3.brush`：`.extent` 限定可刷区域，事件回调里 `selection.map(scale.invert)` 得到数据域，然后驱动主图过滤、统计卡片更新、其他图表同步。工程要点：双击/清空选区要恢复全量；大数据边界定位用 bisect 而不是全量 filter；刷选状态要可编程恢复（ECharts 用 dispatchAction dataZoom）。

```javascript
const brush = d3.brushX()
  .extent([[0, 0], [width, height]])
  .on('start brush end', e => {
    if (!e.selection) { restoreAll(); return; }   // 双击清空选区 -> 恢复全量
    const [x0, x1] = e.selection.map(xScale.invert); // 像素 -> 数据域
    const i0 = d3.bisectLeft(times, x0), i1 = d3.bisectRight(times, x1); // bisect 定位
    const filtered = data.slice(i0, i1);
    renderMain(filtered);   // 主图只画选区内数据
    renderStat(filtered);   // 联动统计卡片：均值/峰值/计数
  });
svg.append('g').call(brush);
// 联动本质：一次刷选 -> 一个数据域 -> 所有视图以该域为单一数据源重算
```
