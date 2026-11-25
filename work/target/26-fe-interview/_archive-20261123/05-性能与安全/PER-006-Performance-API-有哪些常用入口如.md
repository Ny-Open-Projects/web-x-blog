---
title: [PER-006] Performance API 有哪些常用入口？如何读取一次页面加载的完整耗时分解？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-006：Performance API 有哪些常用入口？如何读取一次页面加载的完整耗时分解？

**答**：
- `performance.getEntriesByType('navigation')`：本次导航的 DNS、TCP、TLS、TTFB、DOM 解析、load 各阶段耗时。
- `performance.getEntriesByType('resource')`：所有静态资源请求的耗时、体积、协议。
- `performance.mark()` / `performance.measure()`：自定义业务打点，测量任意两个时点间隔。
- `PerformanceObserver` 是推荐的异步观测入口，能捕获注册后发生的记录。

```javascript
// 读取导航计时：各阶段耗时分解
const nav = performance.getEntriesByType('navigation')[0];
console.log('DNS 查询', nav.domainLookupEnd - nav.domainLookupStart, 'ms');
console.log('TCP 连接', nav.connectEnd - nav.connectStart, 'ms');
console.log('TTFB', nav.responseStart, 'ms');
console.log('HTML 下载', nav.responseEnd - nav.responseStart, 'ms');
console.log('DOMContentLoaded', nav.domContentLoadedEventEnd, 'ms');

// 读取资源计时：每个请求的耗时
performance.getEntriesByType('resource').forEach((r) => {
  console.log(r.name, Math.round(r.duration), 'ms');
});

// 自定义打点：测量弹窗初始化耗时
// performance.measure 返回单个 PerformanceMeasure 对象（不是数组）
performance.mark('modal-open');
performance.mark('modal-ready');
const measure = performance.measure('modal-cost', 'modal-open', 'modal-ready');
console.log('弹窗初始化耗时', measure.duration, 'ms');
```
