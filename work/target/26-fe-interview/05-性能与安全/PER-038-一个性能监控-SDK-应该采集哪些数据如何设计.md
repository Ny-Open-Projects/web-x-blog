---
title: [PER-038] 一个性能监控 SDK 应该采集哪些数据？如何设计？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-038：一个性能监控 SDK 应该采集哪些数据？如何设计？

**答**：
- 加载指标：TTFB、FCP、LCP、CLS（交互响应可加 INP），全部用 `buffered: true` 观测。
- 资源指标：慢资源 Top N（duration 大于 1s），定位劣化的第三方脚本与图片。
- 交互指标：长任务次数与总时长，作为 INP 的过程指标。
- 设计要点：页面稳定后（如 load 后延迟 3s）一次性上报，避免高频请求；字段带页面 URL、设备、网络类型方便下钻。

```javascript
// 性能监控 SDK：统一采集加载指标与慢资源
export function collectPerformance() {
  const data = {};

  new PerformanceObserver((l) => {
    data.ttfb = l.getEntries()[0].responseStart;
  }).observe({ type: 'navigation', buffered: true });

  new PerformanceObserver((l) => {
    data.lcp = l.getEntries().at(-1).startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });

  new PerformanceObserver((l) => {
    for (const e of l.getEntries()) {
      if (!e.hadRecentInput) data.cls = (data.cls || 0) + e.value;
    }
  }).observe({ type: 'layout-shift', buffered: true });

  // 慢资源 Top N，用于发现劣化的第三方脚本
  data.slowResources = performance.getEntriesByType('resource')
    .filter((r) => r.duration > 1000)
    .sort((a, b) => b.duration - a.duration)
    .slice(0, 5)
    .map((r) => ({ name: r.name, duration: Math.round(r.duration) }));

  // 页面稳定后再一次性上报，避免采集本身影响业务
  setTimeout(() => report('perf', data), 3000);
}
```
