---
title: [ALG-179] 用户反馈"点搜索后卡 1 秒才出结果"。如何用 PerformanceObserver 检测长任务（>50ms）并归因到具体路由与交互？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-179：用户反馈"点搜索后卡 1 秒才出结果"。如何用 PerformanceObserver 检测长任务（>50ms）并归因到具体路由与交互？
**答**：`PerformanceObserver` 观察 `longtask` 类型，duration 超过 50ms 即长任务；entry 的 startTime 定位发生时刻、duration 量化阻塞时长、attribution 提供 container 上下文（如 iframe）。归因策略：记录窗口期内的交互事件（click/input），把长任务匹配到最近一次交互上（INP 的思路）。注意 buffered: true 拿注册前的记录，Safari 不支持 longtask 需降级 rAF 间隔估算。

```javascript
const pendingInteraction = { name: null, ts: 0 };
// 记录最近一次交互，用于把长任务归因到交互
['click', 'keydown'].forEach(ev =>
  document.addEventListener(ev, e => {
    pendingInteraction.name = ev; pendingInteraction.ts = performance.now();
  }, { capture: true, passive: true }));
new PerformanceObserver(list => {
  for (const entry of list.getEntries()) {
    // duration 超过 50ms 即长任务，归因到窗口期内的最近交互
    if (entry.startTime - pendingInteraction.ts < 2000) {
      report({
        metric: 'longtask',
        duration: Math.round(entry.duration),
        route: location.pathname,
        interaction: pendingInteraction.name, // 点击后卡顿 => 搜索按钮的问题
      });
    }
  }
}).observe({ type: 'longtask', buffered: true });
```
