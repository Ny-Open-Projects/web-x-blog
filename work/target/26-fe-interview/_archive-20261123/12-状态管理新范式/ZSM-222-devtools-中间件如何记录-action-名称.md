---
title: [ZSM-222] devtools 中间件怎么知道这次 set 对应哪个 action（源码级）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-222：devtools 中间件怎么知道这次 set 对应哪个 action（源码级）

**答**：
- devtools 中间件包装 set：调用时若第二个参数是字符串，直接作为 action 名上报 devtools；否则默认用 `{ type: 'setState', ... }`，显示为匿名 set
- 实现机制是在 devtools 里把顶层 set 包装为「检测 name 参数并转发」的代理，然后调用 config 时传入这个代理——业务代码只需 `set({ ... }, 'addTodo')`
- 它还会劫持 api：挂 dispatch/setState、把每次 state 变化 serialized 后 push 给 Redux DevTools 扩展（connect 走 __REDUX_DEVTOOLS_EXTENSION__ 全局钩子）
- 源码启示：给 set 加「第二个字符串参数」是约定而非类型系统魔法，TS 类型重载了 `(partial, name?: string)` 保证提示

```javascript
// 使用侧约定
const useStore = create(devtools((set) => ({
  todos: [],
  addTodo: (t) => set((s) => ({ todos: [...s.todos, t] }), 'addTodo'),  // 显式命名
})))

// 源码级简化：set 的包装
const setWithLog = (partial, name) => {
  devtools.send({ type: name ?? 'anonymous', payload: partial }, toSnapshot(get()))
  set(partial)
}
```
