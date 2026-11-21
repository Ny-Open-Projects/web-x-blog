---
title: [ALG-168] 面试题：`await Promise.resolve()` 与 `await setTimeout(0)` 之间改两次同一个 DOM，用户分别看到什么？微任务与渲染的关系是什么？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-168：面试题：`await Promise.resolve()` 与 `await setTimeout(0)` 之间改两次同一个 DOM，用户分别看到什么？微任务与渲染的关系是什么？
**答**：微任务在"当前宏任务结束 → 渲染之前"清空，所以 await Promise.resolve()（微任务）之间的两次 DOM 修改会被合并成一次渲染，用户只看到最终值；await setTimeout(0)（宏任务）中间隔了一次渲染，用户先看到 B 再看到 C。推论：需要在页面上有"中间态"必须用宏任务或 rAF 让出；纯微任务内多次改样式是零成本合并的。

```javascript
async function demo() {
  const el = document.getElementById('box');
  el.textContent = 'A';
  await Promise.resolve();            // 微任务：渲染前执行
  el.textContent = 'B';               // 用户永远看不到 A，只看到 B
  await new Promise(r => setTimeout(r, 0)); // 宏任务：中间发生了渲染
  el.textContent = 'C';               // 用户先看到 B，再看到 C
}
// 结论：微任务批量修改 => 一次渲染；需要中间帧必须让出主线程
// 常用让出手段：setTimeout(0) / requestAnimationFrame / requestIdleCallback
// queueMicrotask 只用于"本轮渲染前必须完成"的逻辑，如状态同步
```
