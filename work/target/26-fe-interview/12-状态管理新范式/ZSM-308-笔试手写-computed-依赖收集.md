---
title: [ZSM-308] 笔试：手写简版 computed（运行时依赖收集）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-308：手写简版 computed（运行时依赖收集）
**答**：实现响应式系统 `signal(value)` 与 `computed(fn)`：1) `signal()` 返回读写器，写时通知；2) `computed` 首次读取时通过运行时依赖收集记录用到的 signal/computed；3) 任一依赖变化将 computed 标脏，下次读取时惰性重算；4) 依赖未变（值 Object.is 相同）不重算不传播；5) 不支持异步与循环（循环抛错）。

```javascript
let currentDeps = null

export function signal(initial) {
  const subs = new Set()
  let value = initial
  const read = () => {
    if (currentDeps) currentDeps.add(subs)    // 依赖收集
    return value
  }
  read.set = (v) => {
    if (Object.is(v, value)) return           // 值相等不传播
    value = v
    subs.forEach((run) => run())              // 通知依赖者标脏
  }
  return read
}

export function computed(fn) {
  const deps = new Set()
  const subscribers = new Set()
  let value, dirty = true
  const recompute = () => {
    if (!dirty) return value
    const prevDeps = currentDeps
    currentDeps = new Set()
    const prev = { ...tracking }               // 保留
    const saved = collectStack.pop()
    try {
      const result = fn()                      // 运行时收集 deps
      // 对比新旧依赖，退订失效的
      deps.forEach((s) => { if (!currentDeps.has(s)) s.delete(notify) ; })
      currentDeps.forEach((s) => s.add(notify))
      deps = currentDeps
      if (!Object.is(result, value)) { value = result; subscribers.forEach((f) => f()) }  // 结果稳定不传播
      dirty = false
      return value
    } finally { currentDeps = prevDeps }
  }
  const notify = () => { dirty = true; subscribers.forEach((f) => f()) }  // 标脏 + 向下传播
  const read = () => { if (currentDeps) currentDeps.add(subscribers); return recompute() }
  read.subscribe = (f) => (subscribers.add(f), () => subscribers.delete(f))
  return read
}
```
**评分点**：
- 运行时收集（读取时把订阅集合塞进 currentDeps），不是声明式依赖数组
- 惰性重算：标脏 ≠ 重算，读时才算
- 双重相等短路：signal 值相等不传播、computed 结果相等不向下游传播
- 依赖集合要支持动态更新（分支读取导致依赖集变化时退订旧依赖）
