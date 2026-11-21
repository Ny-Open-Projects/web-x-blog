---
title: [OPT-059] 什么是微任务风暴？Promise 链过度如何造成渲染饥饿？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-059：什么是微任务风暴？Promise 链过度如何造成渲染饥饿？

**答**：
- 微任务在**当前宏任务结束前全部清空**才轮到渲染；一个宏任务里排入海量微任务（长 Promise 链、循环 await 已 resolve 的 Promise），浏览器就一帧都渲染不了，表现为点击无响应但 CPU 满。
- 典型场景：大数组每条数据都 `await Promise.resolve().then(step)` 串行处理——看似异步实则全在一个宏任务里。
- 排查方式：Performance 面板看到一个超长 Script 块但内部函数很碎，即微任务风暴。
- 修复方向：批间用**宏任务**让渡（setTimeout/scheduler.yield），或改同步循环消除无意义的 await。

```javascript
// 一一对应：微任务风暴的复现与两种修复
// 反例：10 万条数据逐条 then —— 全部微任务排进同一个宏任务，渲染被饿 1.2s+
async function storm(items) {
  for (const it of items) {
    await Promise.resolve();          // 每次 await 只让出微任务队列，不让出渲染
    it.result = compute(it);
  }
}

// 修复一：批处理 + 宏任务让渡（每 500 条 yield 一次真正的控制权）
async function chunked(items) {
  for (let i = 0; i < items.length; i += 500) {
    for (const it of items.slice(i, i + 500)) it.result = compute(it);
    await new Promise((r) => setTimeout(r, 0)); // 宏任务边界：浏览器可渲染/响应输入
  }
}

// 修复二：纯 CPU 计算直接同步循环，去掉假 await（最快）
function syncLoop(items) {
  for (const it of items) it.result = compute(it);
}

// 检测工具：观察帧间隔，连续 >200ms 说明有渲染饥饿
let last = performance.now();
function watchFrame() {
  const now = performance.now();
  if (now - last > 200) console.warn('疑似微任务风暴，帧间隔', Math.round(now - last), 'ms');
  last = now;
  requestAnimationFrame(watchFrame);
}
requestAnimationFrame(watchFrame);
```
