---
title: [ZSM-008] 不在组件里渲染状态，只想在 store 变化时执行副作用，Zustand 怎么做？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-008：不在组件里渲染状态，只想在 store 变化时执行副作用，Zustand 怎么做？
**答**：
- 组件外用 `useStore.subscribe(listener)`：每次 set 都回调 `(state, prevState)`，自己 diff 出关心的字段再执行副作用（打点、路由跳转、写缓存）。
- 官方 `subscribeWithSelector` 中间件支持 `subscribe(selector, listener)`，只监听 selector 结果变化，省去手写 diff。
- 返回值是取消订阅函数，用于清理；组件内用 useEffect 包裹并 return 取消。
- 注意：listener 里不要直接再 set 造成死循环，需要条件判断收敛。

```javascript
import { subscribeWithSelector } from 'zustand/middleware'
const useStore = create(subscribeWithSelector((set) => ({ userId: 0, setUserId: id => set({ userId: id }) })))

// 只关心 userId 变化（需 subscribeWithSelector）
const unsub = useStore.subscribe(
  s => s.userId,
  (userId, prev) => {
    if (userId !== prev) reporter.setUserId(userId) // 副作用，不触发渲染
  },
  { fireImmediately: true } // 可选：订阅时先触发一次
)
// 组件内清理
useEffect(() => unsub, [])
```
