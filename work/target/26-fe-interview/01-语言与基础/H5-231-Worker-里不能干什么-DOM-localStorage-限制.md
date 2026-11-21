---
title: [H5-231] Worker 里不能干什么：DOM/localStorage 限制
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-231：Worker 里不能干什么：DOM/localStorage 限制

**答**：
- 不能碰的：DOM（document）、window、localStorage/sessionStorage、alert——它们被设计为单线程独占
- 能用的：fetch/XHR、WebSocket、IndexedDB（异步存储的合法替代）、caches、setTimeout/rAF（部分）、crypto、大量 JS 内置对象
- 设计动机：DOM 操作必须串行化到主线程才安全，Worker 的线程隔离从根上避免竞态
- 实战替代：Worker 需要 UI 数据时由主线程传过去；需要存储用 IndexedDB 异步 API
- 加分点：Worker 里有 navigator（部分子集，如 hardwareConcurrency 可用于决定 Worker 数量）、location（只读）

```javascript
// worker.js 里能/不能的边界
self.addEventListener('message', async ({ data }) => {
  // const el = document.querySelector(...)  ❌ ReferenceError
  const res = await fetch(data.url);          // ✅
  const db = await openIndexedDB();           // ✅ 异步存储
  postMessage(await res.json());
});
console.log(navigator.hardwareConcurrency);   // ✅ 决定 Worker 池大小
```
