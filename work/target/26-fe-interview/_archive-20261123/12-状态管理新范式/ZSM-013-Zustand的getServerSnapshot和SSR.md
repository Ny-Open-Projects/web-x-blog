---
title: [ZSM-013] Zustand 在 SSR（Next.js App Router）下怎么用？模块级单例 store 为什么会串用户？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-013：Zustand 在 SSR（Next.js App Router）下怎么用？模块级单例 store 为什么会串用户？
**答**：
- 服务端是进程常驻的，模块级单例 store 会被所有请求共享，用户 A 的登录态会泄漏给用户 B（串数据），这是 SSR 大忌。
- 解法：用 `createStore`（vanilla）+ 工厂函数每请求新建 store，通过 React Context（Provider）把实例传下去，`useStore(store, selector)` 消费。
- RSC 中只能读快照（getState），不能在服务端组件订阅；客户端组件里再做交互更新。
- 水合一致性：客户端首次渲染必须拿到与服务端相同的快照，否则 useSyncExternalStore 触发 hydration 错误，常见做法是 hydrate 后再写 store 或用 useEffect 延迟写。

```javascript
// store.ts：工厂，不导出单例
import { createStore } from 'zustand'
export const createAppStore = (init) => createStore((set) => ({ ...init, setData: d => set({ data: d }) }))

// provider.tsx：每请求一个 store，Context 下发
const StoreCtx = createContext(null)
export const StoreProvider = ({ init, children }) => {
  const ref = useRef(null)
  if (!ref.current) ref.current = createAppStore(init)
  return <StoreCtx.Provider value={ref.current}>{children}</StoreCtx.Provider>
}
// 使用
const useApp = selector => useStore(useContext(StoreCtx), selector)
```
