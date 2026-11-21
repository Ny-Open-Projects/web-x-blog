---
title: [ZSM-127] 客户端状态里的「归一化缓存」和 TanStack Query 的「KV 缓存」差在哪？什么业务需要归一化？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-127：客户端状态里的「归一化缓存」和 TanStack Query 的「KV 缓存」差在哪？什么业务需要归一化？
**答**：
- KV 缓存（Query/SWR）：按请求 key 存「响应快照」，不解析关系；优点是简单、UI 与响应形态一致，缺点是同一实体在多个响应里各有一份，改一处要失效所有相关 key。
- 归一化缓存（Apollo/Relay/Redux-normalizr 思路）：把响应拆成实体表 `{ Article: { a1: {...} } }`，响应里只存引用 ID；优点是改一处全站自动同步，缺点是要维护 schema、read/write 函数与垃圾回收，心智负担大。
- 选型经验：电商后台、CMS 这类「同一商品出现在列表/详情/购物车多个视图且要强一致」的场景值得归一化；内容型中后台 KV 缓存 + 失效清单就够了。
- 面试要点：说出「一致性维护成本从失效策略转移到 schema 设计」，并给出自己项目的选择与理由。

```javascript
// KV 缓存：同一商品在列表缓存和详情缓存里是两份快照
qc.setQueryData(['goods', 1], { id: 1, price: 99 })
qc.setQueryData(['goods-list'], [{ id: 1, price: 95 }])  // 旧价仍在列表里！

// 归一化：实体表 + 引用
const normalized = {
  entities: { goods: { 1: { id: 1, price: 99 } } },
  lists: { hot: { ids: [1, 2] } },       // 列表只存 ID 引用
}
// 任意视图读同一实体：
function selectGoods(id) { return normalized.entities.goods[id] }

// 归一化的写路径：改实体表，引用它的所有视图自动一致
function patchGoods(id, patch) {
  normalized.entities.goods[id] = { ...normalized.entities.goods[id], ...patch }
}
```
