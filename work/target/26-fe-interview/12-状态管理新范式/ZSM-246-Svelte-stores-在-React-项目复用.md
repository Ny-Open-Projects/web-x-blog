---
title: [ZSM-246] Svelte writable store 能在 React 项目里复用吗
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-246：Svelte writable store 能在 React 项目里复用吗

**答**：
- 可以：Svelte store 协议就是 subscribe(fn) 返回 unsubscribe + 可选 get——与 useSyncExternalStore 完全对齐，writable 内部有 value 闭包可暴露
- writable 不自带 get，用 `get(store)` 或自封装 readable/writable 包装暴露 getValue；注意 getSnapshot 稳定性（返回内部 value 引用）
- SvelteKit 迁 React 或双栈团队的常见桥：核心域（购物车/会话）用 store 协议写一份，两端各自订阅
- 限制：Svelte 的 derived/get 依赖 Svelte 运行时但协议部分纯 JS，跨框架只用协议层（subscribe），不引组件层

```javascript
import { writable, get } from 'svelte/store'
const cart = writable([])

// React 桥
function useCart() {
  return useSyncExternalStore(
    cart.subscribe,
    () => get(cart),        // 或内部 expose value
  )
}
cart.update((items) => [...items, item])   // 两框架共用写入口
```
