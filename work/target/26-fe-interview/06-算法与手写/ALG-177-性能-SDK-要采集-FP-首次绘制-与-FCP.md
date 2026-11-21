---
title: [ALG-177] 性能 SDK 要采集 FP（首次绘制）与 FCP（首次内容绘制）。如何从 PerformanceEntry 中过滤，并注意哪些失真场景？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-177：性能 SDK 要采集 FP（首次绘制）与 FCP（首次内容绘制）。如何从 PerformanceEntry 中过滤，并注意哪些失真场景？
**答**：两个来源：`performance.getEntriesByType('paint')` 同步取（可能早于 SDK 初始化，需 `buffered: true` 的 PerformanceObserver 补拿历史记录）；entry.name 区分 `first-paint` / `first-contentful-paint`，startTime 即指标值。上报注意过滤：页面在后台打开时绘制被推迟、startTime 可能异常大或为 0，需按白名单条件丢弃。每次 observe 回调 O(entries)。

```javascript
function getPaintMetrics() {
  const entries = performance.getEntriesByType('paint');
  const find = name => entries.find(e => e.name === name)?.startTime;
  return {
    fp: find('first-paint'),               // 首次绘制：任何像素上屏
    fcp: find('first-contentful-paint'),   // 首次内容绘制：文本/图片/SVG
  };
}
// 推荐：PerformanceObserver 异步收集，buffered 拿到注册前的历史记录
new PerformanceObserver(list => {
  for (const e of list.getEntries()) {
    // 失真过滤：后台标签页打开时 startTime 可能异常（被节流推迟）
    if (e.startTime <= 0 || e.startTime > 30000) continue;
    report({ metric: e.name, value: Math.round(e.startTime) });
  }
}).observe({ type: 'paint', buffered: true });
```
