---
title: [OPT-031] Long Task 如何发现与拆分？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-031：Long Task 如何发现与拆分？

**答**：
- 超过 50ms 的主线程任务即 Long Task，会推迟输入响应（伤 INP）和渲染帧（掉帧）。
- 发现：`PerformanceObserver` 监听 `longtask`，结合 Performance 面板火焰图定位具体函数。
- 拆分思路：把大循环改成"分批 + 让出主线程"（每批处理若干项后 `setTimeout`/rAF 让出）；把纯计算移到 Web Worker。
- 检查清单：避免一次性 JSON.parse 大文件、同步排序大数组、批量 DOM 操作不合并。

```javascript
// 一一对应：longtask 观测 + 大任务分批拆分
// 1. 观测：记录所有超过 50ms 的任务及其耗时
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.warn('Long Task', Math.round(entry.duration), 'ms', entry.name);
  }
}).observe({ type: 'longtask', buffered: true });

// 2. 拆分：10 万条数据分批处理，每批让出主线程
async function processInBatches(items, batchSize = 1000) {
  for (let i = 0; i < items.length; i += batchSize) {
    processBatch(items.slice(i, i + batchSize)); // 本批约 5ms
    // 让出主线程：浏览器可处理输入与渲染，任务不再连续阻塞
    await new Promise((r) => setTimeout(r, 0));
  }
}
```
