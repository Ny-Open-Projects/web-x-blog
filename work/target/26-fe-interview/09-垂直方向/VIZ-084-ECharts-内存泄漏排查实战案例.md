---
title: [VIZ-084] ECharts 内存泄漏排查实战案例。
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-084：ECharts 内存泄漏排查实战案例。
**答**：案例现象：SPA 频繁切换报表页，内存单调上涨直至崩溃。排查：Performance Monitor 看到 JS Heap 与 DOM Nodes（detached）同步增长；Heap Snapshot 两次快照对比，retained 中出现几十个 `ECharts` 实例，retainer 链指向 `window._charts` 全局缓存与未解绑的 resize 监听。修复：组件卸载时 dispose + removeEventListener + 清空全局引用；轮询定时器一并清理。回归手段：切换 50 次后断言实例数为 1 的内存测试。

```javascript
// 案例：全局缓存 + resize 监听 + 定时器 三处泄漏源
const charts = new Map(); // 泄漏点 1：全局 Map 永不清理，持有 chart -> DOM 整条引用链
function mountChart(el, id, option) {
  let chart = charts.get(id) ?? echarts.init(el);
  chart.setOption(option);
  const onResize = () => chart.resize();
  window.addEventListener('resize', onResize);   // 泄漏点 2：监听器挂在 window 上
  const timer = setInterval(refresh, 5000);      // 泄漏点 3：轮询定时器
  charts.set(id, chart);
  return () => {                                 // 卸载函数必须拆掉全部三处
    clearInterval(timer);
    window.removeEventListener('resize', onResize);
    chart.dispose();
    charts.delete(id);
  };
}
// 验证：切换页面 50 次后 Heap Snapshot 搜 ECharts 实例数应为 0
```
