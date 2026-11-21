---
title: [ZSM-061] Jotai 与 Valtio 的机制差异（pull vs proxy）分别适合什么场景？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-061：Jotai 与 Valtio 的机制差异（pull vs proxy）分别适合什么场景？
**答**：
- Jotai 是 pull 模型：组件订阅 atom，渲染时主动读值，订阅粒度 = atom；更新必须不可变替换。
- Valtio 是 proxy 模型：`useSnapshot` 读取时自动追踪「你用到了哪些字段」，set 直接改 proxy（可变写法），只通知用到被改字段的组件。
- Valtio 心智接近 Vue3 reactive，写法最省；代价是 Proxy 开销、解构快照需小心（snapshot 需用 useProxy/tracked）、性能上限受代理层影响。
- 选择：状态多而互相关联、想要显式依赖图 → Jotai；对象树深、想让组件「用到哪订阅哪」免 selector → Valtio。

```javascript
import { proxy, useSnapshot } from 'valtio'
const state = proxy({ cart: { items: [], user: 'a' } })

function Badge() {
  const snap = useSnapshot(state)
  return <b>{snap.cart.items.length}</b>   // 只订阅 items.length
}
// 写：直接改 proxy
state.cart.items.push(newItem)
```
