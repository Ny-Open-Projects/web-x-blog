---
title: [WCN-064] effect 的调度与批处理（batching）是怎么做的？为什么需要微任务队列？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-064：effect 的调度与批处理（batching）是怎么做的？为什么需要微任务队列？

**答**：
- 问题：一次事件里连续改 3 个 signal，若每次写入都立刻跑 effect，会执行 3 次（渲染 3 帧、读 3 次中间态）。
- 方案：写入不直接执行 effect，而是把 effect 放进微任务队列（Set 去重），当前同步代码跑完后统一 flush——这就是自动批处理；显式 `batch(fn)` 可把跨异步段也合并。
- flush 顺序：按依赖图拓扑——上游 computed 先于下游 effect，避免一个 effect 跑多次；实现上用 epoch/版本号判断"该 effect 在本批次是否已执行"。
- 深层原因：微任务在浏览器绘制前执行，所以批处理不影响同一帧内的视觉一致性；同时避免了同步递归（effect 内改 signal 再次触发 effect 的无限循环风险）。
- 边界：`effect` 内同步读自己的输出 signal 可能造成循环依赖，实现需检测并告警；flush 期间新写入会进入下一批。

```javascript
const queue = new Set();
let flushing = false;

function schedule(effect) {
  queue.add(effect);                    // Set 天然去重
  if (!flushing) {
    flushing = true;
    queueMicrotask(flush);              // 本同步段结束后统一执行
  }
}

function flush() {
  const batch = [...queue]; queue.clear();
  flushing = false;
  batch.sort((a, b) => a.#order - b.#order);   // 拓扑序（简化：注册序）
  for (const eff of batch) eff.run();
}

// 三个写入 → effect 只跑一次
batch(() => { a.value = 1; b.value = 2; c.value = 3; });
```
