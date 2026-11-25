---
title: [V3-259] SSR 下 Pinia 状态同步怎么做？如何避免"双份缓存"？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-259：SSR 下 Pinia 状态同步怎么做？如何避免"双份缓存"？
**答**：
- 机制：SSR 时服务端为每请求创建独立 pinia 实例，渲染后把 state 序列化进 payload；客户端创建 pinia 并从 payload 恢复，两端 store 内容一致。
- 反模式"双份缓存"：把"服务端取回的数据"再塞进客户端自建缓存（如又存一份到本地 map），两份数据会漂移；正确做法是服务端数据以 pinia/useAsyncData 为唯一源。
- 请求级隔离：pinia 实例挂在每请求的上下文（Nuxt 的 useNuxtApp），禁止模块级单例 store 跨请求共享（会串用户数据，高危）。
- 状态瘦身：只序列化"客户端初次渲染需要"的字段，大数组（如千条列表）只传首屏部分，其余客户端分页拉取。
- 面试钩子：能说出"per-request store 实例 + payload 恢复 + 唯一数据源"三点即达标。

```typescript
// 服务端入口（Nuxt 已封装）：每请求
// const pinia = createPinia(); app.use(pinia); ...渲染后 payload = stringify(pinia.state.value)
// 客户端：const pinia = createPinia(); hydrate(pinia, window.__PINIA_STATE__)
// stores/cart.ts —— 每请求独立实例，无泄漏
export const useCartStore = defineStore('cart', () => {
  const items = ref([]);
  async function load() { items.value = await $fetch('/api/cart'); }
  return { items, load };
});
// ❌ 反模式：模块级缓存 const cache = {}; export function getData(k){ return cache[k] ??= fetch(k) }
// SSR 下 cache 跨请求共享 → 用户 A 的数据泄露给用户 B
```
