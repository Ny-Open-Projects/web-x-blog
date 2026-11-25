---
title: [ZSM-658] Redux 的 store enhancer 链：dispatch 被包装了几层
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-658：Redux 的 store enhancer 链：dispatch 被包装了几层

**答**：
- Redux 的组装分两层：**enhancer**（包装整个 createStore：如 applyMiddleware 让 dispatch 能收 action 对象、devtools enhancer 包装 subscribe/send）和 **middleware**（包装 dispatch 本身，逐个拦截 action）。`createStore(reducer, preloadedState, compose(applyMiddleware(m1, m2), devTools))` 的执行序：外层 enhancer 先包，applyMiddleware 在内层再包 dispatch。
- middleware 链结构：`applyMiddleware(m1, m2)` 生成的 dispatch 是 `m1(api)(m2(api)(store.dispatch))`——**数组第一个在最外层**，action 先流经 m1 再到 m2 最后到 reducer。执行顺序想错了（如日志中间件放错位置）就会出现「日志里看不到最终状态」或「thunk 里 dispatch 被 devtools 记两次」。
- 中间件三参签名 `(store) => (next) => (action) => result`：store 是 `{ getState, dispatch }`（受限 API，不含 replaceReducer），next 是链上下一环。thunk 中间件调用 `store.dispatch` 会**从链条头重新走一遍**（新 action 全链可见），而调用 `next(action)` 只往下游传。
- 数量感知：一个典型 RTK 应用 dispatch 被包 3~5 层（thunk → serializableCheck → immutableCheck → devtools → base dispatch）——每次 dispatch 的开销就是这几层函数调用，微秒级，不是瓶颈；瓶颈通常在 reducer 或订阅通知。
- 追问钩子：`compose(f, g)(x) = f(g(x))`——理解 compose 从右到左，就理解了 middleware 顺序和 enhancer 顺序的所有表象。

```javascript
// applyMiddleware 骨架（Redux 源码简化）
function applyMiddleware(...middlewares) {
  return (createStore) => (reducer, preloadedState) => {
    const store = createStore(reducer, preloadedState)
    let dispatch = () => { throw new Error('构建中不允许 dispatch') }
    const middlewareAPI = { getState: store.getState, dispatch: (...args) => dispatch(...args) }
    const chain = middlewares.map((m) => m(middlewareAPI))
    dispatch = compose(...chain)(store.dispatch)   // 从右到左包裹
    return { ...store, dispatch }
  }
}

// thunk 中间件（源码原样）
const thunk = ({ dispatch, getState }) => (next) => (action) => {
  if (typeof action === 'function') {
    return action(dispatch, getState)   // 函数型 action：递归 dispatch（回到链头）
  }
  return next(action)
}

// 层级可视化
// dispatch(thunkAction)
//   → thunk 层：识别函数 → dispatch(innerActions...) 回到链头
//     → serializableCheck：检查 payload 可序列化
//     → devtools 层：send 给扩展
//     → base dispatch：reducer 执行 + 通知订阅

// 顺序影响验证
// applyMiddleware(logger, thunk) —— thunk 在内层：logger 能看到 thunk 派发的每个子 action
// applyMiddleware(thunk, logger) —— logger 在内层：只看到原始 thunkAction，子 action 不可见
```
