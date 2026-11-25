---
title: [JS-091] 如何用 AbortController 取消 fetch？级联取消怎么做？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-091：如何用 AbortController 取消 fetch？级联取消怎么做？

**答**：
- `controller.signal` 传给 fetch，`controller.abort()` 后请求立即中断并抛 AbortError。
- 超时取消是最常见用法：定时器到点调 abort，注意 abort 可以携带原因。
- 级联取消：多个请求共享同一个 signal，主控制器 abort 一次全部中断。
- 取消后所有依赖该任务的 await 都会以 AbortError 结束，需要按 `e.name === 'AbortError'` 区分业务错误。

```javascript
// 1. 单个请求：超时取消
async function fetchWithTimeout(url, ms) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(new DOMException('超时', 'TimeoutError')), ms);
  try {
    const res = await fetch(url, { signal: controller.signal });
    return await res.json();
  } catch (e) {
    if (e.name === 'AbortError') console.log('请求已取消');
    throw e;
  } finally {
    clearTimeout(timer);
  }
}

// 2. 级联取消：一个总开关控制一组请求
async function fetchAll(urls, budgetMs) {
  const parent = new AbortController();
  const timer = setTimeout(() => parent.abort(), budgetMs);
  try {
    return await Promise.all(
      urls.map((u) => fetch(u, { signal: parent.signal }).then((r) => r.json()))
    );
  } catch (e) {
    if (e.name === 'AbortError') console.log('整组请求被取消');
    throw e;
  } finally {
    clearTimeout(timer);
  }
}

// 3. 手动取消：用户切换页面时中断旧请求，避免过期响应覆盖新数据
let current;
function search(kw) {
  current?.abort();                    // 取消上一次
  current = new AbortController();
  return fetch(`/api?q=${kw}`, { signal: current.signal }).then((r) => r.json());
}
```
