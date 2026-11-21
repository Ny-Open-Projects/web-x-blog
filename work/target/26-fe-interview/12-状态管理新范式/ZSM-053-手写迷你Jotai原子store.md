---
title: [ZSM-053] 笔试：手写一个迷你 Jotai（atom + useAtom + 简单派生）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-053：手写一个迷你 Jotai（atom + useAtom + 简单派生）

**题目要求**：
- 实现 `atom(init)`：初始值或 read 函数（`get => value`）。
- 实现 `useAtomValue(atom)`：读取并订阅，派生 atom 依赖变化时重算。
- 实现 `useSetAtom(atom)`：写基础 atom（传值或函数）；写派生 atom 需实现写函数 `atom(read, write)` 的 write 分支。
- 依赖追踪：read 函数里 get 了哪些 atom，就订阅哪些。

```javascript
import { useSyncExternalStore, useCallback } from 'react'

function atom(read, write) {
  return { init: typeof read !== 'function' ? read : null, read, write }
}

const globalStore = (() => {
  const values = new Map()     // atom → 当前值
  const deps = new Map()       // atom → Set(依赖 atom)
  const listeners = new Map()  // atom → Set(fn)

  const notify = a => (listeners.get(a) ?? []).forEach(fn => fn())
  const getDep = (a) => {
    if (!values.has(a)) {      // 首次计算
      if (a.read && typeof a.read === 'function' && a.init === null && a.write === undefined) {
        // 派生：记录依赖
        const read = a.read
        const depsSet = new Set()
        const proxyGet = dep => { depsSet.add(dep); return getDep(dep) }
        deps.set(a, depsSet)
        values.set(a, read(proxyGet))
        // 依赖变化 → 失效重算
        depsSet.forEach(dep => {
          const l = listeners.get(dep) ?? new Set()
          l.add(() => { values.delete(a); notify(a) })
          listeners.set(dep, l)
        })
        return values.get(a)
      }
      values.set(a, a.init)
    }
    return values.get(a)
  }
  const set = (a, v) => {
    const next = typeof v === 'function' ? v(getDep(a)) : v
    if (a.write) return a.write(proxyGet, set, next) // 派生写
    values.set(a, next); notify(a)
  }
  const subscribe = (a, fn) => {
    const l = listeners.get(a) ?? new Set()
    l.add(fn); listeners.set(a, l)
    return () => l.delete(fn)
  }
  return { getDep, set, subscribe, proxyGet: null }
})()

export const useAtomValue = a => useSyncExternalStore(
  cb => globalStore.subscribe(a, cb),
  () => globalStore.getDep(a),
)
export const useSetAtom = a => useCallback(v => globalStore.set(a, v), [a])
```

**评分点**：
- read 是函数且无 write 时按派生处理，首次读取才计算（惰性）。
- 依赖追踪：read 里 get 过的 atom 建立失效回调，依赖变化时删除派生缓存并通知。
- 基础 atom 的 set 支持值和函数两种入参。
- 订阅按 atom 粒度挂在 Map 上，取消订阅返回清理函数。
- 派生写（write 函数）能转发到目标 atom 的 set（答出可加分）。
