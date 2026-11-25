---
title: [BAS-145] try/catch 能捕获异步错误吗？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-145：try/catch 能捕获异步错误吗？
**答**：
- 捕获不到回调型异步错误：setTimeout 里 throw 的错误发生在 try 块之外，只能靠 window.onerror 或进程级 uncaughtException。
- await 的拒绝发生在当前 async 函数作用域内，可以被 try/catch 捕获——这是 async/await 相对 then 链的最大工程优势。
- Promise 构造器内 throw 会被引擎转为 reject，不会变成未捕获异常。

```javascript
try {
  setTimeout(() => { throw new Error('async boom'); }, 0);
} catch (e) { console.log('抓不到'); }   // catch 执行时错误还没发生

async function run() {
  try { await Promise.reject(new Error('rejection')); }
  catch (e) { console.log('能抓到', e.message); }   // await 的拒绝可捕获
}
run();
```
