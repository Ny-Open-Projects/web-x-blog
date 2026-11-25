---
title: [ZSM-522] Zustand 的 redux 中间件和 combine 中间件各自解决什么
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-522：Zustand 的 redux 中间件和 combine 中间件各自解决什么

**答**：
- `redux` 中间件：给 Zustand 塞进 Redux 的心智模型——store 里只有 `{ dispatch, type }` 流转，状态更新全部经 `dispatch(action)` 走 reducer，适合「从 Redux 迁移、复用旧 reducer/中间件生态」的过渡场景。
- `combine` 中间件：把「初始状态对象」和「actions 函数」合并成一个 store 定义，等价于语法糖 `create((set) => ({ ...initialState, ...actions }))`，让「状态字段声明」和「行为」在视觉上分层。
- 本质差异：redux 是**约束写路径**（所有变更必须走 reducer，可预测、可回放），combine 是**组织代码结构**（不改变任何运行时行为）。
- 可以共存：`combine(redux(...))` 之类组合没有冲突，但一般不叠加——redux 模式下 store 结构已经被 dispatch 协议占据，combine 会破坏 action 类型推断。
- 追问钩子：redux 中间件让 DevTools 无需 devtools 中间件也能工作（dispatch 协议原生兼容），这是老 Redux 项目迁移的隐形福利。

```javascript
import { create } from 'zustand'
import { redux, combine } from 'zustand/middleware'

// redux 中间件：dispatch 协议
const useReduxStore = create(redux(
  (state, action) => {
    switch (action.type) {
      case 'ADD': return { ...state, count: state.count + action.payload }
      case 'RESET': return { ...state, count: 0 }
      default: return state
    }
  },
  { count: 0 }   // 初始状态
))
useReduxStore.getState().dispatch({ type: 'ADD', payload: 2 })
// dispatch 前置：type 必填，未匹配走 reducer default 返回原状态

// combine 中间件：状态与 actions 分层声明
const useCounter = create(combine(
  { count: 0, step: 1 },                                        // 纯状态
  (set) => ({
    inc: () => set((s) => ({ count: s.count + s.step })),
    setStep: (step) => set({ step }),
  })
))
// 类型上 counter 自动获得 { count, step, inc, setStep } 全量推断
```
