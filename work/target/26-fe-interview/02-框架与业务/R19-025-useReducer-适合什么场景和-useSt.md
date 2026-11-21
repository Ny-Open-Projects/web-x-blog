---
title: [R19-025] useReducer 适合什么场景？和 useState 怎么选？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-025：useReducer 适合什么场景？和 useState 怎么选？
**答**：
- state 由多个子值组成、更新逻辑之间存在关联或依赖前值时，useReducer 把逻辑集中到 reducer。
- reducer 是纯函数：接收当前 state 与 action，返回新 state，方便测试和时间旅行。
- 多个组件共享同一套更新逻辑时，把 dispatch 传下去比传多个回调更清晰。
- 简单独立的字段用 useState，复杂对象流转用 useReducer。

```jsx
import { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'add':
      return { ...state, todos: [...state.todos, action.payload] };
    case 'remove':
      return { ...state, todos: state.todos.filter((t) => t.id !== action.id) };
    case 'clear':
      return { ...state, todos: [] };
    default:
      return state;
  }
}

export default function Todos() {
  const [state, dispatch] = useReducer(reducer, { todos: [] });

  return (
    <>
      <button
        onClick={() =>
          dispatch({ type: 'add', payload: { id: Date.now(), text: '新任务' } })
        }
      >
        添加
      </button>
      <button onClick={() => dispatch({ type: 'clear' })}>清空</button>
      <ul>
        {state.todos.map((t) => (
          <li key={t.id} onClick={() => dispatch({ type: 'remove', id: t.id })}>
            {t.text}
          </li>
        ))}
      </ul>
    </>
  );
}
```
