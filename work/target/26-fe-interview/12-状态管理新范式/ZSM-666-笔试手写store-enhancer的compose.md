---
title: [ZSM-666] 笔试：手写 compose 与 applyMiddleware（enhancer 链核心）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-666：手写 compose 与 applyMiddleware（enhancer 链核心）
**答**：实现三件套：1) `compose(...fns)`：从右到左组合（零参返回 identity，单参透传）；2) `createStore(reducer, enhancer)`：基础 store（getState/dispatch/subscribe/replaceReducer）；3) `applyMiddleware(...middlewares)`：enhancer 形态——包装 createStore，构建 middleware 链替换 dispatch，链中 dispatch 指向链头（thunk 递归 dispatch 回链头）。附用例：验证两层中间件顺序与 thunk 递归。

```javascript
function compose(...fns) {
  if (fns.length === 0) return (x) => x
  if (fns.length === 1) return fns[0]
  return fns.reduce((a, b) => (...args) => a(b(...args)))   // 从右到左
}

function createStore(reducer, enhancer) {
  if (enhancer) return enhancer(createStore)(reducer)   // enhancer 包装 createStore
  let state = reducer(undefined, { type: '@@INIT' })
  const subs = new Set()
  return {
    getState: () => state,
    dispatch: (action) => {
      state = reducer(state, action)
      subs.forEach((fn) => fn())
      return action
    },
    subscribe: (fn) => (subs.add(fn), () => subs.delete(fn)),
    replaceReducer: (r) => { reducer = r },
  }
}

function applyMiddleware(...middlewares) {
  return (createStore) => (reducer, pre) => {
    const store = createStore(reducer, pre)
    let dispatch = () => { throw new Error('构建中') }
    const api = { getState: store.getState, dispatch: (...a) => dispatch(...a) }   // 闭包指向链头
    const chain = middlewares.map((m) => m(api))
    dispatch = compose(...chain)(store.dispatch)
    return { ...store, dispatch }
  }
}

// 测试用中间件
const logger = (api) => (next) => (action) => {
  console.log('before', action.type)
  const r = next(action)
  console.log('after', api.getState())
  return r
}
const thunk = (api) => (next) => (action) => {
  if (typeof action === 'function') return action(api.dispatch, api.getState)   // 递归回链头
  return next(action)
}

// 用例
const reducer = (state = { n: 0 }, a) => a.type === 'ADD' ? { n: state.n + a.v } : state
const store = createStore(reducer, applyMiddleware(logger, thunk))
store.dispatch({ type: 'ADD', v: 2 })
// 输出: before ADD → after { n: 2 }（链：logger → thunk → base）
store.dispatch((dispatch) => { dispatch({ type: 'ADD', v: 3 }) })   // thunk：子 action 回到链头
console.log(store.getState())   // { n: 5 }
```
**评分点**：
- compose 从右到左 + 边界（零参 identity）
- applyMiddleware 的 api.dispatch 闭包指向链头（thunk 递归语义成立的关键）
- 中间件三参柯西化链的构建顺序（数组首位最外层）
- enhancer 作为 createStore 装饰器的形态
