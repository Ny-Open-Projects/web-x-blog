---
title: [V3-090] 服务端数据放 Pinia 还是 TanStack Query？如何决策？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-090：服务端数据放 Pinia 还是 TanStack Query？如何决策？
**答**：
- 核心判据：数据归谁所有。服务端数据（列表、详情）归 Query 管——缓存、去重、重试、失效更新都是现成的；客户端状态（购物车、UI 开关、表单草稿）归 Pinia 管。
- 反模式：把接口数据复制进 Pinia，等于手写一遍缓存层，还要自己处理失效与竞态。
- 两者协作：Query 拉数据 → 关键结果写入 Pinia 供全局消费；或 Pinia 存查询参数，Query 用参数作 queryKey。
- 引入 Query 前先评估规模：少量接口时 useRequest 已够，多页面共享大量服务端数据时 Query 收益明显。

```typescript
// composables/useProducts.ts —— 决策落地：服务端数据归 Query，客户端状态归 Pinia
import { useQuery } from "@tanstack/vue-query";
import type { Ref } from "vue";
import { useCartStore } from "@/stores/modules/cart";

// 服务端数据：缓存、重试、失效都由 Query 管理，不复制进 Pinia
export function useProductList(keyword: Ref<string>) {
  return useQuery({
    queryKey: ["products", keyword], // keyword 变化自动重新请求并各自缓存
    queryFn: () => fetchProducts(keyword.value),
    staleTime: 60_000, // 60 秒内视为新鲜，不重复请求
  });
}

// 客户端状态：购物车是纯前端状态，留在 Pinia
export function useAddToCart() {
  const cart = useCartStore();
  return (productId: string) => cart.add(productId);
}

// 服务端状态要参与全局派生时（如角标数量），才把结果同步进 Pinia：
// watch(products.data, (d) => badgeStore.setCount(d?.length ?? 0));
```
