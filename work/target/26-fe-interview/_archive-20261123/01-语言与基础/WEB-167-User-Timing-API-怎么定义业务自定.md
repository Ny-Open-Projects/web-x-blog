---
title: [WEB-167] User Timing API 怎么定义业务自定义指标？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-167：User Timing API 怎么定义业务自定义指标？
**答**：
- performance.mark(name) 打点，performance.measure(name, startMark, endMark) 计算区间，精度与浏览器内建指标一致。
- 自定义指标是标准 PerformanceEntry（entryType 为 mark/measure），可被同一套 PerformanceObserver 采集上报。
- 典型用法：业务关键节点（搜索结果首条渲染、支付弹窗出现）打 mark，让业务指标与 TTFB/FP 同口径对比。
- measure 的 options 也支持直接给 start/end 数值，适合与异步事件配合。

```javascript
// 业务自定义指标：搜索到首条结果渲染
performance.mark('search:start');
const results = await search(keyword);
requestAnimationFrame(() => {
  performance.mark('search:first-row-painted');
  performance.measure('search-latency', 'search:start', 'search:first-row-painted');
  const [m] = performance.getEntriesByName('search-latency');
  report('custom-metric', { name: m.name, duration: m.duration }); // 与内建指标同口径
});
```
