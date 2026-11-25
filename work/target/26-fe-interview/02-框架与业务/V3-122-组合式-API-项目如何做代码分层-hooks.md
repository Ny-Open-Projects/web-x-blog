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

**追问**：

1. 两个 composable 互相调用会不会形成循环依赖？→ 会，尤其在彼此 import 对方时；解法是依赖注入：把 service 或 store 当参数传进去，不 import 对方，或者把共用逻辑再下沉一层。
2. store 里能不能写 computed 和异步 action？→ computed 可以，只做派生且不发请求；异步 action 保留但内部只调 service，裸 fetch 和组装查询参数必须留在 service，否则 store 变成第二个组件。
3. 怎么防止 composable 变成"万能层"？→ 划三条线：出现业务规则或格式化就下沉纯函数 utils，出现 IO 就回 services，composable 只留组合、生命周期与 loading/error 编排。
