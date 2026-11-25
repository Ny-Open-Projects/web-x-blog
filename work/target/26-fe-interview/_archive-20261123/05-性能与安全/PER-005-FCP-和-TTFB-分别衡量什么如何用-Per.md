---
title: [PER-005] FCP 和 TTFB 分别衡量什么？如何用 PerformanceObserver 采集？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-005：FCP 和 TTFB 分别衡量什么？如何用 PerformanceObserver 采集？

**答**：
- TTFB：从发起导航请求到收到**响应首个字节**的时间，反映 DNS/TCP/TLS、服务端处理耗时，良好阈值小于 800ms。
- FCP：**第一个内容**（文本或图片）绘制到屏幕的时间，用户第一次"看到东西"，良好阈值小于 1.8s。
- TTFB 从 `navigation` 条目的 `responseStart` 读取；FCP 从 `paint` 条目读取。
- 两者配合分析：TTFB 高先优化服务端/CDN，TTFB 正常但 FCP 高则优化前端关键渲染路径。

```javascript
// TTFB：导航响应首个字节到达时间
new PerformanceObserver((list) => {
  const nav = list.getEntries()[0];
  console.log('TTFB', nav.responseStart, 'ms');
}).observe({ type: 'navigation', buffered: true });

// FCP：首个内容绘制时间
// 注意：PerformanceObserver.observe 不支持按 name 过滤，paint 类型会同时产出
// first-paint 与 first-contentful-paint，需要手动按 name 筛选
new PerformanceObserver((list) => {
  const fcp = list.getEntries().find((e) => e.name === 'first-contentful-paint');
  if (fcp) console.log('FCP', fcp.startTime, 'ms');
}).observe({ type: 'paint', buffered: true });
```
