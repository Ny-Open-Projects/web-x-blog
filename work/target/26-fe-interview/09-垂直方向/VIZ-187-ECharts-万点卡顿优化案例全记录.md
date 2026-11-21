---
title: [VIZ-187] ECharts 万点卡顿优化案例全记录。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-187：ECharts 万点卡顿优化案例全记录。
**答**：案例复盘式作答：**现象**——1 万点折线 + tooltip 拖动掉帧到 20fps。**定位**——Performance 火焰图：tooltip 触发全 series 高亮重绘 + 1 万点未降采样全量绘制，且每点独立 symbol 命中检测。**手段**——① `sampling: 'lttb'` 降到 2 千点；② `large: true` + `largeThreshold` 关逐点命中；③ tooltip 用 cross axisPointer + `emphasis: { focus: 'none' }` 避免全 series 高亮；④ 拖动时 `silent` + 自绘十字线；⑤ 关闭更新动画。**效果**——P95 帧 40ms → 8ms。**沉淀**——团队大数据图表模板默认配置 + 性能 checklist。答题要点：现象→定位→手段→量化效果→沉淀，五步闭环。

```javascript
// 优化前后对比：大数据折线的推荐配置
const before = { series: [{ type: 'line', data: tenKPoints, symbol: 'circle',
  hoverAnimation: true }] };                                   // 全量绘制 + 逐点命中
const after = {
  tooltip: { trigger: 'axis', axisPointer: { type: 'cross' } },
  series: [{
    type: 'line', data: tenKPoints,
    sampling: 'lttb',          // 渲染前 LTTB 降采样
    large: true, largeThreshold: 2000,   // 大数据模式，关逐点 symbol 命中
    symbol: 'none',            // 关 symbol
    emphasis: { focus: 'none' },                          // 关全 series 高亮
    animation: false,          // 大数据关动画
  }],
};
```
