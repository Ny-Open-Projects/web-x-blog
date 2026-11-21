---
title: [WCN-325] 选择性水合与元素优先级（交互区域先水）的调度？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-325：选择性水合与元素优先级（交互区域先水）的调度？
**答**：
- 优先级来源：交互命中区域 > 视口内 > 视口外（idle）。
- 实现：统一调度器按优先级队列逐个 import+注册（并发限流，防请求风暴）。
- 与框架协作：React 的选择性水合管 React 树；元素层有自己的调度——两者对齐（元素多在 React 边界内）。

```javascript
const queue = new PriorityQueue();
// interaction 命中 → P0；IntersectionObserver → P1；idle → P2
scheduler.pump(() => { const job = queue.pop(); return import(job.chunk); }, { concurrency: 3 });
r
```
