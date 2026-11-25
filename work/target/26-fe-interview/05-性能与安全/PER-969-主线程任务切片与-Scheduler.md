---
title: [PER-969] 主线程任务切片与 Scheduler.yield：怎么让长任务让路
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-969：主线程任务切片与 Scheduler.yield：怎么让长任务让路

**答**：
- 核心：把 >50ms 的任务切成 <50ms 片，片间让出主线程（yield）让输入/渲染优先，改善 INP。
- isInputPending 判断是否有待处理输入，有则提前让路；scheduler.postTask 按优先级排队。
- yield 语义：scheduler.yield() 返回 Promise，浏览器保证让出后本任务组仍以"延续"优先级回归，比 setTimeout(0) 更友好（不会被降级到队尾饿死）。
- 兜底：不支持时退化为 setTimeout(0) / MessageChannel。

```javascript
async function processInChunks(list, fn) {
  const out = [];
  for (let i = 0; i < list.length; i++) {
    out.push(fn(list[i]));
    if (i % 20 === 19) {                     // 每 20 项让一次
      if (scheduler?.yield) await scheduler.yield();
      else await new Promise(r => setTimeout(r));
    }
  }
  return out;
}
// INP 视角：每次让出点都是浏览器处理点击/滚动的机会，
// 长列表解析/搜索过滤都应套用
```
