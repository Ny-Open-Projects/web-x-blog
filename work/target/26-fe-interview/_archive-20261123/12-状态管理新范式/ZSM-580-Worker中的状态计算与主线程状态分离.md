---
title: [ZSM-580] Web Worker 里跑状态逻辑：主线程与 worker 的状态分离架构
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-580：Web Worker 里跑状态逻辑：主线程与 worker 的状态分离架构

**答**：
- 为什么要分离：大表计算、规则引擎、排序过滤这类重逻辑在主线程跑会阻塞渲染。架构上把「计算型状态」搬进 worker：主线程状态只存「UI 需要的投影」，worker 持有完整数据并执行 mutation。
- 协议：主线程发 `{ type: 'mutate', op, args, reqId }`，worker 处理后回 `{ type: 'result', reqId, state }`（或增量 patch）。关键决策是**全量快照 vs 增量 patch**：大状态全量 structuredClone 一次几毫秒，会抵消 worker 收益；用 Proxy 记录变更路径生成 patch 更优。
- 渲染接线：worker 回的 state 直接进 `useSyncExternalStore`（store 类放在主线程，值由 worker 回调填充）——对组件层完全透明。
- 时序与取消：reqId 配对响应；快速连续操作时前序请求要取消（worker 里检查 reqId 是否过期，过期结果直接丢弃，避免旧结果覆盖新输入）。
- 追问钩子：worker 里的状态不能被 React DevTools 看到——调试通道要把 worker 状态快照转发到主线程（window.__workerState 供 devtools 读取）。

```javascript
// worker.js
let state = { rows: [], filters: {} }
let latestReqId = 0

onmessage = (e) => {
  const { type, op, args, reqId } = e.data
  if (type === 'mutate') {
    latestReqId = reqId
    const next = compute(op, args, state)
    if (reqId !== latestReqId) return    // 已被更新的请求取代：丢弃
    state = next
    postMessage({ type: 'result', reqId, state })   // 全量（简单版）
  }
}

function compute(op, args, state) {
  switch (op) {
    case 'filter': return { ...state, filters: args, rows: filterRows(state.rows, args) }
    case 'sort':   return { ...state, rows: sortRows(state.rows, args) }
  }
}

// 主线程
const worker = new Worker('worker.js')

function createWorkerStore(initial) {
  let state = initial
  const subs = new Set()
  let reqId = 0
  worker.onmessage = (e) => {
    if (e.data.type !== 'result') return
    state = e.data.state
    subs.forEach((fn) => fn())
  }
  return {
    get: () => state,
    sub: (fn) => (subs.add(fn), () => subs.delete(fn)),
    mutate(op, args) {
      worker.postMessage({ type: 'mutate', op, args, reqId: ++reqId })   // 新请求自动作废旧结果
    },
  }
}
const store = createWorkerStore({ rows: [], filters: {} })

// 组件层无感接入
const rows = useSyncExternalStore(store.sub, store.get)
store.mutate('filter', { kw: 'a' })   // 计算在 worker，主线程不卡
```
