---
title: [DP-088] redux 源码里能识别出哪些设计模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-088：redux 源码里能识别出哪些设计模式？（高频）
**答**：
- **观察者**：`store.subscribe(listener)` + `dispatch` 后遍历通知——最小观察者实现。
- **职责链/装饰器**：`applyMiddleware(...mws)` 把中间件串成 `store => next => action` 链，依次包裹 dispatch（洋葱）。
- **命令模式**：action 是命令对象（type + payload），reducer 是解释器（纯函数解释命令生成新状态）。
- **工厂**：`createStore` 是工厂，按 enhancer 参数组装出增强版 store；`combineReducers` 是组合模式（子 reducer 树）。

```javascript
// redux 源码骨架还原（ createStore + applyMiddleware + combineReducers）
function combineReducers(reducers) {           // 组合模式：reducer 树
  return function combined(state = {}, action) {
    let hasChanged = false;
    const nextState = {};
    for (const key of Object.keys(reducers)) {
      nextState[key] = reducers[key](state[key], action); // 命令沿树分发给各子 reducer
      hasChanged ||= nextState[key] !== state[key];
    }
    return hasChanged ? nextState : state;     // 引用不变则整体返回旧 state（享元/结构共享）
  };
}
function createStore(reducer, enhancer) {
  if (enhancer) return enhancer(createStore)(reducer); // 工厂：把组装权交给增强器
  let state = reducer(undefined, { type: '@@redux/INIT' });
  const listeners = new Set();
  return {
    getState: () => state,
    dispatch: (action) => {
      if (!action.type) throw new Error('action 需要 type'); // 命令对象约束
      state = reducer(state, action);
      listeners.forEach((l) => l());           // 观察者通知
      return action;
    },
    subscribe: (l) => { listeners.add(l); return () => listeners.delete(l); },
  };
}
const applyMiddleware = (...middlewares) => (createStore) => (reducer) => {
  const store = createStore(reducer);
  let dispatch = store.dispatch;
  const chain = middlewares.map((mw) => mw({ getState: store.getState, dispatch: (a) => dispatch(a) }));
  dispatch = chain.reduceRight((next, mw) => mw(next), store.dispatch); // 从右向左包裹（洋葱）
  return { ...store, dispatch };
};
// 装配
const logger = ({ getState }) => (next) => (action) => {
  console.log('prev', getState());
  const r = next(action);
  console.log('next', getState());
  return r;
};
const reducer = combineReducers({
  count: (s = 0, a) => (a.type === 'inc' ? s + 1 : s),
});
const store = createStore(reducer, applyMiddleware(logger));
store.dispatch({ type: 'inc' });
// prev {count: 0} -> next {count: 1} —— 命令进入，观察者更新
```
