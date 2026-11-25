---
title: [ZSM-501] Zustand 的 useStore 内部为什么每次渲染都要重新校验快照
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-501：Zustand 的 useStore 内部为什么每次渲染都要重新校验快照

**答**：
- 源码 `useStore` 里渲染后有一段 `checkForUpdates` 逻辑：React 提交后用最新的 selector 结果和上次值比对，不一致就强制再次渲染。这是为了对抗「撕裂（tearing）」。
- 撕裂场景：并发渲染下，React 可能在一个高优先级渲染中途暂停，此时外部 store 更新了，恢复渲染时旧快照和新快照混在同一棵树里，UI 一半新一半旧。
- 具体实现：`useSyncExternalStoreWithSelector` 在每次 commit 时记录 selector 产物，若期间 store 变化导致结果变了就 `forceStoreRerender`，保证最终一致。
- 追问钩子：React 18 的 `useSyncExternalStore` 已内置订阅阶段的防撕裂，Zustand 这层额外校验主要防的是 selector 记忆化失效导致的漏更。

```javascript
// 简化版 useStore 源码骨架（v4/v5 的 react.ts）
function useStore(api, selector = identity) {
  const slice = useSyncExternalStoreWithSelector(
    api.subscribe,          // 订阅源
    api.getState,           // getSnapshot：React 渲染时取当前值
    api.getInitialState,    // getServerSnapshot：SSR 用初始值防撕裂
    selector,               // 用户 selector
    identity                // 默认浅等可被 useShallow 替换
  )
  useDebugValue(slice)
  return slice
}

// 为什么还要 commit 后校验：并发模式下「暂停-恢复」期间
// store 可能变过，selector 记忆化命中旧缓存就漏更新，
// useSyncExternalStoreWithSelector 内部用 inst.hasValue + inst.value
// 对比新旧 slice，不等则 forceStoreRerender 重新拉一次快照。
```
