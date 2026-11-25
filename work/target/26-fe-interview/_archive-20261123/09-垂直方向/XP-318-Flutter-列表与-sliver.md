---
title: [XP-318] Flutter 列表与 sliver 性能
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-318：Flutter 列表与 sliver 性能

**答**：
- 要点：ListView.builder 懒构建、itemExtent 固定行高、避免 build 里做 IO/计算。
- sliver：CustomScrollView 组合多滚动区域（吸头/悬浮 tab），比嵌套滚动高效。
- 工具：Flutter DevTools 性能图层（build/layout/raster 时间线）。

```javascript
// Flutter 列表要点（Dart 概念）
// ListView.builder(
//   itemExtent: 80,                 // 固定行高
//   itemBuilder: (ctx, i) => ItemWidget(data[i]),
// )
// 反模式：build 里 filter/sort 大数组 -> 应在数据层预计算
// DevTools 读数：build < 8ms, raster < 8ms 才稳 60fps
```
