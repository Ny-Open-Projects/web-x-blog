---
title: [ZSM-526] 多选列表的状态用数组还是 Set 建模
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-526：多选列表的状态用数组还是 Set 建模

**答**：
- 结论：**Set 建模 + selector 转数组出口**。Set 的 has/add/delete 都是 O(1) 且天然去重，数组的高频操作 includes/splice 是 O(n) 且容易出重复项 bug。
- 状态入口用 Set：`selectedIds: Set<string>`，交互层直接 `add/delete/toggle`；展示层需要有序数组时在 selector 里 `[...set]`——注意这会每次产生新引用，须用 useShallow 或记忆化。
- 顺序语义：Set 保持插入序，多选场景「按点击顺序勾选」免费获得；若产品要求「按列表自然序」，selector 里对 Set 做一次按索引排序。
- 持久化注意：JSON.stringify 不支持 Set，持久层序列化时要 `[...set]` 转数组，rehydrate 时 `new Set(arr)` 还原（immer 的 enableMapSet 只管 Map/Set，不管持久化）。
- 追问钩子：万级以上选中项或需要区间选择（shift 点选），用 Set 存 id + 派生区间计算，比维护 index 数组稳得多。

```javascript
import { create } from 'zustand'
import { useShallow } from 'zustand/react/shallow'

const useSelection = create((set, get) => ({
  selectedIds: new Set(),
  order: [],                       // 列表自然序
  toggle: (id) => set((s) => {
    const next = new Set(s.selectedIds)
    next.has(id) ? next.delete(id) : next.add(id)   // 不可变更新 Set
    return { selectedIds: next }
  }),
  selectRange: (fromId, toId) => set((s) => {
    const next = new Set(s.selectedIds)
    const { order } = get()
    const a = order.indexOf(fromId), b = order.indexOf(toId)
    for (let i = Math.min(a, b); i <= Math.max(a, b); i++) next.add(order[i])
    return { selectedIds: next }
  }),
  clear: () => set({ selectedIds: new Set() }),
}))

// 展示出口：转数组 + 浅比较防新引用抖动
const selectedArr = useSelection(useShallow((s) => [...s.selectedIds]))
const count = useSelection((s) => s.selectedIds.size)
```
