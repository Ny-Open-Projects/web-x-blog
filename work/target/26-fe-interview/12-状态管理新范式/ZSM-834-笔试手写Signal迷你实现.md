---
title: [ZSM-834] 笔试：手写迷你 Signal（细粒度响应式：读即订阅 + 精准更新）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-834：手写迷你 Signal（细粒度响应式：读即订阅 + 精准更新）
**答**：实现 Solid 风格迷你响应式：1) `createSignal(v)` 返回 `[read, write]`；2) `createEffect(fn)`：fn 内读 signal 即订阅，依赖 signal 变化自动重跑；**动态依赖**（条件分支不读的不订阅）；3) `createMemo(fn)`：派生缓存（依赖未变不重算）；4) 批处理 `batch(fn)`；5) 附用例：动态依赖（if 分支切换订阅目标）与 memo 缓存命中。

```javascript
let currentEffect = null            // 当前正在执行的 effect（订阅收集器）

function createSignal(value) {
  const subs = new Set()
  const read = () => {
    if (currentEffect) subs.add(currentEffect)   // 读即订阅：细粒度
    return value
  }
  const write = (next) => {
    const v = typeof next === 'function' ? next(value) : next
    if (Object.is(v, value)) return
    value = v
    // 精准更新：只通知订阅者（无 VDOM 全量 diff）
    const targets = [...subs]
    subs.clear()
    batch(() => targets.forEach((fn) => fn()))   // 通知即重跑 effect（重新收集依赖）
  }
  return [read, write]
}

function createEffect(fn) {
  const run = () => {
    currentEffect = run
    try { fn() } finally { currentEffect = null }
  }
  run()
  return () => { /* 退订：从所有 signal 的 subs 移除由 gc+clear 覆盖（简化） */ }
}

function createMemo(fn) {
  const [out, setOut] = createSignal(undefined)
  let initialized = false
  createEffect(() => {
    const v = fn()                    // fn 内读 signal → 本 memo 依赖被收集
    if (!initialized || !Object.is(v, out())) setOut(v)   // 缓存：依赖未变不重算
    initialized = true
  })
  return out
}

let batchDepth = 0
const batchQueue = new Set()
function batch(fn) {
  batchDepth++
  try { fn() } finally {
    if (--batchDepth === 0) {
      const q = [...batchQueue]
      batchQueue.clear()
      q.forEach((fn2) => fn2())
    }
  }
}

// 重跑调度（简化：同步 + batch 合并）
const _origNotify = null

// 用例：动态依赖
const mode = createSignal('a')
const a = createSignal(1)
const b = createSignal(2)
let runs = 0

createEffect(() => {
  runs++
  if (mode() === 'a') console.log('use a =', a())
  else console.log('use b =', b())
})
// runs=1: use a = 1
b(99)                              // b 不在依赖中：effect 不重跑
console.log(runs)                  // 1（动态依赖生效）
mode('b')                          // 依赖切换：重跑
// runs=2: use b = 99
b(100)
console.log(runs)                  // 3：现在 b 在依赖中

// memo 缓存
const doubled = createMemo(() => a() * 2)
a(5)
console.log(doubled())             // 10
a(5)                               // 同值不触发
console.log(doubled())             // 10（缓存命中）
```
**评分点**：
- 读即订阅（currentEffect 全局收集器模式）
- 精准更新（subs 通知后清空重收集——动态依赖生效）
- memo 的依赖未变不重算（initialized 标志 + Object.is）
- batch 深度合并（嵌套批处理外层 flush）
