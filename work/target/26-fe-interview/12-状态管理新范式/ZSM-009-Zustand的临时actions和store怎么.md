---
title: [ZSM-009] Zustand 的切片模式（slices pattern）怎么组织大 store？和单一大 store 有什么取舍？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-009：Zustand 的切片模式（slices pattern）怎么组织大 store？和单一大 store 有什么取舍？
**答**：
- 切片模式：按业务域把 state + actions 拆成多个 creator（如 cartSlice、userSlice），再用一个 `createStore(...slices)` 组合成一个 store，类型上通过 `StateCreator<Store, [], [], SliceA>` 互相引用。
- 好处：文件按域聚合、actions 可跨切片调用（cartSlice 里调 userSlice 的积分逻辑）、类型提示完整。
- 取舍：单一 store 简单但会膨胀；多 store 隔离彻底但跨域读写要互相 import；切片是「一个 store 内的模块化」，是中大型应用的主流折中。
- 注意 set 仍是整个 store 的浅合并，切片间天然共享，命名冲突要靠类型检查兜底。

```javascript
const createCartSlice = (set, get) => ({
  items: [],
  add: i => set(s => ({ items: [...s.items, i] })),
})
const createUserSlice = (set, get) => ({
  points: 0,
  // 跨切片：下单后扣积分
  checkout: () => {
    const count = get().items.length
    set(s => ({ points: s.points - count * 10 }))
  },
})
const useStore = create((...a) => ({ ...createCartSlice(...a), ...createUserSlice(...a) }))
```
