---
title: [ZSM-223] persist 中间件复水 rehydrate 的完整流程（源码级）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-223：persist 中间件复水 rehydrate 的完整流程（源码级）

**答**：
- 创建时立即异步读 storage（默认 localStorage），解析 JSON，用 `merge(persisted, current)` 合并进 store，默认 merge 是浅合并 `{...currentState, ...persistedState}`
- persistedState 由 options.persisted 决定？不对——是 `partialize(state)` 的产物：写入时只存 partialize 结果，读取时也只合并这些字段
- `onRehydrateStorage(store) => (state, error) => {}` 提供复水前后钩子；复水完成前 getState 是初始值，异步数据要留意闪变
- 复水后注册 `api.subscribe`，每次 set 后把 partialize 结果再写回 storage，形成「读一次、写每次」的循环

```javascript
const useStore = create(persist((set) => ({ user: null, token: '', ui: { theme: 'dark' } }), {
  name: 'app-store',
  partialize: (s) => ({ token: s.token, ui: s.ui }),     // 只持久化敏感面之外的可存字段
  onRehydrateStorage: () => (state, err) => err ? console.error(err) : console.log('rehydrated'),
  merge: (persisted, current) => ({ ...current, ...persisted, ui: { ...current.ui, ...persisted.ui } }),
}))
```
