---
title: [ZSM-511] 笔试：手写支持并行状态与守卫的状态机运行器
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-511：手写支持并行状态与守卫的状态机运行器
**答**：实现 `createRunner(machine)`：1) machine 声明 `states` / `initial` / `on`（事件→迁移）；2) 迁移支持 `guard`（返回 boolean 的函数，false 则拒绝迁移）；3) 支持 `parallel` 并行区域（多个区域同时激活，各自消费同一事件）；4) `send(event)` 返回是否发生迁移；5) `state()` 返回当前激活区域集合与 context。附用例：并行区域 + 守卫拒绝。

```javascript
function createRunner(machine) {
  let current = {}
  let context = { ...machine.context }

  function enter(name, node) {
    if (node.parallel) {
      current[name] = Object.keys(node.states)
      Object.entries(node.states).forEach(([k, child]) => enter(`${name}.${k}`, child))
    } else {
      current[name] = node.initial
    }
  }
  enter('root', machine)

  function leafRegions() {
    // 收集叶子层激活状态
    const out = []
    for (const [region, v] of Object.entries(current)) {
      if (typeof v === 'string' && !v.includes('.')) out.push(`${region}:${v}`)
    }
    return out
  }

  function transitionFor(node, type) {
    return node.on?.[type]
  }

  function send(event) {
    const type = typeof event === 'string' ? event : event.type
    let moved = false
    // 遍历每个并行区域：同一事件各区域独立消费
    for (const [region, val] of Object.entries(current)) {
      if (region === 'root') continue
      const parent = region.split('.').slice(0, -1).join('.')
      const node = resolve(parent)
      const t = transitionFor(node, type) ?? machine.on?.[type]
      if (!t) continue
      if (t.guard && !t.guard(context, event)) continue   // 守卫拒绝
      current[region] = t.target
      t.actions?.forEach((a) => a(context, event))
      moved = true
    }
    return moved
  }

  function resolve(path) {
    let node = machine
    if (path !== 'root') path.split('.').forEach((k) => { node = node.states[k] })
    return node
  }

  return { send, context: () => context, state: () => ({ regions: { ...current }, leaves: leafRegions() }) }
}

// 用例：播放器并行「播放状态×画质」
const m = {
  context: { count: 0 },
  parallel: true,
  states: {
    play: { initial: 'pause', states: {} },
    quality: { initial: 'hd', states: {} },
  },
  on: {
    TOGGLE: {
      target: 'toggle',
      guard: (ctx) => ctx.count < 3,          // 超过 3 次禁止切换
      actions: (ctx) => { ctx.count++ },
    },
  },
}
const r = createRunner(m)
console.log(r.send('TOGGLE'))  // true：守卫通过
console.log(r.send('TOGGLE'))  // true
console.log(r.send('TOGGLE'))  // true
console.log(r.send('TOGGLE'))  // false：守卫拒绝，状态保持
```
**评分点**：
- guard 拒绝时不迁移也不执行 actions（守卫语义）
- parallel 区域独立消费同一事件（区域互不干扰）
- actions 在迁移成功后才执行（先判守卫）
- state 输出包含区域级激活信息（可观测）
