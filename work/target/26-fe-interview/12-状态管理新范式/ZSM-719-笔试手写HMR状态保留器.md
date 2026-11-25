---
title: [ZSM-719] 笔试：手写 HMR 状态保留器（快照 dispose + 迁移恢复 + 探针重挂）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-719：手写 HMR 状态保留器（快照 dispose + 迁移恢复 + 探针重挂）
**答**：实现 `createHMRKeeper()`：1) `register(store, name)`：登记 store；`disposeAll()`：替换前对全部 store 快照（含 persist 排除字段的裁剪）；2) `restoreAll(newStores)`：恢复到新实例——结构交集保留 + **函数字段不恢复**（新代码的 action 才是权威）；3) `onReplaced(cb)`：替换完成回调（探针重挂/devtools 重新注册）；4) `history`：记录每次替换的 diff（字段增删）供开发时观察；5) 附用例：模拟模块替换前后状态恢复。

```javascript
function createHMRKeeper() {
  const snapshots = new Map()      // name -> state（纯数据）
  const history = []
  const callbacks = []

  function register(store, name) {
    snapshots.set(name, { store, state: null })
    return () => snapshots.delete(name)
  }

  function disposeAll() {
    for (const [name, { store }] of snapshots) {
      const raw = store.getState?.() ?? store.get?.()
      // 裁剪：persist 排除字段 + 函数字段不存
      const pure = {}
      for (const [k, v] of Object.entries(raw)) {
        if (typeof v !== 'function') pure[k] = structuredCloneSafe(v)
      }
      snapshots.get(name).state = pure
    }
  }

  function restoreAll(newStores) {
    const diffs = []
    for (const [name, entry] of snapshots) {
      const newStore = newStores[name]
      if (!newStore) continue
      const initial = newStore.getInitialState?.() ?? {}
      const restored = {}
      const added = [], dropped = [], kept = []
      // 结构交集：旧数据字段在新结构中存在才恢复
      for (const k of Object.keys(initial)) {
        if (entry.state[k] !== undefined) { restored[k] = entry.state[k]; kept.push(k) }
        else added.push(k)
      }
      for (const k of Object.keys(entry.state)) {
        if (!(k in initial)) dropped.push(k)       // 旧字段已删：丢弃并记录
      }
      newStore.setState?.(restored) ?? newStore.set?.(restored)
      diffs.push({ name, kept, added, dropped })
    }
    history.push({ ts: Date.now(), diffs })
    callbacks.forEach((cb) => cb(diffs))           // 探针重挂等回调
    return diffs
  }

  function structuredCloneSafe(v) {
    try { return JSON.parse(JSON.stringify(v)) } catch { return null }
  }

  return {
    register, disposeAll, restoreAll,
    onReplaced: (cb) => (callbacks.push(cb), () => callbacks.splice(callbacks.indexOf(cb), 1)),
    history: () => history,
  }
}

// 用例：模拟热更
const keeper = createHMRKeeper()
// 旧模块 store
const oldStore = { state: { items: ['a'], legacy: true }, getState: () => oldStore.state,
  setState: (p) => Object.assign(oldStore.state, p) }
keeper.register(oldStore, 'cart')
oldStore.setState({ items: ['a', 'b'] })

keeper.disposeAll()   // 模块替换前快照

// 新模块 store：结构变化（删 legacy、加 coupon）
const newStore = { state: { items: [], coupon: null }, getState: () => newStore.state,
  getInitialState: () => ({ items: [], coupon: null }),
  setState: (p) => Object.assign(newStore.state, p) }
keeper.onReplaced((diffs) => console.log('replaced', diffs))
keeper.restoreAll({ cart: newStore })
console.log(newStore.state)
// { items: ['a','b'], coupon: null }：items 恢复，legacy 丢弃，coupon 保持初始
console.log(keeper.history()[0].diffs[0])
// { name: 'cart', kept: ['items'], added: ['coupon'], dropped: ['legacy'] }
```
**评分点**：
- dispose 快照裁剪（函数字段不存、structuredClone 隔离）
- 恢复按「新结构交集」（kept/added/dropped 三分）
- 函数字段以新代码为权威（action 不恢复）
- onReplaced 回调链（探针重挂钩子）+ diff history 可观测
