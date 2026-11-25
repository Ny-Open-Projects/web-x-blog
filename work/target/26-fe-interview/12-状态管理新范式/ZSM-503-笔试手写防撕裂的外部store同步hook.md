---
title: [ZSM-503] 笔试：手写防撕裂的外部 store 同步 hook
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-503：手写防撕裂的外部 store 同步 hook
**答**：不用 `useSyncExternalStore`，用 `useState + useEffect + useLayoutEffect` 手写一个 `useStoreValue(store, selector)`，要求：1) 订阅外部 store 并返回 selector 结果；2) 处理 getSnapshot 缓存问题（同一状态返回同一引用）；3) 撕裂兜底——layout effect 里发现快照与渲染值不一致时强制重渲；4) 支持卸载时退订。最后说明它与官方 `useSyncExternalStore` 的差距。

```javascript
import { useState, useEffect, useLayoutEffect, useRef, useCallback } from 'react'

function useStoreValue(store, selector) {
  const selectorRef = useRef(selector)
  selectorRef.current = selector

  // getSnapshot 必须稳定：缓存上次快照，状态没变返回同一引用
  const lastSnap = useRef({ state: store.getState(), slice: selector(store.getState()) })
  const getSnapshot = useCallback(() => {
    const state = store.getState()
    if (!Object.is(state, lastSnap.current.state)) {
      lastSnap.current = { state, slice: selectorRef.current(state) }
    }
    return lastSnap.current.slice
  }, [store])

  const [slice, setSlice] = useState(getSnapshot)

  // 撕裂兜底：commit 后核对，不一致就同步 setState 强制重渲
  useLayoutEffect(() => {
    const fresh = getSnapshot()
    if (!Object.is(fresh, slice)) setSlice(fresh)
  })

  useEffect(() => {
    let prevSlice = getSnapshot()
    return store.subscribe(() => {
      const next = getSnapshot()
      if (!Object.is(next, prevSlice)) {
        prevSlice = next
        setSlice(next)
      }
    })
  }, [store, getSnapshot])

  return slice
}

// 与官方差距：1) useSyncExternalStore 在订阅阶段由 React 协调，
// 并发渲染下用 getServerSnapshot 天然防撕裂，无需手动 layout 兜底；
// 2) 官方 subscribe 是「渲染绑定」的，不渲染也保持订阅一致；
// 3) 本实现二次渲染可能闪一帧，官方在订阅阶段就避免了。
```
**评分点**：
- getSnapshot 引用稳定性处理（不缓存会导致死循环）
- layout effect 撕裂兜底（commit 后核对快照）
- selector 变化用 ref 不重订阅（避免依赖抖动）
- 能说出与 useSyncExternalStore 的本质差距（订阅时机归 React 管、天然防撕裂）
