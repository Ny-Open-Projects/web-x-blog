---
title: [V3-085] 大型项目里 Pinia 如何模块化组织（分层 store 设计）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-085：大型项目里 Pinia 如何模块化组织（分层 store 设计）？
**答**：
- 按业务域拆分 store，而不是一个巨型 index：跨页面共享的放 modules，页面级临时状态放 views。
- 目录约定：`stores/modules`（user/order 等长期驻留）、`stores/views`（checkout 等可随路由销毁）、`stores/plugins`（persist/logger）。
- 判据：状态被两个以上页面共享才进 modules，否则放组件或页面级 store。
- 全部用 setup store 写法，与组合式 API 心智一致，TS 推导也最好。

```typescript
// stores/index.ts —— 分层组织的入口
import { createPinia } from "pinia";
import { persistPlugin } from "./plugins/persist";

export const pinia = createPinia();
pinia.use(persistPlugin);

// 推荐目录结构：
// stores/
//   modules/   —— 业务域 store：user.ts order.ts product.ts（跨页面共享，长期驻留）
//   views/     —— 页面级临时 store：checkout.ts（只服务单个页面，可随路由销毁）
//   plugins/   —— persist.ts logger.ts
// 原则：被两个以上页面共享的状态才进 modules，否则放组件内部或 views 层

// stores/modules/user.ts
import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const token = ref("");
  const profile = ref<{ name: string; role: string } | null>(null);
  const isVip = computed(() => profile.value?.role === "vip");
  return { token, profile, isVip };
});

// stores/views/checkout.ts —— 页面级 store 示例
export const useCheckoutStore = defineStore("checkout", () => {
  const submitting = ref(false);
  return { submitting };
});
```
