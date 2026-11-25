---
title: [ZSM-514] XState 的 context 扩展状态与 finite 状态如何配合
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-514：XState 的 context 扩展状态与 finite 状态如何配合

**答**：
- XState 把状态拆成两层：**有限状态**（states 树里的激活节点）负责「控制流」，**context**（可无限扩展的数据）负责「业务数据」。原则：能建模成有限状态的不要塞进 context。
- 判断标准：状态影响行为（决定能否响应某事件、走哪条迁移）→ 做成 state；只影响展示/数值（比如输入框文本、重试次数）→ 放 context。
- `assign` 是唯一修改 context 的途径，且只能在 action 里执行；transition 函数本身是纯的，可序列化、可离线重放——这是 XState 与普通 reducer 状态库最大的架构差异。
- context 里的复杂结构要配合 `guard`（守卫）使用：守卫读 context 判断，决定迁移走向。这层组合就是「有限状态 + 扩展状态」的完整表达。
- 追问钩子：v5 的 `input` 取代了旧版「在 createMachine 里读外部变量」，context 初始值必须从 `input` 派生，保证同一 machine 可复现。

```javascript
import { setup, createActor } from 'xstate'

const machine = setup({}).createMachine({
  context: ({ input }) => ({ retries: input.retries ?? 0, value: '' }), // 初始值从 input 派生
  initial: 'editing',
  states: {
    editing: {
      on: {
        INPUT: { actions: ({ context, event }) => ({ context: { ...context, value: event.value } }) },
        SUBMIT: {
          target: 'submitting',
          // 守卫读扩展状态决定控制流：value 为空拒绝迁移
          guard: ({ context }) => context.value.trim().length > 0,
        },
      },
    },
    submitting: {
      on: {
        FAIL: [
          // 迁移目标按 context.retries 分支：扩展状态影响控制流
          { target: 'editing', guard: ({ context }) => context.retries >= 2 },
          { target: 'submitting', actions: ({ context }) => ({ context: { retries: context.retries + 1 } }) },
        ],
        DONE: 'success',
      },
    },
    success: { type: 'final' },
  },
})

const actor = createActor(machine, { input: { retries: 0 } })
actor.start()
actor.send({ type: 'INPUT', value: 'hi' })
```
