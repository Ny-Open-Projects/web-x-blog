---
title: [R19-136] 手写一个简化版 useReducer，它和 useState 在实现上差在哪？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-136：手写一个简化版 useReducer，它和 useState 在实现上差在哪？
**答**：
- useReducer 与 useState 共用同一套"队列 + 重渲染"机制，差别只在**更新语义**：入队的是 action，消费时统一走 `reducer(state, action)` 收敛出新 state。
- reducer 必须是纯函数：同一输入永远同一输出，不写副作用——这是让"多次更新可正确批量重放"的前提。
- 优势：更新逻辑集中可测、dispatch 引用稳定、复杂状态转换有单一事实来源。
- useState 本质上可以看成 `useReducer(reducer 为基础赋值)` 的特例——React 源码里正是这么实现的。

```jsx
// mini-react.js —— 手写 useReducer：action 入队 + reducer 收敛
export function useReducer(reducer, initialArg, init) {
  const fiber = currentFiber;
  const index = hookIndex++;
  const hooks = fiber.hooks;

  if (hooks[index] === undefined) {
    hooks[index] = {
      state: init ? init(initialArg) : initialArg, // 支持惰性初始化
      queue: [],
    };
  }
  const hook = hooks[index];

  // 与 useState 唯一不同：消费时走 reducer 纯函数
  while (hook.queue.length) {
    const action = hook.queue.shift();
    hook.state = reducer(hook.state, action);
  }

  function dispatch(action) {
    hook.queue.push(action);
    scheduleUpdate(fiber);
  }
  return [hook.state, dispatch];
}

// ---- 实战：购物车 —— 所有状态转换集中在一个可单测的纯函数里 ----
function cartReducer(state, action) {
  switch (action.type) {
    case 'add':
      return {
        ...state,
        items: [...state.items, action.item],
        total: state.total + action.item.price,
      };
    case 'remove':
      return {
        ...state,
        items: state.items.filter(i => i.id !== action.id),
        total: state.total - state.items.find(i => i.id === action.id).price,
      };
    case 'clear':
      return { items: [], total: 0 };
    default:
      throw new Error(`unknown action: ${action.type}`);
  }
}

// cartReducer 可脱离 React 直接单测：
// expect(cartReducer({items: [], total: 0}, {type: 'add', item: {id: 1, price: 9}}))
//   .toEqual({items: [{id: 1, price: 9}], total: 9});
```
