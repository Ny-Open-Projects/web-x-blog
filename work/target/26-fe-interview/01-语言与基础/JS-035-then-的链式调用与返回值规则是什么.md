---
title: [JS-035] then 的链式调用与返回值规则是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-035：then 的链式调用与返回值规则是什么？

**答**：
- then 返回**新 Promise**，因此可以链式续接；每个 then 独立注册成功/失败回调。
- 回调返回普通值 → 下一个 then 收到该值；返回 Promise → 被展开等待。
- 回调抛错 → 链条转入失败分支，最近的 catch 捕获。
- 返回值缺失时发生“值穿透”：非函数参数会被跳过并把值传给下一个 then。

```javascript
Promise.resolve(1)
  .then((v) => v + 1)                    // 返回普通值 2
  .then((v) => Promise.resolve(v * 10))  // 返回 Promise，被展开 → 20
  .then((v) => { throw new Error('boom'); }) // 抛错
  .catch((err) => 0)                     // 捕获并恢复 → 0
  .then('not a function')                // 值穿透，0 继续传递
  .then((v) => console.log(v));          // 0
```
