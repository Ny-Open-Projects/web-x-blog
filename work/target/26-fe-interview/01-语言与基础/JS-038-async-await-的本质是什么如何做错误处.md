---
title: [JS-038] async/await 的本质是什么？如何做错误处理？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-038：async/await 的本质是什么？如何做错误处理？

**答**：
- async 函数返回 Promise，await 在其右侧等待 Promise，语法上是 generator + 自动执行器的封装。
- await 暂停当前 async 函数（不阻塞主线程），后续逻辑被注册为微任务。
- await 一个 rejected Promise 会抛出该原因，用 try/catch 或 `.catch` 捕获。
- 并发场景不要顺序 await，用 `Promise.all` 并行化。

```javascript
async function load() {
  try {
    const user = await fetch('/api/user').then((r) => r.json());
    // 串行：慢
    const orders = await fetch(`/api/orders?uid=${user.id}`).then((r) => r.json());
    return { user, orders };
  } catch (err) {
    console.error('load failed:', err);
    throw err; // 继续向上抛给调用方
  }
}

// 并行优化
async function loadFast() {
  const userP = fetch('/api/user').then((r) => r.json());
  const cfgP = fetch('/api/config').then((r) => r.json());
  const [user, cfg] = await Promise.all([userP, cfgP]); // 两个请求同时发出
  return { user, cfg };
}
```
