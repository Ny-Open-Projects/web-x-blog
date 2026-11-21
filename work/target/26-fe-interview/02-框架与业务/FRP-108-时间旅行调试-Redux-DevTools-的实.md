---
title: [FRP-108] 时间旅行调试（Redux DevTools）的实现思想是什么？"重放"是怎么做的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-108：时间旅行调试（Redux DevTools）的实现思想是什么？"重放"是怎么做的？

**答**：
- 前提：**状态是 action 序列的纯函数**——`state = actions.reduce(reducer, initialState)`。只要记录 (action, 按需快照) 列表，任意时刻的状态都能从历史重算出来。
- DevTools 增强（store enhancer）：包装 dispatch——每次 dispatch 前**deep copy 当前 state 推入历史**（或直接存 action，展示时重算），并把历史暴露给面板；面板执行"跳转到第 N 步"= 取前 N 个 action 重放，或直接读快照。
- 重放要求 reducer 纯（无副作用、无 Date/random 直接调用）——这也解释了为什么 Side Effect 必须移出 reducer（middleware 层处理），否则重放结果失真。
- 与 Vue 对应物：Pinia 可用 `$patch` 序列化 + devtools 插件实现类似能力；本质都是"**可序列化的变更日志 + 纯函数重放**"。

```javascript
// 简化实现，帮助理解 action 日志与重放
function devToolsEnhancer(createStore) {
  return (reducer, preloadedState) => {
    const store = createStore(reducer, preloadedState);
    const history = [{ type: '@@INIT', state: store.getState() }];

    return {
      ...store,
      dispatch: (action) => {
        const result = store.dispatch(action);
        history.push({ type: action.type, state: store.getState() }); // 记录每步快照
        return result;
      },
      // 时间旅行：跳回第 n 步 —— 前缀 action 重放（比存全量快照省内存的方案）
      jumpTo(n) {
        let state = history[0].state;
        const replayReducer = store.getState.__reducer ?? reducer;
        for (let i = 1; i <= n; i++) state = replayReducer(state, { type: history[i].type });
        return state;
      },
      getHistory: () => history.map((h) => h.type),
    };
  };
}

// 用法：todos reducer（纯函数 -> 重放可靠）
const reducer = (s = [], a) =>
  a.type === 'add' ? [...s, a.text] : a.type === 'del' ? s.slice(0, -1) : s;

const store = devToolsEnhancer((r, p) => {
  let state = p;
  const listeners = new Set();
  return {
    getState: () => state,
    dispatch: (a) => { state = r(state, a); listeners.forEach((f) => f()); return a; },
    subscribe: (f) => listeners.add(f),
  };
})(reducer);

store.dispatch({ type: 'add', text: 'a' });
store.dispatch({ type: 'add', text: 'b' });
store.dispatch({ type: 'del' });
console.log('历史:', store.getHistory()); // @@INIT, add, add, del
console.log('跳回第 2 步:', store.jumpTo(2)); // ['a', 'b']：add add 重放结果
console.log('当前:', store.getState());       // ['a']
```
