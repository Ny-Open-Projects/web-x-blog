---
title: [ZSM-513] Zustand 的 getInitialState 与 SSR 场景下的双快照设计
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-513：Zustand 的 getInitialState 与 SSR 场景下的双快照设计

**答**：
- store API 有三个读方法：`getState`（当前值）、`getInitialState`（创建时的初始值，v4.3+ 提供）、服务端场景还有 `getServerSnapshot`。三者区分是为了「快照稳定性」——React 要求 getSnapshot 在同一状态时返回同一引用。
- SSR 一次性渲染：服务端不用订阅，`useStore` 的服务端路径直接走 `getInitialState`，保证「服务端产出 HTML 时用的状态」与「客户端注水时第一次 get」一致，避免注水 mismatch。
- 每请求隔离：服务端模块级单例会串用户，方案是 `createStore()` 工厂在每请求里新建 store，通过 Context 传给子树；客户端才用模块级单例。
- `getInitialState` 的另一个用途：重置 store（回到初始快照）不需要手动列字段，`set(getInitialState())` 即可；也可用于服务端把非序列化字段剔除后再注入。
- 追问钩子：`getServerSnapshot` 若返回新对象引用，React 18 的 useSyncExternalStore 会在注水时直接 throw（服务端快照必须稳定）。

```javascript
// SSR 每请求 store 模式（Next.js App Router）
// storeFactory.ts
import { createStore } from 'zustand'
export const createCounterStore = () =>
  createStore((set) => ({ count: 0, inc: () => set((s) => ({ count: s.count + 1 })) }))

// StoreProvider.tsx —— 客户端组件，服务端每请求建一个 store 实例
'use client'
const StoreContext = createContext(null)
export function StoreProvider({ children }) {
  const storeRef = useRef(null)
  if (storeRef.current == null) storeRef.current = createCounterStore()
  return <StoreContext.Provider value={storeRef.current}>{children}</StoreContext.Provider>
}

// 消费端：始终从 context 取，避免服务端单例串请求
export const useCounter = () => {
  const store = useContext(StoreContext)
  if (!store) throw new Error('missing provider')
  return useStore(store, (s) => s.count)
}

// 重置用法
// useCounterStore.setState(useCounterStore.getInitialState())
```
