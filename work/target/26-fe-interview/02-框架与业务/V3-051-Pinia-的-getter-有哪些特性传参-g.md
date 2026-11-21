---
title: [V3-051] Pinia 的 getter 有哪些特性？传参 getter 为什么无法缓存？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-051：Pinia 的 getter 有哪些特性？传参 getter 为什么无法缓存？
**答**：
- getter 基于 state 计算并有缓存，依赖不变不重算，等价于 computed。
- getter 可以访问其他 getter（this）甚至其他 store 的状态。
- 传参 getter 实际是"返回函数的 getter"，每次调用都重新执行函数，无法缓存结果。
- 需要按参数缓存时，应该把参数作为 state，或直接写 action。

```typescript
import { defineStore } from "pinia";

export const useProductStore = defineStore("product", {
  state: () => ({
    products: [
      { id: 1, price: 100 },
      { id: 2, price: 250 },
    ],
  }),
  getters: {
    // 普通 getter：基于 state 派生，有缓存
    total: (state) => state.products.reduce((sum, p) => sum + p.price, 0),
    // 传参 getter：返回函数，每次调用重新计算，无法缓存
    getByPrice: (state) => (min: number) =>
      state.products.filter((p) => p.price >= min),
  },
});
```
