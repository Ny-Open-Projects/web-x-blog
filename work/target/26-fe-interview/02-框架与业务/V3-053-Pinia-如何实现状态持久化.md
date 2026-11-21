---
title: [V3-053] Pinia 如何实现状态持久化？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-053：Pinia 如何实现状态持久化？
**答**：
- 官方方案 pinia-plugin-persistedstate：注册插件后，store 里配置 persist 选项。
- 默认以 store id 为 key 存 localStorage，支持 pick/omit 选择字段、更换 storage。
- 原理就是 `\$subscribe` 状态变化时序列化写入，初始化时读回并 `\$patch`。
- 敏感信息（token）要注意 XSS 风险，可改用 sessionStorage 或 HttpOnly cookie。

```typescript
// main.ts —— 注册持久化插件
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

// stores/user.ts —— 配置 persist 选项
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({ token: "", theme: "light" }),
  // 默认以 store id 为 key 持久化到 localStorage，刷新后自动恢复
  persist: {
    key: "user-store",
    pick: ["token"], // 只持久化 token，theme 不存
    storage: localStorage,
  },
});

// 手写简化版持久化插件（理解原理）：
// function persistPlugin(context: { store: any }) {
//   const key = `pinia-${context.store.$id}`;
//   const raw = localStorage.getItem(key);
//   if (raw) context.store.$patch(JSON.parse(raw));
//   context.store.$subscribe(() => {
//     localStorage.setItem(key, JSON.stringify(context.store.$state));
//   });
// }
```
