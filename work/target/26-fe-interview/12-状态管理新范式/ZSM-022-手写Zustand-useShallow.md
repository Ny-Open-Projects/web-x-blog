---
title: [ZSM-022] 笔试：手写 Zustand 的 useShallow selector 缓存
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-022：手写 Zustand 的 useShallow selector 缓存

**答**：
- 实现 `useShallowStore(store, selector)`：store 变化时执行 selector，对返回值做**第一层浅比较**，相等则返回上次引用，不触发重渲染。
- 返回的对象/数组要逐 key/逐项比较（Object.is）；嵌套对象只比引用。
- selector 在订阅期间应使用缓存避免每次都创建新对象。

**边界说明**：不考虑深比较；selector 可能返回原始值或对象/数组。

```javascript
import { useRef } from 'react'
import { useSyncExternalStore } from 'react'

const shallowEqual = (a, b) => {
  if (Object.is(a, b)) return true
  if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false
  if (Array.isArray(a) !== Array.isArray(b)) return false
  const ka = Object.keys(a), kb = Object.keys(b)
  if (ka.length !== kb.length) return false
  return ka.every(k => Object.is(a[k], b[k]))
}

export function useShallowStore(store, selector) {
  const cache = useRef({ has: false, value: undefined })
  const getSnapshot = () => {
    const next = selector(store.getState())
    if (cache.current.has && shallowEqual(cache.current.value, next)) {
      return cache.current.value // 命中：返回上次引用，React 不重渲染
    }
    cache.current = { has: true, value: next }
    return next
  }
  return useSyncExternalStore(store.subscribe, getSnapshot, getSnapshot)
}
```

**评分点**：
- 浅比较实现覆盖对象与数组、长度不等、值为 NaN（用 Object.is）等边界。
- 缓存必须命中时返回**旧引用**而非新对象，这是防重渲染的关键。
- getSnapshot 是纯函数式读取，配合 useSyncExternalStore 无 tearing。
- selector 每次 store 变化都会执行，但只有结果不等才更新缓存。

## 变体与延伸（补充）

**变体与延伸**：

1. 浅比较遇到 `NaN` 与 `-0` 表现如何 → `Object.is(NaN, NaN)` 为 true 判定相等，但 `Object.is(-0, 0)` 为 false，会多触发一次渲染，需说明是否接受。
2. 数组内容相同但顺序变了会重渲染吗 → 会，逐下标比较把 `[a,b]` 与 `[b,a]` 判为不等；业务上顺序无关时应换集合比较。
3. `getSnapshot` 里改 `useRef` 算副作用吗，SSR 下有问题吗 → 严格说是不纯读取，若 `getServerSnapshot` 复用同一函数会写 ref；服务端应单独返回纯函数结果。
