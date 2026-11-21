---
title: [JS-081] 如何手写 Promise.allSettled 与 Promise.any？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-081：如何手写 Promise.allSettled 与 Promise.any？

**答**：
- allSettled：全部结算后按原顺序返回 `{ status, value/reason }`，永远 resolve。
- any：第一个成功即 resolve，全部失败才 reject 一个 `AggregateError`，errors 按原顺序收集。
- 共同点：用计数器而不是 `Promise.all` 包装，避免一个失败打断整体流程。
- 注意入参可能是普通值，统一 `Promise.resolve(p)` 兜底。

```javascript
function allSettled(promises) {
  return new Promise((resolve) => {
    const list = Array.from(promises);
    const results = new Array(list.length);
    let count = 0;
    if (list.length === 0) return resolve([]);
    list.forEach((p, i) => {
      Promise.resolve(p).then(
        (value) => { results[i] = { status: 'fulfilled', value }; done(); },
        (reason) => { results[i] = { status: 'rejected', reason }; done(); }
      );
    });
    function done() { if (++count === list.length) resolve(results); }
  });
}

function any(promises) {
  return new Promise((resolve, reject) => {
    const list = Array.from(promises);
    const errors = new Array(list.length);
    let count = 0;
    if (list.length === 0) {
      return reject(new AggregateError([], 'All promises were rejected'));
    }
    list.forEach((p, i) => {
      Promise.resolve(p).then(resolve, (reason) => { // 第一个成功直接兑现整体
        errors[i] = reason;
        if (++count === list.length) {
          reject(new AggregateError(errors, 'All promises were rejected'));
        }
      });
    });
  });
}

allSettled([Promise.resolve(1), Promise.reject(new Error('e'))])
  .then(console.log); // [{status:'fulfilled',value:1},{status:'rejected',reason:Error}]
any([Promise.reject(new Error('x')), Promise.resolve('first ok')])
  .then(console.log); // first ok
```
