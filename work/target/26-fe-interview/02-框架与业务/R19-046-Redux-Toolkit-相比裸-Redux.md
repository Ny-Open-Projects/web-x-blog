---
title: [R19-046] Redux Toolkit 相比裸 Redux 解决了什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-046：Redux Toolkit 相比裸 Redux 解决了什么？
**答**：
- createSlice 自动生成 action creator 与 type 常量，消灭手写 actionType 样板。
- 内置 Immer，reducer 里可以直接"修改"state 写法（实际产出不可变更新）。
- configureStore 默认集成 thunk 中间件与 Redux DevTools，开箱即用。
- 数据流仍是单向的：dispatch action -> reducer -> 新 state -> useSelector 订阅更新。

```jsx
import { configureStore, createSlice } from '@reduxjs/toolkit';
import { Provider, useDispatch, useSelector } from 'react-redux';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1; // 内置 Immer，允许直接改
    },
  },
});

const store = configureStore({ reducer: { counter: counterSlice.reducer } });

function Counter() {
  const value = useSelector((s) => s.counter.value);
  const dispatch = useDispatch();

  return (
    <button onClick={() => dispatch(counterSlice.actions.increment())}>
      {value}
    </button>
  );
}

export default function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}
```
