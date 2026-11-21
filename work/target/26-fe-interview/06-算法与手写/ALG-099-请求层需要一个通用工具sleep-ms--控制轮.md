---
title: [ALG-099] 请求层需要一个通用工具：`sleep(ms)` 控制轮询间隔；`withTimeout(promise, ms)` 给任意 Promise 加超时上限，超时即拒绝。如何用 Promise 竞态实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-099：请求层需要一个通用工具：`sleep(ms)` 控制轮询间隔；`withTimeout(promise, ms)` 给任意 Promise 加超时上限，超时即拒绝。如何用 Promise 竞态实现？
**答**：`sleep` 是定时器包装的 Promise。`withTimeout` 构造一个 ms 后 reject 的 Promise 与原 Promise `Promise.race`——谁先 settle 谁定结果；`finally` 里 `clearTimeout` 防止定时器泄漏。注意：超时只是"提前拒绝"，原 Promise 仍在跑，真正中断需要 AbortController 配合。时间 O(1)，空间 O(1)。

```javascript
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

function withTimeout(promise, ms, label = 'timeout') {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(label)), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}
// 组合用法：搜索节流 300ms 后发请求，5s 超时
async function searchWithTimeout(keyword, fetcher) {
  await sleep(300);
  return withTimeout(fetcher(keyword), 5000, 'request timeout');
}
```
