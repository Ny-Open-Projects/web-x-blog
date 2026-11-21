---
title: [PER-034] 如何捕获未处理的 Promise 异常？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-034：如何捕获未处理的 Promise 异常？

**答**：
- Promise 链中没有被 `catch` 的拒绝会触发全局 `unhandledrejection` 事件，这是 Promise 时代的主要兜底。
- `event.reason` 是拒绝原因，可能是 Error 对象也可能是任意值，取堆栈时要判空。
- 上报后一般不要 `preventDefault()`，保留控制台报错便于本地调试。
- 典型来源：fetch 封装漏 catch、async 事件回调里没 try/catch。

```javascript
// 未被 catch 的 Promise 拒绝会触发全局 unhandledrejection
window.addEventListener('unhandledrejection', (event) => {
  const reason = event.reason;
  report('promise-rejection', { // report 为上报函数
    message: reason?.message || String(reason),
    stack: reason?.stack
  });
  // 上报后不调用 preventDefault，保留控制台默认报错方便调试
});

// 典型来源：then 链中没有接住任何一步的 reject
fetch('/api/user')
  .then((res) => res.json())
  .then((data) => render(data)); // 缺少 .catch，异常最终进入全局监听
```
