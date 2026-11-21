---
title: [V3-086] Pinia store 互相引用出现循环依赖怎么办？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-086：Pinia store 互相引用出现循环依赖怎么办？
**答**：
- 错误写法：store A 在 setup 顶层调用 `useBStore()`，B 又在顶层调用 `useAStore()`，模块加载期互相等待拿到 undefined。
- 正确写法：把 `useBStore()` 的调用推迟到 getter/action 的函数体内部，运行时才解析依赖，模块级循环自然解开。
- setup store 顶层也可以留，但只允许“单向”引用；出现环就必须下放到回调内。
- 更彻底的解法：把公共状态抽到第三个 store，消掉这条环。

```typescript
// stores/modules/cart.ts —— 通过延迟调用 useUserStore() 解开循环依赖
import { defineStore } from "pinia";
import { computed } from "vue";
import { useUserStore } from "./user"; // user.ts 里也 import 了 cart.ts，模块级成环

export const useCartStore = defineStore("cart", () => {
  // 正确：在 getter 回调内部才调用 useUserStore()，运行时解析，循环依赖自动解开
  const discount = computed(() => {
    const user = useUserStore();
    return user.isVip ? 0.9 : 1;
  });

  async function checkout() {
    const user = useUserStore(); // action 内同理
    if (!user.token) throw new Error("请先登录");
    // ...提交结算
  }

  return { discount, checkout };
});

// 错误示例（不要这样写）：
// const user = useUserStore(); // setup 顶层调用且与 user.ts 互相 import
//                              // 模块加载期一边还没初始化，拿到 undefined

// 更彻底的解法：把环上公共的部分（如会员等级）抽成独立 membership store
```
