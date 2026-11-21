---
title: [R19-159] 如何用 useSyncExternalStore 接入一个 external store？注意事项有哪些？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-159：如何用 useSyncExternalStore 接入一个 external store？注意事项有哪些？
**答**：
- 签名：`useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)`，React 18 为非 React 状态源（localStorage、WebSocket、第三方 store）提供的官方桥。
- 三条契约：getSnapshot 必须**缓存稳定**（内容不变返回同一引用，否则无限循环）；subscribe 返回取消函数；数据变化后必须先更新 store 再通知订阅（快照一致性）。
- getServerSnapshot 用于 SSR：服务端返回初始快照，避免 hydration mismatch。
- 与 useEffect+setState 手动桥相比：官方 API 天然处理 tearing（并发下所有组件读到同一快照），不要自己造轮子。

```tsx
// use-broadcast-store.ts —— useSyncExternalStore 完整接入示例
import { useSyncExternalStore, useCallback } from 'react';

// external store：与 React 完全无关的模块级状态
type CartState = { items: { id: string; qty: number }[] };
let cart: CartState = { items: [] };
const cartListeners = new Set<() => void>();

function emitCart() {                       // 约定：先改数据，再通知
  cartListeners.forEach(l => l());
}

export const cartStore = {
  add(id: string) {
    cart = {
      items: [...cart.items, { id, qty: 1 }], // 不可变更新，生成新引用
    };
    emitCart();
  },
  subscribe(listener: () => void) {
    cartListeners.add(listener);
    // 同步其他标签页：跨 tab 共享这份 external store
    window.addEventListener('storage', listener);
    return () => {
      cartListeners.delete(listener);
      window.removeEventListener('storage', listener);
    };
  },
  getSnapshot(): CartState {
    return cart;                              // 内容不变 -> 同一引用，契约满足
  },
  getServerSnapshot(): CartState {            // SSR 稳定初始值
    return { items: [] };
  },
};

// React 绑定：唯一合法的桥
export function useCart() {
  const cart = useSyncExternalStore(
    cartStore.subscribe,
    cartStore.getSnapshot,
    cartStore.getServerSnapshot,
  );
  const add = useCallback((id: string) => cartStore.add(id), []);
  return { cart, add };
}

// CartBadge.tsx
export function CartBadge() {
  const { cart } = useCart();
  return <span>购物车 {cart.items.length} 件</span>;
}

// 常见踩坑：
// 1) getSnapshot 里每次 return {...cart} 新对象 -> 触发 "getSnapshot should be cached" 无限重渲染
// 2) 订阅回调里先通知再改数据 -> React 读到的还是旧快照，出现 tearing
// 3) 忘记 getServerSnapshot -> SSR 与客户端首屏渲染结果不一致
```
