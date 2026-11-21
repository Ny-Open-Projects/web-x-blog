---
title: [VIZ-120] ZRender 的多层 Canvas 与脏矩形是怎么工作的？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-120：ZRender 的多层 Canvas 与脏矩形是怎么工作的？
**答**：① **分层**——zrender 默认背景层 + 可交互层，`zlevel` 相同的图元同层，跨 zlevel 创建新 canvas：把高频动画系列放高 zlevel，静态背景低 zlevel，动画帧内静态层完全不重绘；② **脏矩形**——图元变更时把其包围盒并入脏区，每帧只对脏区 clearRect 并重绘区域内图元，整屏静态部分不动；③ **命中检测**——事件层监听 pointer，用图元 `contain`（路径级精确判断）+ hover 层光标联动；④ tooltip 是独立 DOM 层不占 canvas。大屏分层是标准优化手段。

```javascript
// zrender 分层观察与利用
const chart = echarts.init(el);
chart.setOption(option);
const zr = chart.getZr();
console.log(zr.painter.getLayers().map(l => l.__zlevel)); // 各层 zlevel
// 按层拆分：动画飞线放 zlevel 2，静态地图放 zlevel 1，动画帧只重绘上层
chart.setOption({ series: [
  { type: 'map', zlevel: 1 },                                        // 静态层
  { type: 'lines', coordinateSystem: 'geo', zlevel: 2, data: flows } // 动画层
]});
// 直接用 zrender 同理：指定 zlevel 触发独立 canvas
const zr2 = zrender.init(dom);
zr2.add(new zrender.Circle({ shape: { r: 10 }, zlevel: 2 }));
```
