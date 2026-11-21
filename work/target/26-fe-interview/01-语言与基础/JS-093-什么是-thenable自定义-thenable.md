---
title: [JS-093] 什么是 thenable？自定义 thenable 对象有哪些行为与陷阱？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-093：什么是 thenable？自定义 thenable 对象有哪些行为与陷阱？

**答**：
- thenable：任何带 `then(resolve, reject)` 方法的对象，Promise 会递归展开它。
- resolve 状态锁定：then 内多次调用 resolve 只有第一次生效（Promise 状态不可逆）。
- 展开是异步的且会继续展开返回的 thenable，直到拿到普通值或抛错。
- 自引用 thenable 会触发原生 Promise 的死循环保护，reject 一个 TypeError。

```javascript
// 1. Promise 自动展开 thenable
const thenable = {
  then(resolve, reject) { setTimeout(() => resolve(42), 50); },
};
Promise.resolve(thenable).then((v) => console.log('展开得到', v)); // 42

// 2. 状态锁定：后续 resolve 全部无效
const multi = {
  then(resolve) {
    resolve(1);
    resolve(2);                          // 无效
    setTimeout(() => resolve(3), 0);     // 依旧无效
  },
};
Promise.resolve(multi).then((v) => console.log('只拿一次', v)); // 1

// 3. then 内抛错 → 整体 rejected
Promise.resolve({
  then(_resolve, reject) { reject(new Error('then 内报错')); },
}).catch((e) => console.log('捕获', e.message)); // then 内报错

// 4. 自引用 thenable：原生 Promise 有循环保护
const selfRef = {};
selfRef.then = (resolve) => resolve(selfRef); // resolve 自己 = 死循环
Promise.resolve()
  .then(() => selfRef)
  .catch((e) => console.log('保护触发', e instanceof TypeError)); // true
```
