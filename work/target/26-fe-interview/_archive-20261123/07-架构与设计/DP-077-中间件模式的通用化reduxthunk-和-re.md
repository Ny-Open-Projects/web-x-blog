---
title: [DP-077] 中间件模式的通用化：redux-thunk 和 redux-saga 的模式差异？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-077：中间件模式的通用化：redux-thunk 和 redux-saga 的模式差异？（高频）
**答**：
- 中间件通用形态：`store => next => action => result`——三层柯里化，拦截 action，可改写/短路/异步化（职责链）。
- redux-thunk：action 允许是函数，注入 `dispatch/getState`——用"命令对象扩展"实现异步，逻辑散在 action 里，简单直接。
- redux-saga：用 Generator 把副作用抽到独立 saga（解释器/协程思想），`take/effect` 描述副作用、由引擎执行——逻辑集中、可测试（yield 纯描述可断言）。
- 选型：简单异步用 thunk；复杂流程编排（竞态、取消、并发、轮询）用 saga/observable 类方案。

```javascript
// 1. redux 中间件的三层柯里化骨架
function createStore(reducer, enhancer) {
  let state = reducer(undefined, {});
  const listeners = new Set();
  const getState = () => state;
  const baseDispatch = (action) => { state = reducer(state, action); listeners.forEach((l) => l()); };
  const store = { getState, dispatch: baseDispatch, subscribe: (l) => { listeners.add(l); return () => listeners.delete(l); } };
  return enhancer ? enhancer(createStore)(reducer) : store; // 交给中间件增强
}
const applyMiddleware = (...mws) => (createStore) => (reducer) => {
  const store = createStore(reducer);
  let dispatch = store.dispatch;
  const api = { getState: store.getState, dispatch: (a) => dispatch(a) };
  const chain = mws.map((mw) => mw(api));                       // 第一层：注入 store API
  dispatch = chain.reduce((next, mw) => mw(next), store.dispatch); // 第二层：串成职责链
  return { ...store, dispatch: (a) => dispatch(a) };            // 第三层在调用时生效
};
// 2. thunk：拦截函数型 action（命令扩展）
const thunk = ({ getState, dispatch }) => (next) => (action) =>
  typeof action === 'function' ? action(dispatch, getState) : next(action); // 短路：函数自己接管
// 3. saga 思想：副作用描述与执行分离（解释器模式）
function* userSaga() {
  // yield take('FETCH_USER')        // 等待事件
  // const user = yield call(api.fetchUser, id)   // 描述副作用，不直接执行
  // yield put({ type: 'USER_OK', user })          // 描述 dispatch
}
// saga 引擎（示意）：迭代器驱动，逐步"解释执行" effect
function sagaEngine(gen) {
  const it = gen();
  (function step(input) {
    const { value, done } = it.next(input);
    if (done) return;
    // value 是 effect 描述符，由引擎统一执行 —— 可测试性的来源
    Promise.resolve(value).then((r) => step(r));
  })();
}
sagaEngine(function* () { const r = yield Promise.resolve('saga 结果'); console.log(r); });
```
