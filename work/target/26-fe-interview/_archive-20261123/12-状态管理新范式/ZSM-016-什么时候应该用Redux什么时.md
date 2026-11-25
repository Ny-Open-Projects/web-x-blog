---
title: [ZSM-016] 什么场景仍然应该选 Redux/RTK 而不是 Zustand？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-016：什么场景仍然应该选 Redux/RTK 而不是 Zustand？
**答**：
- 强审计需求：金融、后台审批流要每一步变更可追溯，Redux 的 action 日志 + devtools 时间旅行是硬需求。
- 中间件管线成熟：RTK 的 listenerMiddleware / thunk 生态处理长流程副作用更规范；Zustand 的副作用常散落在组件或 subscribe 里。
- 大团队协作：单一 store + reducer 约定让「谁改了什么」有唯一事实源，利于 code review 和回归排查。
- 跨框架或多入口共享复杂 reducer 逻辑、需要 RTK Query 与服务端状态一体化的场景。
- 反之，中小应用、组件外直读直写、追求包体积（Zustand ~1KB）时 Zustand 优先。

```javascript
// RTK listenerMiddleware：集中管理副作用（对标 Zustand 的 subscribe）
const listener = createListenerMiddleware()
listener.startListening({
  actionCreator: orderCreated,
  effect: async (action, api) => {
    api.dispatch(logEvent('order-created', action.payload)) // 审计日志
    await api.dispatch(syncToServer(action.payload))
  },
})
```
