---
title: [ZSM-155] Zustand 的 redux / combine 中间件有什么用？什么场景值得把 Zustand 写成 Redux 风格？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-155：Zustand 的 redux / combine 中间件有什么用？什么场景值得把 Zustand 写成 Redux 风格？
**答**：
- redux 中间件给 Zustand 加上 `{ type, payload }` 的 dispatch 语义：action 是纯函数 `(state, action) => state`，适合从 Redux 平迁、或需要「操作日志/时间旅行」的场景。
- combine 中间件做的是反向事——把多个切片函数 merge 成一个 store（032 已考切片依赖，这里考 combine 的形态），让大 store 按域拆文件维护。
- 值得 Redux 风格的信号：审计需求（每条状态变更可回放）、团队已有 Redux devtools 工作流、 reducer 逻辑想单测覆盖。
- 不值得的信号：业务就是普通 CRUD——dispatch 样板让代码量翻倍，Zustand 的直接 set 更贴合。能给出「按需选风格」的判断比站队重要。

```javascript
import { redux, combine } from 'zustand/middleware'

// Redux 风格：操作可回放、可审计
const useAuditStore = create(redux(
  (state, action) => {
    switch (action.type) {
      case 'GOODS_ADD':   return { items: [...state.items, action.payload] }
      case 'GOODS_REMOVE':return { items: state.items.filter(i => i.id !== action.id) }
      default:            return state
    }
  },
  { items: [] }                              // 初始态
))

useAuditStore.dispatch({ type: 'GOODS_ADD', payload: { id: 1, name: '键盘' } })

// combine 风格：切片分文件，merge 成一个 store
const useAppStore = create(combine(
  createCartSlice,        // (set, get) => ({ cart: [], add: ... })
  createPrefsSlice,       // (set, get) => ({ theme: 'dark', setTheme: ... })
))
```
