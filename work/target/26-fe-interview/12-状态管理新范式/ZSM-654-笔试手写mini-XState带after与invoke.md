---
title: [ZSM-654] 笔试：手写 mini XState（状态机 + after 延时 + invoke 异步）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-654：手写 mini XState（状态机 + after 延时 + invoke 异步）
**答**：实现 `createMiniMachine(def)` 返回 runner：1) states/on/guard/entry/exit 基础迁移；2) `after: { ms: target }` 延时转移——离开状态自动清除定时器（重入状态重置，天然防抖）；3) `invoke: { src: asyncFn, onDone: target, onError: target }`——进入状态启动异步，离开自动取消（AbortController）；4) `send(event)` 返回是否迁移；5) 附用例：防抖搜索（INPUT 自迁移重置 after）与异步加载失败迁移。

```javascript
function createMiniMachine(def) {
  let current = def.initial
  let timers = []
  let aborts = []
  const subs = new Set()

  function clearTimers() { timers.forEach(clearTimeout); timers = [] }
  function abortInvokes() { aborts.forEach((a) => a.abort()); aborts = [] }

  function enter(name) {
    const node = def.states[name]
    node.entry?.()
    // after 延时转移
    if (node.after) {
      for (const [ms, target] of Object.entries(node.after)) {
        timers.push(setTimeout(() => transition(target), Number(ms)))
      }
    }
    // invoke 异步
    if (node.invoke) {
      const ac = new AbortController()
      aborts.push(ac)
      node.invoke.src({ signal: ac.signal })
        .then((output) => transition(node.invoke.onDone, { output }))
        .catch((e) => { if (e.name !== 'AbortError') transition(node.invoke.onError, { error: e }) })
    }
  }

  function transition(target, payload = {}) {
    clearTimers()
    const cur = def.states[current]
    cur.exit?.()
    abortInvokes()
    current = target
    enter(target)
    subs.forEach((fn) => fn(current, payload))
    return true
  }

  function send(type, payload = {}) {
    const node = def.states[current]
    const t = node.on?.[type]
    if (!t) return false
    if (t.guard && !t.guard(payload)) return false      // 守卫拒绝
    t.actions?.forEach((a) => a?.(payload))
    return transition(t.target ?? t, payload)
  }

  enter(def.initial)
  return { send, get: () => current, subscribe: (fn) => (subs.add(fn), () => subs.delete(fn)) }
}

// 用例1：防抖搜索（INPUT 自迁移重置 after）
const search = createMiniMachine({
  initial: 'idle',
  states: {
    idle: { on: { INPUT: { target: 'typing' } } },
    typing: {
      on: { INPUT: { target: 'typing' } },   // 自迁移 → 重置 after
      after: { 200: 'searching' },
    },
    searching: {
      invoke: {
        src: async ({ signal }) => { await new Promise((r, rej) => { const t = setTimeout(r, 50); signal.addEventListener('abort', () => rej(Object.assign(new Error('x'), { name: 'AbortError' }))); setTimeout(() => clearTimeout(t), 60) }); return ['a'] },
        onDone: 'idle',
        onError: 'error',
      },
    },
    error: {},
  },
})
search.send('INPUT')
search.send('INPUT')                       // 连续输入重置计时
await new Promise((r) => setTimeout(r, 300))
console.log(search.get())                  // 'searching' → 最终 done/error

// 用例2：守卫拒绝
const g = createMiniMachine({ initial: 'a', states: { a: { on: { GO: { target: 'b', guard: (p) => p.ok } } }, b: {} } })
console.log(g.send('GO', { ok: false }))   // false
console.log(g.send('GO', { ok: true }))    // true
```
**评分点**：
- after 离开清除 + 自迁移重置（防抖语义内建）
- invoke 用 AbortController 取消（离开状态 abort，错误区分 AbortError）
- guard 拒绝时不迁移不执行 actions
- 状态迁移通知订阅者（可观测）
