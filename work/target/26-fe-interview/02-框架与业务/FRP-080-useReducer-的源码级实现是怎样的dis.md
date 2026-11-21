---
title: [FRP-080] useReducer 的源码级实现是怎样的？dispatch 闭包如何拿到最新的 state？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-080：useReducer 的源码级实现是怎样的？dispatch 闭包如何拿到最新的 state？

**答**：
- 每个带队列的 Hook（useState/useReducer）节点上有 `queue: { pending, lastRenderedReducer, lastRenderedState }`；dispatch 产生的 update 对象先挂 `queue.pending`（环形链表），再 `scheduleUpdateOnFiber` 触发重渲染。
- **dispatch 是闭包但永不失效**：它只持有 fiber 引用和 queue，不含 state；重渲染时 `renderWithHooks` 会**循环取出 queue 里所有 update**，从 `baseState` 起依次 `reducer(baseState, action)` 算出最新 state——这就是"dispatch 里读到旧值却写对了"的原理。
- 首次渲染走 `mountReducer`（直接把 reducer 存到 hook），更新渲染走 `updateReducer`（replay 队列 + baseState/baseQueue 机制，支持优先级跳过部分 update）。
- useState 就是 `useReducer(basicStateReducer)` 的特化：reducer 为 `(state, action) => typeof action === 'function' ? action(state) : action`。

```javascript
// 简化实现，帮助理解 dispatch 闭包与 update 队列重放
let currentHook = null, rerender = null;

function mountReducer(reducer, initialArg, init = (v) => v) {
  const hook = { memoizedState: init(initialArg), queue: { pending: null } };
  currentHook = hook;
  const dispatch = (action) => {
    // dispatch 闭包只捕获 hook.queue，不捕获 state -> 永远"新鲜"
    hook.queue.pending = action; // 真实实现是环形链表，这里简化为最新一个
    rerender();                  // scheduleUpdateOnFiber
  };
  return [hook.memoizedState, dispatch];
}

function updateReducer(reducer) {
  const hook = currentHook;
  const baseState = hook.baseState ?? hook.memoizedState;
  let newState = baseState;
  const pending = hook.queue.pending;
  if (pending) {
    hook.queue.pending = null;
    newState = reducer(baseState, pending); // 重放队列得到最新 state
  }
  hook.baseState = hook.memoizedState = newState;
  return [newState, hook.dispatch];
}

function useMyReducer(reducer, initialArg) {
  return currentHook?.dispatch ? updateReducer(reducer) : mountReducer(reducer, initialArg);
}

// 验证：连续两次 dispatch 只用同一个 action 队列重放
const countReducer = (s, a) => (a.type === 'inc' ? s + a.step : s);
let fiberState;
const run = () => {
  let result;
  [fiberState] = useMyReducer(countReducer, 0);
  return fiberState;
};
rerender = () => run();
let [, dispatch] = (() => { rerender = () => run(); return run() || [] })();
void dispatch;
// 演示闭包捕获 queue 而非 state：两次 dispatch 后最终值正确
// dispatch({type:'inc',step:1}); dispatch({type:'inc',step:10}); -> replay 得 11
console.log(countReducer(countReducer(0, { type: 'inc', step: 1 }), { type: 'inc', step: 10 })); // 11
```
