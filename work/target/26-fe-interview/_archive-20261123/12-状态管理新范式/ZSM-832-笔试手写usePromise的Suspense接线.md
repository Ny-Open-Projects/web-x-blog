---
title: [ZSM-832] 笔试：手写 use(Promise) 的简化实现（挂起/恢复/缓存去重）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-832：手写 use(Promise) 的简化实现（挂起/恢复/缓存去重）
**需求**：实现 `useThenable(promiseOrContext)`：1) promise 未完成时**抛出该 promise**（Suspense 接住）；完成时返回结果（缓存）；reject 时抛错误（ErrorBoundary 接）；2) **同一 Promise 只抛一次**（内部 status 缓存：pending/resolved/rejected——重复调用直接返回缓存值）；3) 支持 `use(Context)` 形态（对象有 `$$typeof: Symbol.for('react.context')` 时走 context 读取）；4) 附用例：挂起→恢复→二次读取不重复请求。

```javascript
import { useContext } from 'react'

function useThenable(thenable) {
  // Context 形态：React 19 的 use(Context) 统一
  if (thenable && thenable.$$typeof === Symbol.for('react.context')) {
    return useContext(thenable)
  }
  // Promise/Thenable 形态
  const t = thenable
  if (t == null || typeof t.then !== 'function') {
    throw new TypeError('use expects a thenable or context')
  }

  // status 缓存：同一 promise 只挂起一次
  if (t.__status === undefined) {
    t.__status = 'pending'
    t.__value = undefined
    t.then(
      (v) => { t.__status = 'resolved'; t.__value = v },   // 恢复：React 重试渲染
      (e) => { t.__status = 'rejected'; t.__value = e },   // 错误：ErrorBoundary
    )
  }

  switch (t.__status) {
    case 'pending':
      throw t                                  // 抛 promise：Suspense 兜住
    case 'rejected':
      throw t.__value                          // 抛错误：ErrorBoundary 兜住
    default:
      return t.__value                         // 缓存值：不重复请求
  }
}

// 用例（配合 Suspense 渲染验证语义）
let calls = 0
function fetchData() {
  calls++
  return new Promise((resolve) => setTimeout(() => resolve({ n: calls }), 10))
}

const cached = fetchData()                     // 稳定引用（组件外）

// 模拟三次渲染周期
function renderOnce() {
  try {
    return { type: 'data', value: useThenable(cached) }
  } catch (thrown) {
    if (thrown && typeof thrown.then === 'function') return { type: 'suspended' }
    return { type: 'error', value: thrown }
  }
}

// t1：挂起
let r1 = renderOnce()
console.log(r1.type)                           // 'suspended'
// promise resolve 后
await new Promise((r) => setTimeout(r, 20))
// t2/t3：恢复 + 缓存
let r2 = renderOnce()
let r3 = renderOnce()
console.log(r2.type, r3.type)                  // 'data' 'data'
console.log(r2.value === r3.value, calls)      // true 1：同一 promise 只请求一次
console.log(cached.__status)                   // 'resolved'
```
**评分点**：
- 抛 promise（pending）/抛 error（rejected）/返回缓存（resolved）三态
- __status 缓存挂载在 promise 上（同引用去重，跨渲染稳定）
- Context 形态统一（$$typeof 识别走 useContext）
- 组件外稳定引用的前提验证（calls === 1）
