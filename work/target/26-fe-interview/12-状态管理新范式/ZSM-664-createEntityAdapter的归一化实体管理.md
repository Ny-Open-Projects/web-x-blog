---
title: [ZSM-664] RTK 的 createEntityAdapter：归一化实体的 CRUD 与 selector 生成
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-664：RTK 的 createEntityAdapter：归一化实体的 CRUD 与 selector 生成

**答**：
- createEntityAdapter 把「归一化实体管理」（ZSM-535 的思路）标准化：内部维护 `{ ids: EntityId[], entities: Record<id, T> }`（保持插入序/排序序的双结构），提供全套 CRUD（addOne/addMany/updateOne/removeOne/setAll/upsertMany）——全部是 immer draft 下的正确不可变实现，手写容易漏的点（更新后重排序、删除后 ids 清理）都处理了。
- 排序策略：`sortComparer: (a, b) => b.score - a.score`——**每次插入/更新后自动重排** ids；但重排是 O(n log n)，万级实体高频更新时改用「update 后手动重排」或切换到无排序 + selector 里排。
- selector 自动生成：`adapter.getSelectors((state) => state.users)` 产出 `selectById/selectAll/selectTotal/selectIds`——selectAll 返回按 ids 顺序的实体数组（引用稳定依赖 entities/ids 未变），这些就是手写归一化派生的标准答案。
- 与手写 Map 的对比：adapter 用 `Record<id, T>`（对象字典）而非 Map——序列化友好（persist/DevTools 直接可见），是「Redux 生态 = 可序列化」原则的体现。
- 追问钩子：`updateMany` 批量更新的原子性——一次 action 内多个更新合并为一次 immer 产出一轮通知，比多次 dispatch 更新省 N-1 轮订阅通知。

```javascript
import { createEntityAdapter, createSlice } from '@reduxjs/toolkit'

const usersAdapter = createEntityAdapter({
  selectId: (u) => u.id,
  sortComparer: (a, b) => b.score - a.score,   // 分数降序自动维护
})

const usersSlice = createSlice({
  name: 'users',
  initialState: usersAdapter.getInitialState({ loading: 'idle' }),
  reducers: {
    userAdded: usersAdapter.addOne,             // 自动插入 + 重排
    usersSet: usersAdapter.setAll,              // 全量替换（服务端同步）
    userUpdated: {
      reducer: usersAdapter.updateOne,          // { id, changes: {...} }
    },
    userRemoved: usersAdapter.removeOne,
  },
})

// selector 自动生成
const usersSelectors = usersAdapter.getSelectors((state) => state.users)
// usersSelectors.selectAll(state)  → 按 ids 排序的实体数组
// usersSelectors.selectById(state, 'u1')
// usersSelectors.selectTotal(state)

// updateMany 原子批量
dispatch(usersAdapter.updateMany(state, [
  { id: 'u1', changes: { score: 10 } },
  { id: 'u2', changes: { score: 20 } },
]))   // 一次产出：合并重排 + 一轮通知

// 与手写 Map 的取舍
// adapter（Record 对象）：可序列化、DevTools 可见 —— Redux 生态首选
// Map：高频 has/delete O(1) —— 序列化需转换，非 Redux 场景更顺手
```
