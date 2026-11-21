---
title: [ZSM-012] Zustand 底层为什么用 useSyncExternalStore？tearing 问题是什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-012：Zustand 底层为什么用 useSyncExternalStore？tearing 问题是什么？
**答**：
- useSyncExternalStore 是 React 18 官方为「外部 store + 并发渲染」提供的订阅 API，保证读到的快照与渲染一致，并在客户端 hydration 时强制对齐服务端快照。
- tearing（撕裂）：并发模式下渲染可中断，如果同一帧内不同组件读到不同版本的 store 快照，页面会出现「一半旧一半新」。useSyncExternalStore 通过「渲染期间读快照若已变更则强制同步重渲染」来消除它。
- 旧方案 useSubscription/手写 useState+useEffect 都难以同时满足并发安全与减少重渲染。
- 追问钩子：SSR 时 getServerSnapshot 必须是纯函数返回稳定引用，否则 hydration 报错。

```javascript
import { useSyncExternalStore } from 'react'
// Zustand 内核简化版
function useStore(store, selector = s => s) {
  return useSyncExternalStore(
    store.subscribe,        // 订阅
    () => selector(store.getState()), // 客户端快照
    () => selector(store.serverState ?? store.getState()) // 服务端快照
  )
}
```
