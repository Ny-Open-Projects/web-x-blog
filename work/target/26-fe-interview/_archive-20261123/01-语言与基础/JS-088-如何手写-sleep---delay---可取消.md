---
title: [JS-088] 如何手写 sleep / delay / 可取消的 timeout 包装？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-088：如何手写 sleep / delay / 可取消的 timeout 包装？

**答**：
- sleep：`new Promise(r => setTimeout(r, ms))`，是最基础的异步原语。
- delay：sleep 的函数版——延迟 n 毫秒后才执行原函数并透传参数。
- timeout 包装：race 一个定时器 reject，超时即抛错，finally 清理定时器。
- 可取消 sleep：暴露 cancel 句柄，取消时提前 resolve，用于竞态场景防止悬挂。

```javascript
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// 延迟执行版函数
function delay(fn, ms) {
  return async (...args) => {
    await sleep(ms);
    return fn(...args);
  };
}
delay((x) => console.log('delayed', x), 100)('hello'); // 100ms 后输出

// 可取消的 sleep：防止“等到超时才反应”的竞态
function cancellableSleep(ms) {
  let resolveFn, timer;
  const promise = new Promise((resolve) => {
    resolveFn = resolve;
    timer = setTimeout(resolve, ms);
  });
  return {
    promise,
    cancel() { clearTimeout(timer); resolveFn(); }, // 提前兑现
  };
}

(async () => {
  const s = cancellableSleep(5000);
  setTimeout(() => s.cancel(), 100); // 100ms 后取消
  await s.promise;
  console.log('没有等满 5 秒');
})();

// 超时包装：把“可能永远挂起”的操作限时
function timeout(promise, ms) {
  let timer;
  const limit = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(`操作超时 ${ms}ms`)), ms);
  });
  return Promise.race([promise, limit]).finally(() => clearTimeout(timer));
}
```

## 十三、异步编程深水区
