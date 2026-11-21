---
title: [ZSM-303] 笔试：手写带 selector 订阅的 mini store
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-303：手写带 selector 订阅的 mini store
**需求**：实现 `createStore(init)`：1) `getState()`/`setState(patch)`（函数或对象，浅合并）；2) `subscribe(selector, listener, equalityFn?)`——仅当 selector 结果变化（默认 Object.is）时通知；3) 返回退订函数；4) 整树 setState 也必须先浅合并再比较；5) 提供与 useSyncExternalStore 对接的 getSnapshot 稳定性保证（未变更时返回同一引用）。

```javascript
export function createStore(init) {
  let state = init
  const subs = new Set()   // { selector, listener, equalityFn, prev }

  const setState = (patch) => {
    const next = typeof patch === 'function' ? patch(state) : patch
    const merged = { ...state, ...next }
    if (Object.is(merged, state)) return
    state = merged
    subs.forEach((sub) => {
      const nextVal = sub.selector(state)
      if (!sub.equalityFn(nextVal, sub.prev)) {
        const old = sub.prev
        sub.prev = nextVal
        sub.listener(nextVal, old)
      }
    })
  }

  const subscribe = (selector, listener, equalityFn = Object.is) => {
    const sub = { selector, listener, equalityFn, prev: selector(state) }
    subs.add(sub)
    return () => subs.delete(sub)
  }

  const getState = () => state          // 未变更时同引用 → getSnapshot 稳定
  return { getState, setState, subscribe }
}
```
**评分点**：
- prev 缓存 selector 结果，setState 时先比较再通知（避免 selector 无变化也触发）
- listener 通知前先更新 prev，且传出 (next, prev) 双值
- getSnapshot 稳定性：state 不变必须返回同一引用（useSyncExternalStore 会死循环检查）
- 退订从 Set 删除；浅合并语义与 Zustand 一致
