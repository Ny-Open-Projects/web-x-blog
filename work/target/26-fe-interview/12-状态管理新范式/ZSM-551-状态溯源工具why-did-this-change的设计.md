---
title: [ZSM-551] 状态溯源工具（why-did-this-change）的设计思路
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-551：状态溯源工具（why-did-this-change）的设计思路

**答**：
- 溯源要回答的问题：某字段在 t 时刻为什么变成了这个值——谁（调用栈）、因什么事件、从什么改成什么。只靠 DevTools 时间线翻历史效率极低，需要程序化的「变更索引」。
- 实现路径：在 store 的 setState 上包一层探针，每次变更记录 `{ seq, ts, path, prev, next, stack(前3帧), actionName }`。`path` 是浅 diff 得到的变更字段（一层为主，深字段记到两级），栈通过 `new Error().stack` 或 `captureStackTrace` 获取。
- 查询接口：`trace(key)` 返回该字段的所有变更时间线；`whoChanged(key, seq)` 返回某次变更的归因；配合 time travel 可直接跳到那次变更前后状态。
- 生产策略：探针只 dev 开启；生产用采样（1% 流量记录非 PII 字段）+ 压缩（只记 hash 差异），用于复现线上状态 bug。
- 追问钩子：React 18 严格模式下同一变更可能触发两次探针（double invoke），要按 seq 去重。

```javascript
function attachTracer(storeApi, options = {}) {
  const log = []
  const origSet = storeApi.setState
  storeApi.setState = (updater, replace, actionName) => {
    const prev = storeApi.getState()
    origSet(updater, replace, actionName)
    const next = storeApi.getState()
    // 浅 diff 定位变更字段
    const changed = []
    for (const k of new Set([...Object.keys(prev), ...Object.keys(next)])) {
      if (!Object.is(prev[k], next[k])) changed.push(k)
    }
    log.push({
      seq: log.length,
      ts: Date.now(),
      actionName: actionName ?? 'anonymous',
      changed,
      prev: Object.fromEntries(changed.map((k) => [k, prev[k]])),
      next: Object.fromEntries(changed.map((k) => [k, next[k]])),
      stack: new Error().stack.split('\n').slice(2, 5),
    })
    if (log.length > (options.max ?? 500)) log.shift()   // 环形截断
  }

  return {
    trace: (key) => log.filter((e) => e.changed.includes(key)),   // 字段时间线
    whoChanged: (key, seq) => log.find((e) => e.changed.includes(key) && e.seq === seq)?.stack,
  }
}

// 用法
const t = attachTracer(useCartApi)
t.trace('items')   // → [{ seq: 3, actionName: 'cart/addItem', ... }]
```
