---
title: [V3-493] Pinia 在大型应用的状态分层
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 状态管理]
type: 面试题
---

## V3-493：Pinia 在大型应用的状态分层

**答**：
- 三层状态划分：服务器缓存（列表/详情——带 TTL 与失效）、客户端状态（UI 态/草稿/选择）、会话态（token/用户）——不同层不同失效策略，混在一起是退化之源
- store 粒度：按业务域拆 store（order/user/cart）而不是全局巨型 store——跨 store 依赖用「store 内引用另一个 store」显式声明
- 服务器缓存层实践：Pinia + TanStack Query 的分工（Query 管缓存与重试，Pinia 管派生视图态）——「状态管理库不等于服务端缓存库」的边界意识
- 持久化分层：只有会话态与少量 UI 态持久化（pinia-plugin-persistedstate 按路径持久化）；服务器缓存绝不持久化（过期问题）
- 性能关联：大 store 的 getter 是 computed——细粒度 getter/选择性订阅（storeToRefs 按字段）避免「改一个字段全 store 订阅者重算」

```javascript
// 分层示例
export const useSessionStore = defineStore('session', { persist: true, ... });    // 会话层
export const useOrderStore = defineStore('order', () => {                          // 业务域
  const orders = ref([]);                       // 服务器缓存(由 query 层填充)
  const selectedIds = ref(new Set());           // 客户端选择态
  const total = computed(() => sum(orders.value.filter(o => selectedIds.value.has(o.id))));
});
```
