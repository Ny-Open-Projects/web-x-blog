---
title: [FRP-034] useReducer 与 useState 是什么关系？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-034：useReducer 与 useState 是什么关系？

**答**：
- 源码中 `useState` 就是 `useReducer(basicStateReducer, initial)` 的特例：basicStateReducer 即 `action => typeof action === 'function' ? action(state) : action`——所以 useState 的 setter 支持传函数或传值。
- useReducer 把"怎么改"集中到 reducer：多来源修改同一 state 时逻辑内聚、dispatch 引用永远稳定（不像多个 setter 各自闭包）。
- dispatch 是稳定的：它只往 hook 的 queue 里 push action，不依赖本次渲染的任何值，所以可以安全放进子组件 props 而无需 useCallback。
- 两者共享同一套 hook 链表与批处理机制，性能无本质差异。

```javascript
// 简化实现，帮助理解 useState 是 useReducer 的特例
function useReducer(reducer, initialArg, init) {
  const hook = workInProgressHook;
  if (isMount) {
    hook.memoizedState = init ? init(initialArg) : initialArg;
    hook.queue = [];
  } else {
    hook.queue.forEach((action) => {
      // 与 useState 唯一的区别：计算新 state 走 reducer
      hook.memoizedState = reducer(hook.memoizedState, action);
    });
    hook.queue.length = 0;
  }
  const dispatch = (action) => {
    hook.queue.push(action);
    scheduleRender(currentFiber);
  };
  return [hook.memoizedState, dispatch];
}

// basicStateReducer：useState 的 reducer 就是"直接应用 action"
function basicStateReducer(state, action) {
  return typeof action === 'function' ? action(state) : action;
}

function useState(initialState) {
  return useReducer(basicStateReducer, initialState);
}

// 验证：setCount(1) 与 setCount(n => n + 1) 都被 basicStateReducer 解释
// const [count, setCount] = useState(0);
// setCount(1);            // basicStateReducer(0, 1) => 1
// setCount((n) => n + 1); // basicStateReducer(1, n => n+1) => 2
```
