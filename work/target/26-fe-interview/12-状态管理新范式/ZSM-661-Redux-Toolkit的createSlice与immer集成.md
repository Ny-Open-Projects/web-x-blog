---
title: [ZSM-661] RTK 的 createSlice 内部：immer produce 与 reducer 注册表
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-661：RTK 的 createSlice 内部：immer produce 与 reducer 注册表

**答**：
- createSlice 做三件事：1) 遍历 reducers 配置生成 **action creator**（`type: `${name}/${key}`` 唯一命名 + auto-prepare：payload 直接透传或 prepare 回调自定义）；2) 把每个 reducer 包上 **immer produce**（`(state, action) => { state.xxx = ... }` 写法，draft 机制自动产出不可变新状态）；3) 输出总 reducer：`type` 在注册表里的走对应 reducer，未匹配返回原 state（reducer 必须是纯函数总闸）。
- prepare 回调的价值：把「组件里的复杂构造」收进 slice——`addTodo: { reducer(state, action), prepare(text) { return { payload: { id: nanoid(), text, createdAt: Date.now() } } } }`——payload 含 id/时间戳的生成逻辑集中一处，组件只传语义参数。
- extraReducers：slice 可以监听**其他 slice 或 thunk 的 action**（builder.addCase(fetchThunk.fulfilled, ...)）——跨 slice 数据流的正规通道，避免 action type 字符串耦合。
- immer 集成的边界（同 ZSM-508）：draft 里不能异步、不能重赋值整个 state（replace 要用 return）；嵌套大数组高频更新仍有 Proxy 成本。
- 追问钩子：RTK 的 `createSlice` + `configureStore` 默认就开了 devtools/immutability/serializability 检查——中间件链的默认配置即「最佳实践自动化」。

```javascript
import { createSlice, nanoid } from '@reduxjs/toolkit'

const todosSlice = createSlice({
  name: 'todos',
  initialState: { items: [], filter: 'all' },
  reducers: {
    // 普通形式：直接 draft mutate
    addTodo: {
      reducer(state, action) {
        state.items.push(action.payload)          // immer draft：看似可变
      },
      // prepare：payload 构造收进 slice
      prepare(text) {
        return { payload: { id: nanoid(), text, done: false, createdAt: Date.now() } }
      },
    },
    toggleTodo(state, action) {
      const t = state.items.find((i) => i.id === action.payload)
      if (t) t.done = !t.done                     // 深层 mutate 也是合法 draft
    },
    setFilter(state, action) { state.filter = action.payload },
  },
  // 监听其他 thunk
  extraReducers: (builder) => {
    builder
      .addCase(fetchTodos.fulfilled, (state, action) => { state.items = action.payload })
      .addCase(fetchTodos.rejected, (state, action) => { state.error = action.error.message })
  },
})

// 使用
dispatch(todosSlice.actions.addTodo('写周报'))   // prepare 生成 payload
// type: 'todos/addTodo' —— 唯一命名防冲突
```
