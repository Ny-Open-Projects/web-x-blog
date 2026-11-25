---
title: [ZSM-242] Vue 组件怎么直接消费 Zustand 的 vanilla store
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-242：Vue 组件怎么直接消费 Zustand 的 vanilla store

**答**：
- Zustand 的 `createStore()` 返回 vanilla API（getState/setState/subscribe），与 React 无耦合，Vue 用 shallowRef + subscribe 桥接即可
- 关键点：unsub 时机（onUnmounted）与引用触发（shallowRef 需要 replace 整个值或 triggerRef）
- 两个框架共享同一 store 实例时，React 侧用 useStore、Vue 侧用桥接 ref，写入口统一走 store.setState，保证单一真相源
- 这种「vanilla 核心 + 双适配」结构同样适用于迁移期（Vue 老页面渐进接 React 新模块）的场景

```javascript
import { createStore } from 'zustand/vanilla'
import { useStore } from 'zustand'          // React 侧
import { shallowRef, triggerRef, onUnmounted } from 'vue'

export const store = createStore(() => ({ count: 0 }))

// React: useStore(store)
export function useVueStore() {
  const ref = shallowRef(store.getState())
  const unsub = store.subscribe((s) => { ref.value = s; triggerRef(ref) })
  onUnmounted(unsub)
  return ref
}
```
