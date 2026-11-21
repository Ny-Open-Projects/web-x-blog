---
title: [BAS-147] 什么是 Promise 链的"值穿透"？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-147：什么是 Promise 链的"值穿透"？
**答**：
- then/catch/finally 传入非函数参数时，不会处理值，而是把上游的值或失败状态原样透传给下一个函数型回调。
- 典型表现：`.then(1)` 之后的 then 拿到的还是上游的值；rejected 状态会一直穿透到第一个 catch。
- 用途：catch(null) 式的占位、条件化组装链时跳过某几步。

```javascript
Promise.resolve('v')
  .then(1)                                  // 非函数，值穿透
  .then(null)
  .then(v => console.log(v));               // v —— 透传到第一个函数型 then

Promise.reject(new Error('skip'))
  .then(() => console.log('不会执行'))
  .catch(e => console.log('失败也穿透', e.message)); // 跳过 then 直达 catch
```
