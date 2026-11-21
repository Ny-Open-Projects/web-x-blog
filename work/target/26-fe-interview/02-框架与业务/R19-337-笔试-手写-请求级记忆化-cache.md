---
title: [R19-337] 笔试：手写请求级记忆化 cache(fn)（AsyncLocalStorage 模拟）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-337：笔试：手写请求级记忆化 cache(fn)
**题**：实现 `requestCache(fn)`：同一「请求作用域」内同参数调用只执行一次；不同请求互不共享（请求结束销毁）；用 AsyncLocalStorage 实现作用域。

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
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-fb4f0066-c4aa-470f-81b2-38f517ebec12-cwd'; fi
exit "$__zcode_status"
