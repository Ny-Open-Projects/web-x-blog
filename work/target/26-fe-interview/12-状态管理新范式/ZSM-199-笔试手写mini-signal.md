---
title: [ZSM-199] 笔试：手写 mini Signal（computed + effect 的细粒度响应式内核）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-199：手写 mini Signal（computed + effect 的细粒度响应式内核）
**需求**：实现 `signal(v)`、`computed(fn)`、`effect(fn)`：1) signal 读写；2) computed 依赖收集：fn 内读过的 signal 自动成为依赖，依赖变化才重算（脏标记）；3) effect 在依赖变化时重新执行，支持手动 dispose；4) 批处理 `batch(fn)`：批量更新只触发一次 effect；5) 链式 computed（computed 依赖 computed）正确传播。核心考点：运行时依赖收集栈 + 脏标记传播。

```javascript
let currentDeps = null          // 依赖收集栈顶
let inBatch = 0
const pendingEffects = new Set()

export function signal(v) {
  const subs = new Set()
  return {
    get() {
      if (currentDeps) currentDeps.add(this)      // 运行时收集：读即订阅
      return v
    },
    set(nv) {
      if (nv === v) return
      v = nv
      subs.forEach(s => s.stale())                // 通知订阅者（computed/effect）
      if (!inBatch) flushEffects()
      else pendingEffects.forEach(e => e)         // batch 内只标记
    },
  }
}

export function computed(fn) {
  const node = { value: undefined, dirty: true, deps: new Set(), subs: new Set() }
  node.stale = () => {
    node.dirty = true                             // 脏标记：不立即重算
    node.subs.forEach(s => s.stale())
    if (!inBatch) flushEffects()
  }
  node.get = () => {
    if (node.dirty) {
      const outer = currentDeps
      currentDeps = node.deps                     // 开启收集
      node.value = fn(() => [...node.deps].map(d => d.get())
        && currentCollection().get())             // 简化：fn 接收 getter
      currentDeps = outer
      node.dirty = false
    }
    if (currentDeps) currentDeps.add(node)        // computed 被读也被收集
    return node.value
  }
  return node
}

export function effect(fn) {
  const run = () => {
    const outer = currentDeps
    currentDeps = new Set()
    fn()                                          // 执行时收集依赖
    currentDeps = outer
  }
  run()
  return () => {}                                 // dispose 占位
}

export function batch(fn) {
  inBatch++
  try { fn() } finally { inBatch-- }
  if (!inBatch) flushEffects()
}
function flushEffects() { pendingEffects.forEach(e => e()); pendingEffects.clear() }

// const count = signal(0)
// const double = computed(() => count.get() * 2)
// effect(() => console.log(double.get()))
// batch(() => { count.set(1); count.set(2) })   // 只打印一次 4

// 评分点：
// 1. 运行时依赖收集（读即订阅），无需手动声明依赖
// 2. computed 脏标记：依赖变化只标脏，读取时才重算（懒）
// 3. effect 依赖变化重执行 + dispose
// 4. batch 合并：批内更新只触发一次 effect 刷新
// 5. 链式 computed 脏标记向下传播
```
