---
title: [VIZ-121] ECharts 的动画系统如何实现？形变动画的插值原理？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-121：ECharts 的动画系统如何实现？形变动画的插值原理？
**答**：① 入场/更新动画——View 层每图元注册到 zrender 的 **Animatable**：记录起始与目标状态，按 easing 函数 rAF 逐帧插值；② **形变（morphing）**——数据变化时旧图元到新图元：路径采样成等量点列做点对点插值，多边形用顶点插值，`universalTransition` 让跨系列形变（柱→饼→折线）成为可能；③ 插值器覆盖数字、颜色（RGB）、transform；④ 性能要点——大数据关更新动画（animationDurationUpdate: 0），只保留入场；自定义 easing 可注册到 zrender。

```javascript
// zrender 动画 API 与 ECharts 跨系列形变
const zr = zrender.init(document.getElementById('c'));
const rect = new zrender.Rect({ shape: { x: 0, y: 0, width: 10, height: 10 } });
zr.add(rect);
rect.animate('shape', true)          // loop 循环动画
  .when(1000, { width: 200, height: 80 })
  .when(2000, { width: 10, height: 10 })
  .start('cubicOut');                // easing 名称即插值函数
// ECharts 侧：柱形平滑变饼形
chart.setOption({ series: [{ type: 'bar',
  universalTransition: { enabled: true }, data }], animationDurationUpdate: 600 });
chart.setOption({ series: [{ type: 'pie',
  universalTransition: { enabled: true }, data }]); // 形变插值在 zrender 层完成
```
