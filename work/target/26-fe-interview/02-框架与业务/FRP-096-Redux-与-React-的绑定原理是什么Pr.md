---
title: [FRP-096] Redux 与 React 的绑定原理是什么？Provider 和 connect 各自做了什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-096：Redux 与 React 的绑定原理是什么？Provider 和 connect 各自做了什么？

**答**：
- Redux 本体与 React 无关：`createStore(reducer)` 返回 `{ getState, dispatch, subscribe }`。绑定层（react-redux）做两件事：**把 store 放进 Context**（Provider）与**把 store 映射为 props 并订阅更新**（connect）。
- Provider：`<Provider store={store}>` 内部一个组件把 `store.getState()` 放入 Context value 并 `store.subscribe`——state 变化时更新 Context value 触发整棵 Provider 子树重渲染（v7 前）；v8 改为订阅层 `useSyncExternalStore`，Provider 只提供 store 实例不再存 state，性能大幅改善。
- connect(mapStateToProps, mapDispatchToProps)(Component)：HOC 内部 `subscribe(() => { if (!shallowEqual(mapped, prev)) forceUpdate(); })`——订阅 + **mapState 结果浅比较**决定是否 forceUpdate，这是 Redux 时代的"精准订阅"实现。
- useSelector（Hooks API）与 connect 的订阅本质相同，区别是钩子化 + 每次 render 重新执行 selector。

```javascript
// 简化实现，帮助理解 Provider 与 connect 的绑定
function createStore(reducer, preloadedState) {
  let state = preloadedState;
  const listeners = new Set();
  return {
    getState: () => state,
    dispatch: (action) => {
      state = reducer(state, action);   // 纯函数计算新 state
      listeners.forEach((l) => l());    // 同步通知所有订阅者
      return action;
    },
    subscribe: (l) => { listeners.add(l); return () => listeners.delete(l); },
  };
}

// Provider：把 store 放进 Context（react-redux v8 形态：只放实例，不放 state）
const StoreContext = { _currentValue: null };
function Provider({ store, children }) {
  StoreContext._currentValue = store;
  return children;
}

// connect：HOC = 订阅 + mapState 浅比较 + forceUpdate
function connect(mapStateToProps, mapDispatchToProps) {
  return function wrap(WrappedComponent) {
    return function ConnectWrapper(props) {
      const store = StoreContext._currentValue;
      let mapped = mapStateToProps(store.getState(), props);
      const actions = mapDispatchToProps(store.dispatch);
      // 订阅：state 变化 -> 重算 mapState -> 浅比较决定是否重渲染
      store.subscribe(() => {
        const next = mapStateToProps(store.getState(), props);
        if (!shallowEqual(mapped, next)) {
          mapped = next;
          console.log(`[connect] ${WrappedComponent.name} re-render`);
        }
      });
      return WrappedComponent({ ...props, ...mapped, ...actions });
    };
  };
}
const shallowEqual = (a, b) => Object.keys(a).length === Object.keys(b).length
  && Object.keys(a).every((k) => a[k] === b[k]);

// 用法
const reducer = (s = { count: 0 }, a) => (a.type === 'inc' ? { ...s, count: s.count + 1 } : s);
const store = createStore(reducer);
const Counter = ({ count, inc }) => ({ count, inc });
const ConnectedCounter = connect((s) => ({ count: s.count }), (d) => ({ inc: () => d({ type: 'inc' }) }))(Counter);

Provider({ store, children: null });
ConnectedCounter({});
store.dispatch({ type: 'inc' }); // [connect] Counter re-render
```
