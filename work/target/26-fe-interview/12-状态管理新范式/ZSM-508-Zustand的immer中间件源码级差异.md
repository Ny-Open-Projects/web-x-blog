---
title: [ZSM-508] Zustand 的 immer 中间件内部是怎么桥接 produce 与 set 的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-508：Zustand 的 immer 中间件内部是怎么桥接 produce 与 set 的

**答**：
- immer 中间件包装了 `set`：用户写的 `set((s) => { s.count++ })` 会被包成 `set(produce(fn))`——produce 返回新状态树（没有变化时返回原引用），再走 Zustand 原生的浅合并。
- 关键细节：produce 返回 undefined 时 immer 直接沿用 draft 里的修改（mutate 式），Zustand 侧约定「返回值即新状态」，所以中间件里判断 produce 结果非 undefined 才替换，否则用 draft 本身。
- 代价与陷阱： immer 的 Proxy draft 有开销，大数组高频更新（拖拽、动画）不适合；draft 内不能做异步或产生副作用（console 可以，fetch 不行）。
- 依赖版本：中间件要求 React 18+ / zustand v4+，`enableMapSet` 需手动开启 Map/Set 支持；嵌套 store 引用 draft 化的对象跨 store 使用会报「不可变外泄」错误。
- 追问钩子：为什么 immer 和 persist 组合时要保证 immer 在内层？因为 persist 需要拿到序列化友好的普通对象，draft 不能直接进 JSON。

```javascript
// 简化的 immer 中间件实现
import { produce } from 'immer'

function immerImpl(initializer) {
  return (set, get, store) => {
    store.setState = (updater, replace, ...rest) => {
      const setStateImpl = store.setState
      setStateImpl(
        (state) => {
          const nextState = produce(updater)(state)   // 桥接点
          // updater 返回 undefined：沿用 draft 的修改结果
          return nextState !== undefined ? nextState : state
        },
        replace,
        ...rest
      )
    }
    return initializer(store.setState, get, store)
  }
}

// 用法与陷阱示例
const useStore = create(immer()((set) => ({
  todos: [],
  add: (t) => set((s) => { s.todos.push({ text: t, done: false }) }), // 直接 mutate
  // 反例：draft 里异步
  // bad: async () => set(async (s) => { s.x = await api() }) // throw
})))
```
