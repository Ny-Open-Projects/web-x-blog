---
title: [WEB-118] PerformanceObserver 如何搭建统一的性能采集体系？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-118：PerformanceObserver 如何搭建统一的性能采集体系？
**答**：
- PerformanceObserver 统一订阅各指标条目类型：navigation/resource（网络）、paint（FP/FCP）、largest-contentful-paint、layout-shift（CLS）、longtask（主线程阻塞）、event（INP 相关）。
- `buffered: true` 回放观察者注册前已产生的条目——埋点 SDK 必开，否则早期指标丢失。
- 按需订阅避免全量收包：采集什么订阅什么；上报用 sendBeacon 在 pagehide 时一次性发送。
- longtask 归因：entry.attribution 里能看到容器类型，辅助定位是脚本还是渲染。

```javascript
// 统一采集核心 Web Vitals + 长任务
function report(name, value) {
  beacon.push({ name, value: Math.round(value), ts: Date.now() });
}
const beacon = [];
new PerformanceObserver((l) => l.getEntries().forEach((e) => report('LCP', e.startTime)))
  .observe({ type: 'largest-contentful-paint', buffered: true });
new PerformanceObserver((l) => l.getEntries().forEach((e) => report('CLS', e.value)))
  .observe({ type: 'layout-shift', buffered: true });
new PerformanceObserver((l) => l.getEntries().forEach((e) => report('longtask', e.duration)))
  .observe({ type: 'longtask', buffered: true });
new PerformanceObserver((l) => l.getEntries().forEach((e) => report('FCP', e.startTime)))
  .observe({ type: 'paint', buffered: true });

// 离开页面时一次性上报
window.addEventListener('pagehide', () => {
  navigator.sendBeacon('/perf', JSON.stringify(beacon)); // 不阻塞卸载且可靠
});
```
