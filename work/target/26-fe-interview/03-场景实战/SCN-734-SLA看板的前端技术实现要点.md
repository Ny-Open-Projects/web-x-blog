---
title: [SCN-734] SLA 看板前端技术实现要点（大数据量图表渲染）有哪些？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-734：看板前端技术实现要点？
**答**：
- 图表库选型：ECharts（功能全）vs 高性能场景（uPlot/G2 Plot Canvas 渲染）；多面板同屏时控制实例数（>20 个图表用懒渲染 + IntersectionObserver 进入视口才初始化）。
- 更新策略：数据推送 patch 更新 setOption（appendData/增量），禁止销毁重建实例；tooltip/legend 交互事件解绑在面板卸载。
- 时间轴交互：brush 缩放联动多图（主图选区间，子图同步缩放）；缩放触发重新查询时防抖。
- 渲染调度：面板按优先级分帧初始化（首屏核心 4 图先出，其余 idle 初始化），避免首帧卡死。
- 追问钩子：为什么 30 个 ECharts 实例同时 init 会卡——每个实例独立 canvas + 初始化计算，一次性创建主线程被占满；按视口/优先级分批是标准解法。

```javascript
const io = new IntersectionObserver(entries => {
  for (const e of entries) {
    if (e.isIntersecting && !e.target.__chart) {
      e.target.__chart = echarts.init(e.target);
      e.target.__chart.setOption(buildOption(e.target.dataset.metric));
      io.unobserve(e.target);                        // 初始化后停止观察
    }
  }
}, { rootMargin: '200px' });                          // 预渲染临近面板
document.querySelectorAll('.panel-chart').forEach(el => io.observe(el));
```
