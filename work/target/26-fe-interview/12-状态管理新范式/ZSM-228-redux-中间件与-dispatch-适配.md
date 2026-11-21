---
title: [ZSM-228] redux 中间件把 Zustand 适配成 dispatch 风格的原理
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-228：redux 中间件把 Zustand 适配成 dispatch 风格的原理

**答**：
- redux 中间件给 api 挂 `dispatch`：dispatch(action) 内部把 action 转成 reducer 调用——store 里存的是 `dispatch: (a) => void`，状态更新全走 reducer(state, action)
- 目的：让从 Redux 迁移的团队保留 dispatch 习惯与 action 日志结构，同时享受 Zustand 的轻量；也是把 action 流接入旧 Redux DevTools 的桥
- 现实建议：新项目不推荐 redux 中间件，direct set 更贴近 Zustand 设计意图；仅在存量迁移或需要 action 重放时用
- dispatch 与普通 set 混用时注意：reducer 必须是纯函数，副作用放 action creator 外层

```javascript
const useStore = create(redux((state, action) => {
  switch (action.type) {
    case 'increment': return { count: state.count + 1 }
    default: return state
  }
}, { count: 0 }))

useStore.dispatch({ type: 'increment' })   // 与 Redux 相同的调用面
```
