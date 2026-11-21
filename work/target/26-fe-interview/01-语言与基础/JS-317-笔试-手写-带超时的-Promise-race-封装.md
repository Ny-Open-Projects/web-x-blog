---
title: [JS-317] 笔试：手写带超时的 Promise 封装
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-317：笔试：带超时的 Promise 封装

**题目**：实现 `withTimeout(promise, ms)`：超时 reject TimeoutError；失败原因不被吞；补充 `withTimeoutValue(p, ms, fallback)` 超时返回默认值不 reject；说明「超时后原任务仍在跑」的问题与解法。

**答**：
```javascript
class TimeoutError extends Error { name = 'TimeoutError'; }

function withTimeout(p, ms) {
  let timer;
  const timeout = new Promise((_, rej) => {
    timer = setTimeout(() => rej(new TimeoutError(`超过 ${ms}ms`)), ms);
  });
  return Promise.race([p, timeout]).finally(() => clearTimeout(timer)); // 清理防泄漏
}

function withTimeoutValue(p, ms, fallback) {
  return withTimeout(p, ms).catch(e => {
    if (e instanceof TimeoutError) return fallback;
    throw e; // 业务错误仍要抛
  });
}

// 用法
const data = await withTimeout(fetch('/api').then(r => r.json()), 3000);
const cfg = await withTimeoutValue(loadConfig(), 500, DEFAULT_CONFIG);
```
```javascript
// 进阶：超时后真正终止任务（fetch 用 AbortController）
async function fetchWithTimeout(url, ms) {
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), ms);
  try {
    return await fetch(url, { signal: ctl.signal });
  } finally {
    clearTimeout(t);
  }
}
```

**评分点**：
- Promise.race 模型 + finally 清理 timer（不清会泄漏悬挂 reject）——核心
- TimeoutError 类型化区分超时与业务错误
- withTimeoutValue 的降级语义（catch 里过滤类型）
- 进阶：AbortController 真正终止任务（race 只是「不再等待」的说明，加分）
