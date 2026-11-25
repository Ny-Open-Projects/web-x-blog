---
title: [ARC-053] 全局状态（Pinia/Zustand/Redux）在大型应用如何模块化切分？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-053：全局状态（Pinia/Zustand/Redux）在大型应用如何模块化切分？
**答**：
- 按业务域切片（slice）而非技术分层（actions/reducers 分文件），每个域一个 store 文件，自包含 state/actions/selectors。
- store 之间不直接 import 互相的 state，通过事件或显式订阅通信，防止状态网状耦合。
- Redux 适合需要中间件生态/时间旅行/严格规范的团队；Zustand/Pinia 适合轻量直接的场景，二者都强调 slice 化。

```typescript
// Zustand 按域切片
export const useCartStore = create<CartState>()((set, get) => ({
  items: [],
  add: (item) => set(s => ({ items: [...s.items, item] })),
  total: () => get().items.reduce((sum, i) => sum + i.price * i.qty, 0),
}));

export const useSessionStore = create<SessionState>()(set => ({
  user: null,
  login: async (token) => set({ user: await fetchMe(token) }),
}));

// 跨 store 不互相 import state，用事件解耦
cartBus.on('checkout:done', () => useCartStore.setState({ items: [] }));
```
