---
title: [R19-160] 手写 Redux 核心：createStore、dispatch、subscribe、applyMiddleware？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-160：手写 Redux 核心：createStore、dispatch、subscribe、applyMiddleware？
**答**：
- createStore：闭包保存 currentState + listeners；dispatch 先跑 reducer 再通知；getState 返回当前引用。
- applyMiddleware 本质是 **dispatch 的装饰**：把 `({ getState, dispatch })` 注入中间件，链式包装出增强版 dispatch，形成 `action -> mw1 -> mw2 -> reducer` 的洋葱管道。
- 中间件约定 `store => next => action => result`，thunk 中间件就是"action 是函数就传 dispatch 给它"。
- 面试手写重点：reducer 纯函数、订阅通知在 reducer 之后、middleware 组合顺序（从右向左 compose）。

```javascript
// redux-mini.js —— 手写 Redux 核心
export function createStore(reducer, preloadedState, enhancer) {
  if (enhancer) return enhancer(createStore)(reducer, preloadedState);

  let currentState = preloadedState;
  let listeners = [];
  let isDispatching = false; // 防 reducer 内再 dispatch，保证纯函数

  function getState() {
    return currentState;
  }

  function dispatch(action) {
    if (isDispatching) throw new Error('Reducers may not dispatch actions.');
    isDispatching = true;
    try {
      currentState = reducer(currentState, action); // 纯函数收敛新 state
    } finally {
      isDispatching = false;
    }
    listeners.slice().forEach(l => l());            // 先改 state 再通知
    return action;
  }

  function subscribe(listener) {
    listeners.push(listener);
    return () => { listeners = listeners.filter(l => l !== listener); };
  }

  dispatch({ type: '@@redux/INIT' }); // 播种初始 state
  return { getState, dispatch, subscribe };
}

export function compose(...fns) {
  return fns.reduce((a, b) => (...args) => a(b(...args)));
}

export function applyMiddleware(...middlewares) {
  return (createStoreFn) => (reducer, preloadedState) => {
    const store = createStoreFn(reducer, preloadedState);
    let dispatch = store.dispatch;

    const middlewareAPI = {
      getState: store.getState,
      dispatch: (action) => dispatch(action), // 惰性引用，指向增强后的 dispatch
    };

    // 注入 middlewareAPI，得到 next => action => result 链
    const chain = middlewares.map(mw => mw(middlewareAPI));
    dispatch = compose(...chain)(store.dispatch); // 组合：mw1 包 mw2 包原始 dispatch
    return { ...store, dispatch };
  };
}

// ---- 内置一个 redux-thunk 验证 ----
const thunk = ({ getState, dispatch }) => next => action => {
  if (typeof action === 'function') {
    return action(dispatch, getState); // 异步 action：把 dispatch 交给业务
  }
  return next(action);
};

const counterReducer = (state = { count: 0 }, action) =>
  action.type === 'inc' ? { count: state.count + 1 } : state;

const store = createStore(counterReducer, undefined, applyMiddleware(thunk));
store.subscribe(() => console.log('state:', store.getState()));

store.dispatch({ type: 'inc' });
store.dispatch(async (dispatch) => {       // thunk 异步流程
  await Promise.resolve();
  dispatch({ type: 'inc' });
});
```
