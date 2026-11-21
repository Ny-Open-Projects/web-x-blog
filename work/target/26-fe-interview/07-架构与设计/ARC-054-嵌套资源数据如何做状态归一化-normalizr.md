---
title: [ARC-054] 嵌套资源数据如何做状态归一化（normalizr 思想）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-054：嵌套资源数据如何做状态归一化（normalizr 思想）？
**答**：
- 后端返回嵌套对象（订单含用户含商品）时，直接存会导致同一实体多份拷贝、更新需全量刷新。
- 归一化：按实体类型（order/user/product）拍平成 `{ byId, allIds }`，关联处只存 id，更新 O(1) 且天然去重。
- 权衡：归一化增加写复杂度与 selector 成本，适合实体被多视图共享的中后台；一次性展示的嵌套数据不必归一化。

```typescript
// 输入（嵌套）→ 归一化存储
const orderSchema = { user: 'user', items: [{ product: 'product' }] };
const normalized = normalize(apiOrder, orderSchema);
// { entities: { order: {o1:{...}}, user: {u1:{...}}, product: {p1:{...}} }, result: 'o1' }

interface NormalizedState<T> { byId: Record<string, T>; allIds: string[]; }

function normalize<T extends { id: string }>(list: T[]): NormalizedState<T> {
  return {
    byId: Object.fromEntries(list.map(e => [e.id, e])),
    allIds: list.map(e => e.id),
  };
}

// 更新一个用户，所有引用它的订单视图自动生效（单一事实源）
function updateUser(state: { users: NormalizedState<User> }, user: User) {
  return { ...state, users: { ...state.users, byId: { ...state.users.byId, [user.id]: user } } };
}
// selector 再做反查组装视图模型，缓存依赖 byId 引用
```
