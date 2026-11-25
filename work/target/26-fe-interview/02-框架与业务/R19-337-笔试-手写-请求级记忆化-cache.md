---
title: [R19-337] 笔试：手写请求级记忆化 cache(fn)（AsyncLocalStorage 模拟）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-337：笔试：手写请求级记忆化 cache(fn)
**答**：实现 `requestCache(fn)`：同一「请求作用域」内同参数调用只执行一次；不同请求互不共享（请求结束销毁）；用 AsyncLocalStorage 实现作用域。

```javascript
const { AsyncLocalStorage } = require('async_hooks')
const als = new AsyncLocalStorage()
function requestCache(fn) {
  return (...args) => {
    const store = als.getStore() // 每请求独立 Map
    if (!store) return fn(...args) // 无请求上下文直接执行
    const key = JSON.stringify(args)
    if (store.map.has(key)) return store.map.get(key)
    const p = fn(...args)
    store.map.set(key, p) // 缓存 promise（并发去重）
    return p
  }
}
function runInRequest(reqId, cb) {
  als.run({ reqId, map: new Map() }, cb)
}
// 服务端入口：runInRequest(req.id, () => renderPage())
// getUser = requestCache(async (id) => db.user(id))
// 同一请求内 getUser(1) 多次调用只查一次；不同请求各自独立
```
**评分点**：
- AsyncLocalStorage 建立请求级作用域（不是全局 Map——核心区别）。
- 缓存 promise（并发去重）而非结果。
- 无上下文降级直接执行。
- 请求结束 store 销毁，无跨请求泄漏。

## 变体与延伸（补充）

**变体与延伸**：

1. 为什么缓存 promise 而不是缓存结果？ → 并发场景下同一 key 的第二个调用在结果回来之前就到了，缓存结果会穿透重复请求；缓存 promise 才能把并发合并成一次。
2. AsyncLocalStorage 的上下文什么情况下会丢？ → 回调没走 als.run 的异步链（自己造的跨作用域 setTimeout、跨 worker 传递）就会丢；用全局单例 Map 则相反，会跨请求串数据。
3. 用 JSON.stringify(args) 当 key 有什么问题？ → 键序不同的同构对象会得到不同 key，函数与 undefined 会丢信息，循环引用直接抛错；生产上要用稳定序列化或参数规范化。
