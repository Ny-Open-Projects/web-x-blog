---
title: [WEB-389] requestIdleCallback 和 Idle-time GC 是什么关系？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-389：requestIdleCallback 和 Idle-time GC 是什么关系？
**答**：
- 浏览器把空闲时段（无渲染/输入/动画任务）作为调度窗口：GC、编译、rIC 回调都在空闲期跑，deadline 内尽量完成，超时可打断。
- rIC 注意：不保证执行（可能一直忙），必须配 timeout 参数兜底；别在里面做 UI 更新或下次渲染依赖的工作。
- 适合任务：日志批量上报、缓存预计算、数据序列化等可中断/延后任务；React 的并发调度思想同源。

```javascript
requestIdleCallback((deadline) => {
  while (deadline.timeRemaining() > 1 && tasks.length) {
    tasks.shift()();          // 空闲分片执行
  }
  if (tasks.length) requestIdleCallback(arg); // 没做完续约
}, { timeout: 2000 });          // 兜底：最迟 2s 必须执行
console.log('空闲 = 无更高优先级任务的窗口');
```
