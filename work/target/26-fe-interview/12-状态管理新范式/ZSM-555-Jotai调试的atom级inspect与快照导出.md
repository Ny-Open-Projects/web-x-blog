---
title: [ZSM-555] Jotai 的 atom 级调试：inspect、快照导出与 store.get 的差异
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-555：Jotai 的 atom 级调试：inspect、快照导出与 store.get 的差异

**答**：
- 调试 Jotai 的难点：atom 是函数对象，没有名字（除非 `debugLabel`），依赖图是运行时动态的——调试 API 要解决「有哪些 atom、各自值多少、依赖谁」三个问题。
- `store.get(atom)`（v2 的 `getDefaultStore()`）：强制求值并缓存 atom，副作用是「读即创建」——调试面板扫 store 时会把惰性 atom 全部实例化，改变应用行为。调试要用「只读不改」的枚举 API 或白名单。
- `debugLabel`：给 atom 命名，devtools 面板与错误信息里可读；`atomWithDebugLabel` 或 `{ debugLabel }` 属性。团队规范：所有导出 atom 必须有 debugLabel（lint 规则可查）。
- 快照导出：`jotai-devtools` 的 JSON 导出依赖遍历 store 内部 atomState；自实现方案是用 WeakRef 建立注册表，业务代码 `registerDebugAtom(atom, label)` 手动登记，导出时逐个 `store.get` 并 diff 上次导出。
- 追问钩子：SSR 下 atom 值在每请求 store 里，调试要 attach 到请求作用域 store 而非 default store。

```javascript
import { getDefaultStore, atom } from 'jotai'

const store = getDefaultStore()

// 规范 1：debugLabel 全覆盖
export const cartCountAtom = atom(0)
cartCountAtom.debugLabel = 'cartCount'

// 规范 2：注册表式调试导出（避免「读即创建」扫全 store）
const registry = new Map()   // atom -> label
export function registerDebugAtom(a, label) { registry.set(a, label) }
registerDebugAtom(cartCountAtom, 'cartCount')

// 快照导出 + 与上次 diff
let lastSnap = null
export function debugSnapshot() {
  const snap = {}
  for (const [a, label] of registry) {
    try { snap[label] = store.get(a) } catch (e) { snap[label] = `<error: ${e.message}>` }
  }
  const diff = {}
  if (lastSnap) {
    for (const [k, v] of Object.entries(snap)) {
      if (!Object.is(lastSnap[k], v)) diff[k] = { prev: lastSnap[k], next: v }
    }
  }
  lastSnap = snap
  return { snap, diff }
}

// 直接订阅单个 atom 的变更（不经过组件）
store.sub(cartCountAtom, () => console.log('cartCount →', store.get(cartCountAtom)))
```
