---
title: [FRP-189] 手写 redux mini：createStore + combineReducers + applyMiddleware？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-189：手写 redux mini：createStore + combineReducers + applyMiddleware？

**答**：
- createStore 内核：state 闭包 + `getState/dispatch/subscribe`；dispatch 里 `state = reducer(state, action)` 纯函数替换，然后通知订阅者。
- combineReducers：把多个子 reducer 组合成一个——每个子 reducer 只管自己分支，合并成新 state 对象（引用未变的分支保持原对象，浅比较优化可用）。
- applyMiddleware 的经典三段式：改造 dispatch 形成**洋葱链**——`chain = middlewares.map(mw => mw(store))`，再 `compose(...chain)(store.dispatch)`。
- 关键认知：middleware 拿到的是 `getState` 与"下一个 dispatch"，thunk 之类都是靠"拦截 action 是函数就不继续"实现的。

```javascript
// 简化实现，帮助理解 redux mini
function createStore(reducer, preloadedState, enhancer) {
  if (enhancer) return enhancer(createStore)(reducer, preloadedState); // enhancer 包装整个 store

  let state = reducer(preloadedState, { type: '@@INIT' });  // 用初始 action 求初始 state
  const listeners = new Set();
  let isDispatching = false;                                // 防 reducer 内 dispatch

  function getState() { return state; }
  function dispatch(action) {
    if (typeof action.type === 'undefined') throw new Error('action 需要 type');
    if (isDispatching) throw new Error('reducer 执行期间禁止 dispatch');
    isDispatching = true;
    try { state = reducer(state, action); }                 // 核心：纯函数替换
    finally { isDispatching = false; }
    listeners.forEach(fn => fn());                          // 通知订阅
    return action;
  }
  function subscribe(fn) {
    listeners.add(fn);
    return () => listeners.delete(fn);
  }
  return { getState, dispatch, subscribe };
}

function combineReducers(reducers) {
  return (state = {}, action) => {
    let hasChanged = false;
    const next = {};
    for (const key in reducers) {
      const prevBranch = state[key];
      const nextBranch = reducers[key](prevBranch, action); // 每个子 reducer 只处理自己分支
      next[key] = nextBranch;
      hasChanged ||= nextBranch !== prevBranch;             // 引用比较：未变分支保持原对象
    }
    return hasChanged ? next : state;                       // 全没变：返回原 state（性能）
  };
}

function applyMiddleware(...middlewares) {
  return (createStore) => (reducer, preloadedState) => {
    const store = createStore(reducer, preloadedState);
    let dispatch = store.dispatch;

    const api = {
      getState: store.getState,
      dispatch: (action) => dispatch(action),  // 注意：指向"最终 dispatch"，链上共享
    };
    const chain = middlewares.map(mw => mw(api));           // 第一段：注入 store api
    dispatch = compose(...chain)(store.dispatch);           // 第二段：洋葱包裹原生 dispatch
    return { ...store, dispatch };
  };
}

const compose = (...fns) => fns.reduce((a, b) => (...args) => a(b(...args)));

// 经典 middleware：thunk 与 logger
const thunk = ({ dispatch, getState }) => (next) => (action) =>
  typeof action === 'function' ? action(dispatch, getState) : next(action);
const logger = ({ getState }) => (next) => (action) => {
  console.log('prev', getState());
  const r = next(action);                    // 进入下一层，最终到原生 dispatch
  console.log('next', getState());
  return r;
};

// 组装：
// const store = createStore(rootReducer, undefined, applyMiddleware(thunk, logger));
// dispatch 的调用链：thunk -> logger -> 原生 dispatch -> reducer
```
