---
title: [JS-260] 复杂输出题：async 函数返回值与 await 的展开顺序
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 面试题
---

## JS-260：async 函数返回值与 await 的展开顺序

**答**：
- async 函数总是返回 Promise：返回原始值 → 包装成 resolved；返回 Promise → 等待其状态再 resolve（thenable 两次微任务）
- await 的调度：await 后的代码进入微任务；await 非 Promise 值也至少让出一次（微任务队列多走一轮）
- 嵌套计数：`await await p`（await 接 Promise 返回值仍是 Promise）比 `await p` 多轮微任务——高频考题
- return await 的差异：`return await p` 会多一轮 then 展开，且 try/catch 能捕获 p 的异常；`return p` 则异常逃到调用方

```javascript
async function a() { return 1; }
a().then(console.log); // 1（异步打印，同步代码后）

async function f() {
  const p = Promise.resolve('x');
  console.log(await p);        // 微任务 1 轮后打印
}
// await 接普通值也排队
async function g() { console.log(await 42); } // 同样异步执行

async function h() {
  try { return await Promise.reject(new Error('e')); } // 此处能 catch
  catch (e) { return 'caught'; }
}
```
