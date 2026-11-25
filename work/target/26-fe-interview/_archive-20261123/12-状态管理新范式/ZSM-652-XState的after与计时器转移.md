---
title: [ZSM-652] XState 的 after / delayed transitions：超时与防抖在状态机里建模
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-652：XState 的 after / delayed transitions：超时与防抖在状态机里建模

**答**：
- `after: { 3000: 'timeoutState' }` 是延时转移：进入该状态时启动定时器，期间状态离开（收到其他事件迁移）定时器**自动清除**——不需要手写 setTimeout/clearTimeout，且不会泄漏。延时可动态：`after: { paymentTimeout: {...} }` 配 `delays: { paymentTimeout: ({ context }) => context.maxWait }`。
- 典型建模场景：1) 支付超时（进入 `awaitingPayment`，after 15min 到 `expired`）；2) 搜索防抖（输入事件迁移回自身并重启计时——「重入状态重置 after」，天然防抖）；3) 懒加载超时降级（after 500ms 仍 pending 就显示骨架）。
- 防抖建模精髓：`typing: { on: { INPUT: 'typing' }, after: { debounce: 'searching' } }`——INPUT 自迁移会**重置**该状态的 after 计时器，连续输入不触发 searching，停顿超 debounce 才触发。手写防抖逻辑全免。
- 与 setTimeout 的对比优势：定时器生命周期与状态绑定（离开即清）、可测试（transition 到状态即推进虚拟时间）、可观测（timeout 也是迁移，DevTools 可见）。
- 追问钩子：`after` 配 `guard` 可做「超时但有条件」——如会话空闲超时仅在「无编辑中草稿」时登出。

```javascript
import { setup, createActor } from 'xstate'

// 防抖搜索：typing 自迁移重置 after 计时
const searchMachine = setup({
  delays: { debounce: ({ context }) => context.debounceMs ?? 300 },
}).createMachine({
  context: { kw: '', debounceMs: 300, results: [] },
  initial: 'idle',
  states: {
    idle: { on: { INPUT: 'typing' } },
    typing: {
      on: {
        INPUT: {
          target: 'typing',                                   // 自迁移：重置 after
          actions: ({ context, event }) => ({ context: { ...context, kw: event.value } }),
        },
      },
      after: { debounce: 'searching' },                       // 停顿超时才搜索
    },
    searching: {
      invoke: {
        src: 'doSearch',
        input: ({ context }) => context.kw,
        onDone: { target: 'idle', actions: ({ context, event }) => ({ context: { results: event.output } }) },
      },
    },
  },
})

// 支付超时：动态延时
const payMachine = setup({
  delays: { paymentTimeout: ({ context }) => context.maxWait },
}).createMachine({
  context: { maxWait: 15 * 60 * 1000 },
  initial: 'awaitingPayment',
  states: {
    awaitingPayment: {
      on: { PAID: 'paid' },
      after: { paymentTimeout: { target: 'expired', guard: ({ context }) => !context.paid } },
    },
    paid: {},
    expired: {},
  },
})
```
