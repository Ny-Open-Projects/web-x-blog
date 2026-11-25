---
title: [FRP-297] 笔试：手写框架无关 Store 内核（可接 React/Vue）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-297：笔试：手写框架无关 Store 内核
**答**：实现 createStore：`get()`/`set(patch)`/`subscribe(fn)`；set 用不可变合并；提供 `useStore(selector)`（React：useSyncExternalStore）与 Vue 版（customRef/computed）两个适配层，核心零框架依赖。

```javascript
// core（零依赖）
function createStore(initial) {
  let state = initial
  const subs = new Set()
  return {
    get: () => state,
    set(patch) {
      const next = typeof patch === 'function' ? patch(state) : { ...state, ...patch }
      if (Object.is(next, state)) return
      state = next
      subs.forEach(fn => fn(state))
    },
    subscribe(fn) { subs.add(fn); return () => subs.delete(fn) }
  }
}
// React 适配
function useStoreReact(store, selector) {
  return useSyncExternalStore(
    store.subscribe,
    () => selector(store.get()),
    () => selector(store.get())
  )
}
// Vue 适配
function useStoreVue(store, selector) {
  return customRef((track, trigger) => ({
    get() { track(); return selector(store.get()) },
    set() {}
  }))
}
```
**评分点**：
- 内核零框架依赖（发布订阅 + 不可变合并）。
- React 用 useSyncExternalStore（并发安全）。
- Vue 用 customRef/computed 桥接。
- selector 级订阅（防全 store 变更触发渲染）。
