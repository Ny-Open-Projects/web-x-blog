---
title: [ZSM-029] Zustand 的 actions 里怎么做异步请求和乐观更新？和 thunk 相比差在哪？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-029：Zustand 的 actions 里怎么做异步请求和乐观更新？和 thunk 相比差在哪？
**答**：
- action 就是普通函数，async/await 直接写，await 后用 set/get 更新，没有 dispatch 中间层。
- 乐观更新：先 set 期望值，请求失败回滚并记录旧值；并发请求要按序号防覆盖。
- 和 thunk 的差异：thunk 拿到的 getState 是「dispatch 时刻的视图」，Zustand 的 get 始终最新；thunk 的 action 可被日志/中间件统一记录，Zustand 的异步过程对 devtools 不可见（除非手动派发）。
- 复杂副作用链建议抽成 service 函数，store 只持有状态，避免 action 膨胀。

```javascript
const useTodos = create((set, get) => ({
  todos: [], loading: false,
  async toggle(id) {
    const prev = get().todos.map(t => ({ ...t })) // 乐观前快照
    set(s => ({ todos: s.todos.map(t => t.id === id ? { ...t, done: !t.done } : t) }))
    try {
      await api.toggleTodo(id)
    } catch (e) {
      set({ todos: prev }) // 失败回滚
      toast.error('更新失败')
    }
  },
}))
```
