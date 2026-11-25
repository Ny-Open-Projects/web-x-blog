---
title: [ZSM-477] 笔试：手写状态机 guard 与延迟事件
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-477：手写状态机 guard 与延迟事件
**答**：实现增强版 FSM：1) 转移可带 guard：`(ctx) => boolean`，guard 不过则事件被拒绝（状态不变，返回 rejected）；2) 延迟事件：`after: ms` 定义的自动转移（进入状态后计时，离开状态取消计时）；3) 多个事件匹配同一状态时按定义顺序取第一个 guard 通过的；4) 延迟事件与显式事件竞态：显式事件先到则延迟计时取消；5) `send(event)` 返回 { changed, from, to, rejectedBy? }；6) 进入/离开钩子（onEnter/onExit）。

```javascript
export function createMachine({ initial, states, context = {} }) {
  let current = initial
  let ctx = { ...context }
  let timer = null
  const listeners = new Set()

  function enter(name) {
    const st = states[name]
    st.onEnter?.(ctx)
    if (st.after) timer = setTimeout(() => send(st.after.event), st.after.ms)   // 延迟事件
  }

  function send(event, payload) {
    const st = states[current]
    const candidates = (st.on?.[event] ?? [])
      .map((t) => typeof t === 'string' ? { target: t } : t)
    for (const t of candidates) {
      if (t.guard && !t.guard(ctx, payload)) continue       // guard 不过试下一个
      if (timer) { clearTimeout(timer); timer = null }      // 显式事件取消延迟计时
      states[current].onExit?.(ctx)
      const from = current
      current = t.target
      ctx = t.assign ? { ...ctx, ...t.assign(ctx, payload) } : ctx
      enter(current)
      const result = { changed: true, from, to: current, rejectedBy: null }
      listeners.forEach((fn) => fn(result))
      return result
    }
    const rejected = { changed: false, from: current, to: current, rejectedBy: 'guard' }
    listeners.forEach((fn) => fn(rejected))
    return rejected
  }

  enter(current)
  return { send, get state() { return current }, get context() { return ctx },
    onChange: (fn) => (listeners.add(fn), () => listeners.delete(fn)) }
}

// 用法：支付 FSM + 超时
const fsm = createMachine({
  initial: 'idle',
  states: {
    idle: { on: { SUBMIT: [{ target: 'paying', guard: (c) => c.amount > 0 }] } },
    paying: { after: { ms: 120_000, event: 'TIMEOUT' }, on: { SUCCESS: 'success', TIMEOUT: 'timeout' } },
    success: {}, timeout: { on: { RETRY: 'paying' } },
  },
  context: { amount: 0 },
})
```
**评分点**：
- guard 拒绝语义（顺序尝试下一个转移，全拒绝返回 rejectedBy）
- after 延迟事件的计时生命周期（进入启动、离开取消、显式事件竞态处理）
- assign 上下文更新与 onEnter/onExit 钩子
- send 返回值结构化（changed/from/to/rejectedBy）可测试
