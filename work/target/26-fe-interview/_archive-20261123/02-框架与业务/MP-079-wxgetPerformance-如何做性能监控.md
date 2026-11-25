---
title: [MP-079] wx.getPerformance 如何做性能监控？（高频）
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-079：wx.getPerformance 如何做性能监控？（高频）
**答**：
- `wx.getPerformance()` 获取 PerformanceObserver，可观测 `appLaunch/firstRender/firstPaint/route` 等性能条目。
- 实践：上报首屏（appLaunch → firstRender）、页面路由耗时，按机型（benchmarkLevel）/版本聚合看趋势。
- 配合「启动性能分析」工具与自定义埋点定位慢页面、慢机型。

```javascript
const observer = wx.getPerformance().createObserver((entryList) => {
  entryList.getEntries().forEach((e) => {
    report('perf', { name: e.name, duration: e.duration, path: e.path })
  })
})
observer.observe({ entryTypes: ['navigation', 'render', 'script'] })
```
