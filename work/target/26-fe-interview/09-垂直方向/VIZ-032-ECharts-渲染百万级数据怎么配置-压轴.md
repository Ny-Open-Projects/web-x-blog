---
title: [VIZ-032] ECharts 渲染百万级数据怎么配置？（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-032：ECharts 渲染百万级数据怎么配置？（压轴）
**答**：三板斧组合：**sampling: 'lttb'**——在像素级降采样，保留峰值形状，数据量与渲染点数解耦；**large: true**——large 模式关闭逐项样式与动画，走优化绘制路径（scatter/bar 生效）；**progressive 分片渲染**——每帧最多渲染 progressive 个数据项，超长的渲染任务切片执行，避免单帧长任务阻塞交互。再配合：关动画、dataZoom 限制可视窗口、后端预聚合。终极手段是 `appendData` 增量加载或自研 WebGL 系列（GL series）。

```javascript
option = {
  xAxis: { type: 'category' },
  yAxis: { type: 'value' },
  dataZoom: [{ type: 'inside' }, { type: 'slider' }],
  series: [{
    type: 'line',
    data: millionPoints,          // 十万级以上数据
    sampling: 'lttb',             // 1. 像素级降采样，保留峰值形状
    large: true,                  // 2. large 模式：关逐项样式，走优化路径
    largeThreshold: 2000,         //    超过 2000 条启用 large
    progressive: 5000,            // 3. 分片渲染：每帧最多 5000 项，不阻塞交互
    progressiveThreshold: 10000,  //    超过 1 万条启用分片
    showSymbol: false,
    animation: false,             // 4. 大数据必关动画
  }],
};
```
