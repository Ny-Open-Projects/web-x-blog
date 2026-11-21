---
title: [ZSM-221] Zustand 中间件是怎么包装 set 和 get 的（源码级）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-221：Zustand 中间件是怎么包装 set 和 get 的（源码级）

**答**：
- 中间件本质是高阶函数：`(config) => (set, get, api) => config(wrappedSet, get, api)`，洋葱式包裹 create 的初始化函数
- 每个 `create(mw1(mw2(fn)))` 的调用链里，外层中间件拿到的是「内层包装过的 set」，所以调用顺序决定包装层级——这是顺序敏感的根源
- 包装只发生在 store 创建时一次，运行时零开销：set 调用会依次穿过每层中间件再到达 vanilla store 的 setState
- api 对象是共享引用，中间件还可以在 api 上挂新方法（如 subscribeWithSelector 给 api.subscribe 加重载），这是「扩展 store 能力」的第二种手法

```javascript
// 简化版 vanilla.js createStore + 中间件签名
function createStore(createState) {
  let state
  const listeners = new Set()
  const setState = (partial, replace) => {
    const next = typeof partial === 'function' ? partial(state) : partial
    if (!Object.is(state, next)) {
      state = replace ? next : { ...state, ...next }
      listeners.forEach((l) => l(state))
    }
  }
  const getState = () => state
  const api = { setState, getState, subscribe: (l) => (listeners.add(l), () => listeners.delete(l)) }
  state = createState(setState, getState, api)
  return api
}

// logger 中间件：只包 set
const logger = (config) => (set, get, api) =>
  config((args) => { console.log('old', get()); set(args); console.log('new', get()) }, get, api)
```
