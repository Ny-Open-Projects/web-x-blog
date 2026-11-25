---
title: [ZSM-665] XState v5 的 actor 引用体系：parent/self/system 与 sendTo 的寻址
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-665：XState v5 的 actor 引用体系：parent/self/system 与 sendTo 的寻址

**答**：
- v5 的 actor 通信建立在**引用**上：每个 actor 内部可访问 `self`（自己）、`parent`（父 actor，子 actor 内）、`system`（全局注册表）。`createActor(machine, { systemId: 'cart' })` 注册到 system 后，任何 actor 都能 `system.get('cart')` 拿引用——跨层级通信不用层层透传 props。
- `sendTo(ref, event)` 是事件通信的标准形式：`sendTo(('actors', ...) => spawnRef, {...})` 或在 event 回调里 `raise`（发给自己）/`sendParent`（发给父机，子 actor 内）。引用安全：sendTo 只在 actor 存活时投递（mailbox），死 actor 的事件静默丢弃——比手写事件总线多一层生命周期保证。
- actor 输入（input）从哪来：`createActor(machine, { input })` 或父级 invoke 时 `input: ({ context }) => ...`——v5 强制 input 显式化（替代 v4 的闭包变量），同一 machine 可复现。
- snapshot 体系：`actor.getSnapshot()` 拿状态、`actor.subscribe(snap => ...)` 订阅——React 绑定层 `useActor(actor)` 就是 subscribe + getSnapshot 的封装，可以拿到任意 actor（不限于自己组件树的）。
- 追问钩子：systemId 的滥用风险——全局注册表是「服务定位器」，注册过多会变成隐式耦合；规范：父子直连用 sendTo/sendParent，跨子树才 system.get。

```javascript
import { setup, createActor, sendTo } from 'xstate'

// systemId 全局寻址
const cartMachine = setup({}).createMachine({
  id: 'cart',
  context: ({ input }) => ({ items: input.items ?? [] }),
  on: {
    ADD_ITEM: { actions: ({ context, event }) => ({ context: { items: [...context.items, event.item] } }) },
  },
})

const checkoutMachine = setup({}).createMachine({
  id: 'checkout',
  initial: 'idle',
  states: {
    idle: {
      on: {
        SYNC: {
          actions: sendTo('cart', { type: 'ADD_ITEM', item: { id: 'g1' } }),   // systemId 寻址
        },
      },
    },
  },
})

const actor = createActor(checkoutMachine, { systemId: 'checkout' })
const cartActor = createActor(cartMachine, { systemId: 'cart' })
actor.start({ system: [cartActor] })   // 注册进同一个 system
cartActor.start()
actor.send({ type: 'SYNC' })           // checkout → cart：引用通信

// 子 actor 内的寻址族
// fromCallback(({ sendBack, receive, self, parent, system }) => {...})
// sendParent({ type: 'PROGRESS', pct })   → 父机消费
```
