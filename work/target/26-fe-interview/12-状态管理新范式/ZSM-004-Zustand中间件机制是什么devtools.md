---
title: [ZSM-004] Zustand 中间件机制是什么？devtools 和 persist 分别怎么工作？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-004：Zustand 中间件机制是什么？devtools 和 persist 分别怎么工作？
**答**：
- 中间件本质是**高阶函数包装 creator**：`(config) => (set, get, api) => config(增强后的set, get, api)`，可以劫持 set/get、注入额外能力。
- devtools 中间件：劫持 set，每次状态更新向 Redux DevTools 派发 action（自动生成或自定义 action 名），获得时间旅行、日志、回放能力。
- persist 中间件：拦截 set 和初始 state，把（部分）state 写入 localStorage/AsyncStorage，并在 store 创建时读回合并，支持 `partialize` 挑字段、`version/migrate` 做数据迁移。
- 中间件可组合，书写顺序影响行为：惯例 `devtools(persist(...(...)))`，persist 在内层避免把动作日志也存进存储。
- 追问钩子：所有中间件共享同一个 `(set, get, api)` 契约，所以可以手写自定义中间件（如日志、同步多标签页）。

```javascript
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

const useAuth = create(devtools(persist(
  (set) => ({
    token: '', userId: 0,
    login: (token, userId) => set({ token, userId }, false, 'auth/login'), // 命名 action
  }),
  {
    name: 'auth',                       // storage key
    partialize: s => ({ token: s.token }), // 只持久化 token，不含函数
    version: 1,
    migrate: (old, ver) => ver === 1 ? old : old, // 版本迁移
  }
)))
```
