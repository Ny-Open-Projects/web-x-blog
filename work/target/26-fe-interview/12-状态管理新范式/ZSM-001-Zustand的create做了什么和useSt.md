---
title: [ZSM-001] Zustand 的 create 做了什么？和 useState/useContext 相比解决了什么问题？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-001：Zustand 的 create 做了什么？和 useState/useContext 相比解决了什么问题？
**答**：
- `create(fn)` 接收 `(set, get, api) => 初始 state`，返回一个 store 对象，本质是模块级的闭包 + 订阅集合（Map/Set）。
- store 暴露 `getState / setState / subscribe / destroy`，React 侧通过 `useSyncExternalStore` 订阅，状态在组件外，天然绕开 props 与 Context 的层层传递。
- 对比 useState：状态提升到模块级，任意组件直接读写，不需要父组件搬运；对比 Context：没有「一个值变了全树重渲染」的问题，selector 只订阅切片。
- 无 Provider 包裹，全局唯一 store 也可以用 `create` 工厂函数按需创建多个 store（如每个购物车实例一个）。
- 追问钩子：为什么不用 useEffect 同步？因为 useSyncExternalStore 保证了并发安全的一致快照。

```javascript
import { create } from 'zustand'

// fn 返回的对象就是初始 state；set 是浅合并（类似 this.setState）
const useCart = create((set, get) => ({
  items: [],
  total: 0,
  add(item) {
    // set 默认浅合并，只会替换指定 key，不会整个覆盖
    set(state => ({ items: [...state.items, item], total: get().total + item.price }))
  },
}))

// 任意组件直接用，无 Provider
function CartCount() {
  const count = useCart(s => s.items.length) // 只订阅 items.length
  return <span>{count}</span>
}
```
