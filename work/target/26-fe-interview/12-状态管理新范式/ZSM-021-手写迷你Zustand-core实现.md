---
title: [ZSM-021] 笔试：手写一个迷你 Zustand（create + useStore 核心）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-021：手写一个迷你 Zustand（create + useStore 核心）

**答**：
- 实现 `create(initFn)`：内部维护 state、订阅集合，返回 hook；initFn 接收 `(set, get)`。
- set 支持 `部分对象浅合并` 和 `函数入参` 两种形式；组件卸载自动取消订阅。
- 保证并发渲染安全（使用 useSyncExternalStore）；重复渲染不因引用新对象而无限循环。

**边界说明**：不需要中间件、devtools、selector 浅比较；get 必须总是返回最新 state（异步回调可用）。

```javascript
import { useSyncExternalStore, useCallback } from 'react'

export function create(initFn) {
  let state
  const listeners = new Set()

  const setState = (partial, replace) => {
    const next = typeof partial === 'function' ? partial(state) : partial
    if (next === state) return            // 相同引用直接跳过
    state = replace ? next : { ...state, ...next } // 浅合并
    listeners.forEach(l => l())
  }
  const getState = () => state
  const subscribe = l => {
    listeners.add(l)
    return () => listeners.delete(l)      // 返回取消订阅
  }

  state = initFn(setState, getState)

  const api = { setState, getState, subscribe }
  function useStore(selector = s => s) {
    return useSyncExternalStore(
      subscribe,
      () => selector(state),              // 客户端快照：每次渲染重新执行 selector
      () => selector(state),
    )
  }
  useStore.getState = getState
  useStore.setState = setState
  useStore.subscribe = subscribe
  return useStore
}
```

**评分点**：
- 用 useSyncExternalStore（或等效订阅+快照方案），getSnapshot 每次返回当前 state 的 selector 结果。
- set 同时支持对象与函数入参，且是浅合并而非替换（除非 replace）。
- subscribe 返回取消函数，避免内存泄漏。
- 引用相等短路（next === state 直接 return），防止死循环。
- getState 闭包读取最新 state，异步回调中正确。

## 变体与延伸（补充）

**变体与延伸**：

1. selector 每次返回新对象，`useSyncExternalStore` 会死循环吗 → 会，getSnapshot 返回新引用被判定为变化；解法是只取原始值或套用 useShallow。
2. 想在 `setState` 之后同步拿到新 state（不等订阅回调）怎么办 → 先算 `next` 再赋值，`getState()` 立即返回新值，同一 tick 内读到的都是新的。
3. 多个 store 需要互相读写怎么办 → 不要在 initFn 里直接调另一个 store 的 set，改在 action 中显式调用或用订阅桥接，避免循环触发。
