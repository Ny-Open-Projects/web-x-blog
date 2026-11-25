---
title: [ZSM-521] 笔试：手写 useShallow 的浅比较器与记忆化 selector 包装
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-521：手写 useShallow 的浅比较器与记忆化 selector 包装
**答**：实现三件事：1) `shallow(a, b)`：支持对象/数组/Map/Set 的浅相等（NaN 相等、+0/-0 区分可简化为 Object.is）；2) `memoSelector(selector)`：包装 selector，输入 state 引用没变直接返回缓存输出；变了才重算并用 shallow 与上次输出比对，浅相等也返回旧引用；3) `useShallowStore(store, selector)` hook：等价于 zustand 的 `useShallow`。附用例验证「新引用但浅相等」不再触发订阅回调。

```javascript
function shallow(a, b) {
  if (Object.is(a, b)) return true
  if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false
  if (a instanceof Map && b instanceof Map) {
    if (a.size !== b.size) return false
    for (const [k, v] of a) if (!b.has(k) || !Object.is(v, b.get(k))) return false
    return true
  }
  if (a instanceof Set && b instanceof Set) {
    if (a.size !== b.size) return false
    for (const v of a) if (!b.has(v)) return false
    return true
  }
  const ka = Object.keys(a), kb = Object.keys(b)
  if (ka.length !== kb.length) return false
  return ka.every((k) => Object.is(a[k], b[k]))
}

function memoSelector(selector) {
  let lastState, lastOut, hasOut = false
  return (state) => {
    if (hasOut && Object.is(state, lastState)) return lastOut   // 输入没变
    const out = selector(state)
    if (hasOut && shallow(out, lastOut)) { lastState = state; return lastOut } // 浅相等返回旧引用
    lastState = state; lastOut = out; hasOut = true
    return out
  }
}

function useShallowStore(store, selector) {
  return useSyncExternalStore(
    store.subscribe,
    memoSelector(selector),       // getSnapshot：保证引用稳定
    () => selector(store.getInitialState?.() ?? store.getState())
  )
}

// 用例
const sel = memoSelector((s) => ({ name: s.name, tags: s.tags.slice(0, 2) }))
const s1 = { name: 'a', tags: [1, 2, 3], noise: 1 }
const o1 = sel(s1)
const o2 = sel({ ...s1, noise: 2 })   // 关心字段没变
console.log(o1 === o2)                // true：浅相等复用旧引用，订阅不触发
```
**评分点**：
- shallow 覆盖对象/数组/Map/Set 且 Object.is 语义（NaN、±0）
- 双层缓存：输入引用级 + 输出浅相等级（两层都过才复用）
- getSnapshot 引用稳定性（React 订阅契约的核心）
- SSR 侧 getServerSnapshot 降级处理
