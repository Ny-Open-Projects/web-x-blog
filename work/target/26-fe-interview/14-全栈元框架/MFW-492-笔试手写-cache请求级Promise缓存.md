---
title: [MFW-492] 笔试：手写 React cache() 请求级缓存语义
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-492：请求级 Promise 缓存（React cache() 语义）
**答**：实现 `createRequestCache()`：1) `wrap(fn)` 返回包装函数：同一请求上下文内同参数调用只执行一次（React cache() 的核心：Request Memoization 的用户级版本）；2) 缓存键 = fn.id + 稳定化参数（深序列化排序）；3) 缓存的是 **promise 本身**（调用方各自 await 同一 promise——不必等首次完成才能命中）；4) 请求结束 `clear()`（AsyncLocalStorage 挂钩演示：每个请求一个独立 store，不跨请求泄漏）。

```javascript
import { AsyncLocalStorage } from 'node:async_hooks'

const als = new AsyncLocalStorage()

export function createRequestCache() {
  function run(reqCtx, handler) { return als.run(new Map(), handler) } // 每请求一个 Map

  function wrap(id, fn) {
    return async (...args) => {
      const store = als.getStore()
      if (!store) return fn(...args) // 无请求上下文（构建期/脚本）直通
      const key = id + ':' + JSON.stringify(sortDeep(args))
      if (!store.has(key)) store.set(key, fn(...args)) // 缓存 promise 本身
      return store.get(key)
    }
  }
  return { run, wrap }
}

function sortDeep(v) {
  if (Array.isArray(v)) return v.map(sortDeep)
  if (v && typeof v === 'object')
    return Object.fromEntries(Object.keys(v).sort().map(k => [k, sortDeep(v[k])]))
  return v
}
```

**评分点**：
- 缓存 promise 而非结果（并发首调未完成也能被后续调用共享——关键差异点）
- AsyncLocalStorage 每请求隔离（请求 Memoization 不跨请求——泄漏即串数据）
- 键排序稳定化（同语义不同键序必须命中同一缓存）
- 无上下文直通（构建期调用不进请求缓存——两套生命周期）
