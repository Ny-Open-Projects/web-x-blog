---
title: [V3-122] 组合式 API 项目如何做代码分层（hooks、services、stores 的边界）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-122：组合式 API 项目如何做代码分层（hooks、services、stores 的边界）？
**答**：
- services：纯 IO 与类型，函数进函数出，不 import vue，可单测。
- hooks（composables）：编排层，调用 services、管理响应式状态与副作用，可依赖 stores。
- stores：只放跨组件共享的状态与动作，状态来源仍走 services，禁止在 store 里直接写 fetch 细节。
- 判据：组件里的逻辑超过一屏就下沉成 composable；同一份数据被两个组件用就进 store。

```typescript
// 一条完整链路的三层边界示例

// 1. services/orders.ts —— 纯 IO 层：不依赖 Vue，可独立单测
import { http } from "@/shared/http";
import type { Order } from "./types";

export function fetchOrders(params: { page: number; keyword?: string }) {
  return http.get<Order[]>("/orders", { params });
}

// 2. features/order/composables/useOrderList.ts —— 编排层：连接 services 与组件
import { useRequest } from "@/shared/useRequest";
import { useOrderFilters } from "./useOrderFilters";

export function useOrderList() {
  const filters = useOrderFilters(); // 页码、关键词等筛选状态
  const { data, loading, run } = useRequest(() =>
    fetchOrders({ page: filters.page.value, keyword: filters.keyword.value })
  );
  return { orders: data, loading, filters, refresh: run };
}

// 3. stores/modules/cart.ts —— 共享状态层：只管共享，不直接写 fetch 细节
//    例外允许调用 services 函数，但不允许出现裸 fetch/axios 调用
//
// 边界口诀：services 管 IO，hooks 编排流程与生命周期，stores 管跨组件共享
```
