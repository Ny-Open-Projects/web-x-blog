---
title: [DP-130] Pinia store 里如何实践状态模式？getter 与 action 各扮演什么角色？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-130：Pinia store 里如何实践状态模式？getter 与 action 各扮演什么角色？（高频）
**答**：
- Pinia store = 模块级单例 + 观察者（响应式依赖收集）+ 状态收敛；把状态机的"转移规则"写在 action 里，getter 承担派生数据（selector，DP-078）。
- 状态模式落点：复杂流程（订单）在 store 内维护 `status`，action 先校验当前状态合法性再转移，等价于 DP-102 的状态机表放进 store。
- 规范：action 内不写 UI 副作用；跨 store 调用通过组合（store 内 use 另一个 store）而非事件广播。

```vue
<script setup>
// stores/order.js —— 状态机收敛在 store
import { defineStore } from 'pinia';
const transitions = {                                                   // 转移表（DP-102 思想）
  pending: { pay: 'paid', cancel: 'closed' },
  paid: { ship: 'shipped', refund: 'refunding' },
  shipped: { confirm: 'done' },
};
export const useOrderStore = defineStore('order', {
  state: () => ({ id: '', status: 'pending', history: [] }),
  getters: {
    canCancel: (s) => !!transitions[s.status]?.cancel,                  // 派生：按钮可用性由状态推导
    timeline: (s) => s.history,
  },
  actions: {
    dispatch(event, payload = {}) {                                     // action = 唯一转移入口
      const next = transitions[this.status]?.[event];
      if (!next) throw new Error(`非法转移 ${this.status} + ${event}`);  // 状态模式：非法转移被拦截
      this.history.push({ from: this.status, event, at: Date.now() });
      this.status = next;
      if (event === 'pay') return api.post(`/orders/${this.id}/pay`, payload);  // 副作用仍在 action 层
    },
  },
});
// 组件：UI 只问 getter、只调 action
const store = useOrderStore();
const canPay = computed(() => !!transitions[store.status]?.pay);
</script>
<template><button :disabled="!canPay" @click="store.dispatch('pay')">支付</button></template>
```
