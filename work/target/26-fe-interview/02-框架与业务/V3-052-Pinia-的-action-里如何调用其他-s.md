---
title: [V3-052] Pinia 的 action 里如何调用其他 store 与处理异步？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-052：Pinia 的 action 里如何调用其他 store 与处理异步？
**答**：
- action 内直接 `useOtherStore()` 获取其他 store 实例，模块间自由组合。
- 异步直接用 async/await，没有 mutation 概念，await 后直接改 this。
- this 指向 store 实例；setup store 中则直接操作本地 ref。
- 错误处理、并发控制（如防重复提交）都可以内聚在 action 里。

```typescript
import { defineStore } from "pinia";
import { useUserStore } from "./user";

export const useOrderStore = defineStore("order", {
  state: () => ({ orders: [] as string[], submitting: false }),
  actions: {
    async submit(order: string) {
      if (this.submitting) return; // 防重复提交
      this.submitting = true;
      try {
        const userStore = useUserStore(); // 调用其他 store
        const res = await fetch("/api/orders", {
          method: "POST",
          headers: { token: userStore.token },
          body: JSON.stringify({ order }),
        });
        const data = await res.json();
        this.orders.push(data.id); // await 后直接修改 state
      } finally {
        this.submitting = false;
      }
    },
  },
});
```
