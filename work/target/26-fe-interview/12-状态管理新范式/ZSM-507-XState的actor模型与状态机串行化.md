---
title: [ZSM-507] XState 的 actor 模型是怎么与状态机结合的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-507：XState 的 actor 模型是怎么与状态机结合的

**答**：
- XState v5 全面转向 actor 模型：每个 `createActor(machine)` 的实例就是一个 actor，拥有独立 mailbox——事件进队列、按序处理，天然解决并发事件乱序。
- 状态机决定 actor 的行为：transition 是纯函数 `(state, event) => nextState`，处理完一个事件才取下一个，mailbox 串行消费，杜绝「处理中又收到新事件」的竞态。
- actor 可以 spawn 子 actor（`fromPromise` / `fromCallback` / 嵌套 machine），父子间用 `sendTo` 通信；父 machine 在状态配置里声明 `invoke`，进入状态时拉起子 actor、退出时自动 stop——生命周期与状态绑定是它相对手写 reducer 的核心价值。
- `fromPromise` actor 结束时自动发完成的 done 事件给父状态机，把「异步完成」建模成一次状态迁移，不用在组件里 await。
- 追问钩子：v4 的 `interpret` 变成 v5 的 `createActor`，`send` 变成带 mailbox 语义的 `sendTo`，旧版「先发后启丢事件」问题在 v5 被 mailbox 修掉了。

```javascript
import { setup, createActor, fromPromise } from 'xstate'

const machine = setup({
  actors: {
    fetchUser: fromPromise(async ({ input }) => {
      const res = await fetch(`/api/users/${input.id}`)
      return res.json()
    }),
  },
}).createMachine({
  id: 'user',
  initial: 'idle',
  context: { userId: 1, user: null },
  states: {
    idle: { on: { LOAD: 'loading' } },
    loading: {
      invoke: {
        src: 'fetchUser',                  // 进入 loading 自动拉起 actor
        input: ({ context }) => ({ id: context.userId }),
        onDone: { target: 'ready', actions: ({ event }) => ({ context: { user: event.output } }) },
        onError: 'error',
      },
    },
    ready: {},
    error: { on: { RETRY: 'loading' } },   // 退出 loading 时子 actor 自动 stop
  },
})

const actor = createActor(machine)
actor.subscribe((s) => console.log(s.value))
actor.start()
actor.send({ type: 'LOAD' })   // 进入 mailbox，loading 状态拉起 fetchUser actor
```
