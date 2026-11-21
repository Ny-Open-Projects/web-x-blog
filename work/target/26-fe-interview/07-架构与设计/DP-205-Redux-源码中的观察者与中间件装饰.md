---
title: [DP-205] 源码识别：Redux 源码中的观察者与中间件装饰？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-205：源码识别：Redux 源码中的观察者与中间件装饰？
**答**:
- 观察者：store.subscribe(listener) 是最小观察者（Set 存 listener，dispatch 后遍历通知）；React-Redux 的 selector 缓存（连接层）在其上做 memo。
- 命令模式：action 是命令对象（type + payload），reducer 是"命令 → 状态转移"的解释器； combineReducers 是组合模式（子 reducer 树）。
- 装饰：applyMiddleware 把 dispatch 包成 `chain = middles.map(m => m(api))` 再 compose 注入——对 dispatch 逐层装饰，thunk/saga 都挂在这条装饰链上。
- 识别要点：一句话总结"Redux = 命令( action ) + 状态机( reducer ) + 观察者( subscribe )，中间件是 dispatch 的装饰器"。

```javascript
// Redux 核心源码级简化
function createStore(reducer, enhancer) {
  let state; const listeners = new Set();
  const store = {
    getState: () => state,
    dispatch: action => { state = reducer(state, action); listeners.forEach(l => l()); return action; }, // 通知
    subscribe: l => { listeners.add(l); return () => listeners.delete(l); },
  };
  return enhancer ? enhancer(createStore)(reducer) : store;      // 装饰入口
}
const applyMiddleware = (...middles) => next => (...a) => {
  const store = next(...a);
  const api = { getState: store.getState, dispatch: (act) => chainDispatch(act) };
  const chain = middles.map(m => m(api));                        // 装饰链
  const chainDispatch = compose(chain)(store.dispatch);          // dispatch 被层层包裹
  return { ...store, dispatch: chainDispatch };
};
// combineReducers = 组合模式：顶层 dispatch 递归分发给各子 reducer
```
