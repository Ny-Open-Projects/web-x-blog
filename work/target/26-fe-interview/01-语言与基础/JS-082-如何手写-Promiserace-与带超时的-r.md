---
title: [JS-082] 如何手写 Promise.race 与带超时的 race？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-082：如何手写 Promise.race 与带超时的 race？

**答**：
- race：第一个结算（无论成败）的 promise 决定整体结果，其余被忽略但不会自动取消。
- 超时 race 是 race 最典型的应用：一个计时器 promise 与业务 promise 赛跑。
- 必须在 finally 里 clearTimeout，否则定时器泄漏、进程无法退出。
- race 不会真正“取消”慢的那一方，要彻底中断需配合 AbortController。

```javascript
function race(promises) {
  return new Promise((resolve, reject) => {
    for (const p of promises) Promise.resolve(p).then(resolve, reject); // 先到先得
  });
}

function withTimeout(promise, ms, label = 'timeout') {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(`${label}: ${ms}ms 内未完成`)), ms);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}

const slow = new Promise((r) => setTimeout(() => r('done'), 3000));
withTimeout(slow, 500, 'query').catch((e) => console.log(e.message)); // timeout: 500ms 内未完成

// race 与超时连用：多个镜像节点谁先返回用谁
race([withTimeout(fetch('/a'), 800, 'a'), withTimeout(fetch('/b'), 800, 'b')]);
```
