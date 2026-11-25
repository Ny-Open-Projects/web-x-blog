---
title: [ZSM-674] XState 与 React 的接线细节：useActor 生命周期与 actor 归属
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-674：XState 与 React 的接线细节：useActor 生命周期与 actor 归属

**答**：
- React 绑定的三种 actor 归属：1) **组件私有 actor**——`useActor(machine, { input })`（内部 createActor + useEffect start/stop），卸载即 stop，资源干净（表单向导、抽屉流程）；2) **全局单例 actor**——模块级 `createActor().start()` + `useActor(actorRef)` 引用（购物车、会话），组件卸载不销毁；3) **Context 共享 actor**——Provider 里创建，子树 `useActorRef` 拿引用。
- useActor 的生命周期语义：返回 `[snapshot, send]`，snapshot 是渲染快照（引用稳定，state 对象不变不重渲）；StrictMode 下双挂载——组件私有 actor 会 start→stop→start，机内副作用（invoke）必须幂等可中止。
- 常见错误：1) 每次 render 调 `createActor`（actor 泄漏）——要用 useActor 或 useMemo+useEffect；2) send 后立即读 `actor.getSnapshot()`（迁移同步完成，但 React 渲染是异步的——读到的值对，UI 还是旧的）；3) 组件卸载后 send（死 actor 静默丢弃，不报错但逻辑丢失）——清理态要靠 stop 钩子或卸载前 finalize。
- stateMatches 模式：`snapshot.matches('loading')` 的渲染分支是状态机的核心消费形态——`if (snapshot.matches({ a: 'b' }))` 支持嵌套/并行匹配。
- 追问钩子：XState 的 value 比较（matches）与 context 比较（eq）分别用什么——value 是结构匹配，context 要自己写等值函数；把「渲染依赖的 context」选出来用 `useSelector(actor, selector)` 才能控制重渲粒度。

```javascript
import { useActor, useSelector } from '@xstate/react'
import { useActorRef } from '@xstate/react'

// 1) 组件私有 actor：卸载即 stop
function Drawer() {
  const [snapshot, send] = useActor(drawerMachine, { input: { mode: 'edit' } })
  useEffect(() => () => { /* stop 已由库处理 */ }, [])
  if (snapshot.matches('closed')) return null
  if (snapshot.matches({ open: 'editing' })) return <Editor />
}

// 2) 全局单例 + 粒度订阅
const cartActor = createActor(cartMachine).start()   // 模块级

function CartCount() {
  // useSelector 控制重渲粒度：只订阅 count
  const count = useSelector(cartActor, (s) => s.context.items.length)
  return <Badge count={count} />
}

function CartView() {
  const snapshot = useActor(cartActor)   // 全量订阅
  return snapshot.matches('empty') ? <Empty /> : <List items={snapshot.context.items} />
}

// 3) 错误示范
function Bad() {
  const actor = createActor(machine)   // ✗ 每次 render 新建 actor
  return null
}
```
