---
title: [BAS-144] async 函数的返回值是怎么被包装的？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-144：async 函数的返回值是怎么被包装的？
**答**：
- return 的值一律被 `Promise.resolve()` 包装；返回另一个 promise 时跟随它的最终状态。
- throw 等价于返回 rejected promise，错误会变成 Promise 拒绝而不是同步异常。
- 所以 `async fn()` 的结果永远可以安全地 .then/.catch。

```javascript
async function f() { return 1; }
f().then(console.log);              // 1 —— 返回值自动 Promise.resolve 包装

async function g() { return Promise.resolve(2); }
g().then(console.log);              // 2 —— 返回 promise 时跟随其状态

async function h() { throw new Error('x'); }
h().catch(e => console.log('rejected', e.message)); // throw 等价于 reject
```
