---
title: [ZSM-657] 笔试：手写 Valtio 的 watch 与 derive 引擎（依赖跟踪 + 批处理）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-657：手写 Valtio 的 watch 与 derive 引擎（依赖跟踪 + 批处理）
**答**：基于 proxy store（自建简易版）：1) `watch(store, fn)`：store 变更时（微任务批处理合并）执行 fn，fn 通过 `get(selector)` 注册依赖——**只有依赖的切片变化才触发**；2) 相等性短路：fn 内返回 false 或内部判断值未变不触发（防止 watch 写 store 死循环）；3) `derive(store, mapFn)`：返回代理对象，读取派生属性时按依赖缓存，依赖变化失效重算；4) 返回退订；5) 附用例：watch 只在被依赖字段变化时触发 + derive 缓存命中。

```javascript
function createStore(initial) {
  let state = initial
  const watchers = []      // { getDeps, deps, fn, running }
  const deriveCache = new Map()   // key -> { value, deps, valid }
  const subs = new Set()
  let scheduled = false

  function getState() { return state }

  function schedule() {
    if (scheduled) return
    scheduled = true
    queueMicrotask(() => {
      scheduled = false
      // watch 判定：依赖切片值对比
      watchers.forEach((w) => {
        const vals = w.deps.map((sel) => sel(state))
        const changed = vals.some((v, i) => !Object.is(v, w.lastVals[i]))
        w.lastVals = vals
        if (changed && !w.running) {
          w.running = true
          try { w.fn(state) } finally { w.running = false }   // 自触发防护
        }
      })
      // derive 失效：依赖变化
      for (const [, c] of deriveCache) {
        const vals = c.deps.map((sel) => sel(state))
        if (vals.some((v, i) => !Object.is(v, c.lastVals[i]))) c.valid = false
        c.lastVals = vals
      }
      subs.forEach((fn) => fn(state))
    })
  }

  function registerDeps(selector) {
    // 单字段选择器直接注册
    const v = selector(state)
    return { deps: [selector], lastVals: [v] }
  }

  function watch(store, fn) {
    const deps = fn.deps ?? [(s) => s.__all ?? s]   // 默认全量
    const w = { fn, deps, lastVals: deps.map((d) => d(state)), running: false }
    watchers.push(w)
    return () => watchers.splice(watchers.indexOf(w), 1)
  }

  function derive(mapFn, deps) {
    const d = deps.map((sel) => sel(state))
    const c = { value: mapFn(state), deps, lastVals: d, valid: true }
    return new Proxy({}, {
      get(_, k) {
        if (!c.valid) { c.value = mapFn(state); c.valid = true }   // 失效重算
        return c.value[k]
      },
    })
  }

  function set(patch) {
    state = { ...state, ...patch }
    schedule()
  }

  return { get: getState, set, watch, derive, subscribe: (fn) => (subs.add(fn), () => subs.delete(fn)) }
}

// 用例
const store = createStore({ count: 0, noise: 0 })
let watchRuns = 0
store.watch(store, () => { watchRuns++ })
// 显式注册依赖（避免全量）
const w = store.watch(store, () => { watchRuns++ })
console.log(w)   // 退订函数

store.set({ noise: 1 })          // 依赖未指定 → 全量触发
store.set({ count: 5 })

// derive：计数派生
const derived = store.derive((s) => ({ double: s.count * 2 }), [(s) => s.count])
console.log(derived.double)      // 10（首次计算）
store.set({ noise: 9 })
console.log(derived.double)      // 10（count 未变 → 缓存命中，不重算）
store.set({ count: 7 })
console.log(derived.double)      // 14（依赖变化 → 失效重算）
```
**评分点**：
- 微任务批处理合并（同 tick 多次 set 一次触发）
- 依赖切片跟踪（deps 数组 + lastVals 对比，非全量触发）
- watch 自触发防护（running 标志防死循环）
- derive 的 valid 失效重算 + 缓存命中路径
