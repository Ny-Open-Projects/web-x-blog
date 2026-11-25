---
title: [ZSM-516] Zustand 的 devtools 中间件是怎么与 Redux DevTools 协议对接的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-516：Zustand 的 devtools 中间件是怎么与 Redux DevTools 协议对接的

**答**：
- Redux DevTools 扩展暴露的是 window 级 `__REDUX_DEVTOOLS_EXTENSION__` 全局对象，其 `connect` 给出一个带 `send(action, state)` 的实例。Zustand devtools 中间件就是包装 `setState`：每次变更把 `{ type, payload }` 通过 `connection.send` 推给扩展，扩展按时间线展示。
- `type` 默认是匿名（anonymous），可传第二参 `replace || 'setState'` 或对象 `{ type: 'cart/addItem', payload }` 命名 action——命名是 DevTools 时间线可读性的关键。
- 双向能力：`connection.subscribe` 接收 DevTools 面板里点「time travel / dispatch」的消息，中间件调用原生 `setState` 把历史状态写回 store，实现时间旅行回放。
- `partialize` 与 DevTools 结合可只暴露关心的切片，避免大状态撑爆扩展的 JSON 传输；`trace` 选项开启后记录 action 触发时的调用栈，定位「谁改了状态」。
- 追问钩子：SSR/无 window 环境中间件要降级为直通（不包装），否则 window undefined 报错——中间件内部有 `typeof window === 'undefined'` 分支。

```javascript
// 简化的 devtools 中间件
function devtoolsImpl(fn, options = {}) {
  return (set, get, api) => {
    const ext = typeof window !== 'undefined' && window.__REDUX_DEVTOOLS_EXTENSION__
    if (!ext) return fn(set, get, api)          // 无扩展直通

    const connection = ext.connect({ name: options.name })
    // 时间旅行：面板 dispatch 把历史状态写回
    connection.subscribe((msg) => {
      if (msg.type === 'DISPATCH' && msg.state) {
        set(JSON.parse(msg.state), true)        // replace 模式整体替换
      }
    })

    api.setState = (state, replace, typeOrAction, ...rest) => {
      set(state, replace, ...rest)
      const type = typeof typeOrAction === 'string' ? typeOrAction : typeOrAction?.type ?? 'setState'
      const payload = typeof typeOrAction === 'object' ? typeOrAction.payload : undefined
      connection.send({ type, payload }, get())  // 推给 DevTools 时间线
    }
    return fn(api.setState, get, api)
  }
}

// 用法：命名 action
const useCart = create(devtools((set) => ({
  items: [],
  add: (item) => set((s) => ({ items: [...s.items, item] }), false, {
    type: 'cart/addItem', payload: item.id,
  }),
}), { name: 'CartStore', trace: true }))
```
