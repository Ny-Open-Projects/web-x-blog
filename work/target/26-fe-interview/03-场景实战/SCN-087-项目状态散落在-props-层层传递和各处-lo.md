---
title: [SCN-087] 项目状态散落在 props 层层传递和各处 localStorage 里，如何做选型收敛？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-087：项目状态散落在 props 层层传递和各处 localStorage 里，如何做选型收敛？
**答**：
- 先分类再选型：服务端状态（列表/详情）交给 TanStack Query/SWR，缓存、失效、重试全部内置；纯 UI 状态（抽屉开关、主题）用轻量 store（zustand/pinia）；真正全局的业务状态（登录用户、租户）才进全局 store。
- 原则：能局部的不提升；服务端状态不做二次手写缓存（把接口数据抄进 redux 是反模式）。
- 写操作后用缓存失效（invalidate）而非手动同步数据，保持"服务端是唯一真源"。

```typescript
// 状态选型落地：服务端状态用 TanStack Query，UI 状态用 zustand，两者不混
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { create } from 'zustand';

// 服务端状态：缓存 key 精确到参数，自动失效与重试
function useOrders(params: OrdersQuery) {
  return useQuery({
    queryKey: ['orders', params],          // 参数变化自动重新请求
    queryFn: () => api.getOrders(params),
    staleTime: 30_000,                     // 30 秒内视为新鲜，不重复请求
    placeholderData: (prev) => prev,       // 翻页保留旧数据避免闪空
  });
}

// 纯 UI 状态：轻量 store，不必进全局大 store
const useUIStore = create<{ sidebarOpen: boolean; toggle: () => void }>((set) => ({
  sidebarOpen: false,
  toggle: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
}));

// 写操作后精准失效相关查询：服务端是唯一真源，不做手动数据同步
const qc = useQueryClient();
function onOrderCreated(order: Order) {
  qc.invalidateQueries({ queryKey: ['orders'] });
}
```
