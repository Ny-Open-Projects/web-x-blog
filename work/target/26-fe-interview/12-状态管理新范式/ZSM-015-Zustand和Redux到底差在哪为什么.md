---
title: [ZSM-015] Zustand 和 Redux 的核心区别是什么？为什么新项目不再默认上 Redux？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-015：Zustand 和 Redux 的核心区别是什么？为什么新项目不再默认上 Redux？
**答**：
- 样板量：Redux 强制 action/reducer/dispatch 单向数据流 + immutability，一个字段更新要写三处；Zustand 直接 set，函数即 action。
- 更新粒度：Redux 的 reducer 是整树纯函数替换；Zustand 是浅合并 + selector 细粒度订阅，不用 reselect 也能避免多余渲染。
- Provider：Redux 必须包 Provider 传 dispatch；Zustand 无 Provider，组件外直接 getState/setState。
- RTK 修复了 Redux 的样板痛点（createSlice/Immer），但仍保留了「单一 store、可预测日志、时间旅行」的约束，适合需要强审计的中后台；轻交互页面用 Zustand 更快。
- 追问钩子：两者都基于不可变更新 + 订阅，真正差异是约束强度，不是性能。

```javascript
// Redux（RTK）一个字段更新
const slice = createSlice({
  name: 'cart', initialState: { count: 0 },
  reducers: { add: state => { state.count += 1 } },  // Immer 让你直接改
})
store.dispatch(cart.actions.add())

// Zustand 同一件事
const useCart = create(set => ({
  count: 0,
  add: () => set(s => ({ count: s.count + 1 })), // 定义即调用：useCart.getState().add()
}))
```
