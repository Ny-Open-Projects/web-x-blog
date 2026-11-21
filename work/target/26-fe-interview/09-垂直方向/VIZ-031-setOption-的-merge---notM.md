---
title: [VIZ-031] setOption 的 merge / notMerge / replaceMerge 有什么区别？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-031：setOption 的 merge / notMerge / replaceMerge 有什么区别？
**答**：默认 **merge**：新旧 option 深合并，未传字段保留，交互状态（dataZoom 位置等）不丢，适合数据更新；**notMerge: true**：完全替换，组件状态重置，适合整体切换视图/换图表类型；**replaceMerge: ['series']**：以数组为单位精确替换指定组件维度，用于动态增删系列且避免 merge 导致的旧系列残留。另有两个性能参数：`lazyUpdate` 延迟到下一帧渲染、`silent` 阻止触发事件。

```javascript
chart.setOption(baseOption); // 首次全量
// 默认 merge：只更新传入字段，dataZoom 位置等交互状态保留
chart.setOption({ series: [{ data: newData }] });
// notMerge: true 完全替换，适合整体切换视图（如换图表类型），但交互状态被重置
chart.setOption(nextOption, { notMerge: true, lazyUpdate: true });
// replaceMerge：动态增删系列时精确替换 series 维度，避免旧系列残留
chart.setOption({ series: newSeries }, { replaceMerge: ['series'] });
// 经验：轮询更新用 merge；页面视图切换用 notMerge + lazyUpdate；可配置面板用 replaceMerge
```
