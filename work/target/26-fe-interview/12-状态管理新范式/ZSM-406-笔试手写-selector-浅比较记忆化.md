---
title: [ZSM-406] 笔试：手写 useSyncExternalStore + shallow selector Hook
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-406：手写 useSyncExternalStore + shallow selector Hook
**需求**：实现 `useShallowStore(store, selector)`：1) 基于 useSyncExternalStore 订阅外部 store；2) getSnapshot 返回 selector(state)——必须引用稳定（用缓存的上次结果，浅相等时不产生新引用）；3) shallow 比较：一层 key 逐个 Object.is；4) 订阅清理正确（useSyncExternalStore 自管）；5) selector 返回原始值时直接比较。

```javascript
import { useSyncExternalStore, useRef } from 'react'

function shallowEqual(a, b) {
  if (Object.is(a, b)) return true
  if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false
  const ka = Object.keys(a), kb = Object.keys(b)
  if (ka.length !== kb.length) return false
  return ka.every((k) => Object.is(a[k], b[k]))
}

export function useShallowStore(store, selector) {
  const cache = useRef({ input: undefined, output: undefined, has: false })

  const getSnapshot = () => {
    const state = store.getState()
    const output = selector(state)
    if (cache.current.has && shallowEqual(cache.current.output, output))
      return cache.current.output            // 浅相等 → 返回旧引用（稳定快照）
    cache.current = { output, has: true }
    return output
  }

  return useSyncExternalStore(store.subscribe, getSnapshot, getSnapshot)
}
```
**评分点**：
- getSnapshot 稳定性是生死线：浅相等必须返回同一引用（否则 React 无限重渲染）
- subscribe 直接透传 store.subscribe（返回退订函数的契约一致）
- SSR 第三参数 getServerSnapshot 传入（否则服务端渲染报错）
- selector 每次渲染执行的成本说明（selector 要便宜，昂贵派生上移）
