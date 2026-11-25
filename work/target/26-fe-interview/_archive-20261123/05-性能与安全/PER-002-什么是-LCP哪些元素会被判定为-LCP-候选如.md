---
title: [PER-002] 什么是 LCP？哪些元素会被判定为 LCP 候选？如何优化？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-002：什么是 LCP？哪些元素会被判定为 LCP 候选？如何优化？

**答**：
- LCP 是视口内**最大的图片或文本块**完成渲染的时间点，良好阈值 2.5s。
- 候选元素包括：`<img>`、`<video>` 封面帧、带背景图的块级元素、包含文本节点的块级元素；候选会随渲染更新，最终值取最后一次。
- 优化方向：LCP 图片用 `preload` 提前加载、`fetchpriority="high"` 提升优先级；不要给 LCP 元素加懒加载；服务端 TTFB 要快；避免首屏字体阻塞文本渲染。
- 观测时注意 `buffered: true`，否则会漏掉 observer 注册前的记录。

```javascript
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const last = entries[entries.length - 1]; // 候选元素会多次更新，取最后一次为准
  console.log('LCP 耗时', last.startTime, 'ms');
  console.log('LCP 元素', last.element?.tagName, last.url || '');
}).observe({ type: 'largest-contentful-paint', buffered: true });
```
