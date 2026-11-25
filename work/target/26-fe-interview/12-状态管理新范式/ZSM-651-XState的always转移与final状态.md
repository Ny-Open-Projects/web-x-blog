---
title: [ZSM-651] XState 的 always 转移与 final 状态：无事件迁移怎么用对
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-651：XState 的 always 转移与 final 状态：无事件迁移怎么用对

**答**：
- `always` 是**无事件转移**：进入状态时立即评估（在 entry 动作之后），守卫通过就迁移——适合「进入状态后根据 context 立即分派」的场景（如 `reviewing` 进入时若 `alreadyApproved` 直接到 `done`），避免「进状态→自己发事件→再迁移」的迂回。
- 执行顺序：`entry actions → always（按数组顺序评估，首个守卫通过的生效）→ （此后等待事件）`。always 里再 set context 会与 entry 的 assign 组合成两次微任务内的 context 更新，最终一致。
- `type: 'final'` 状态：标记子机完成，触发父级的 `onDone` 事件（携带子机 context 输出 `output`）——嵌套流程的「子流程完成」语义；顶层 final 的 actor 直接到 done。与 `done` 事件区分：`onDone` 是结构化的（只由 final 状态触发），普通自定义事件 `DONE` 要自己 send。
- 常见误用：用 always 做「轮询判断」——always 只在进入时评估一次，context 后续变化不会自动重跑；需要响应变化的分支应该用事件转移或 `after` 延迟重评估。
- 追问钩子：always + guard 组合就是「在进入状态时做一次 context 驱动的路由」，等价于构造函数里决定初始状态——比在 machine 外部判断初始状态更内聚。

```javascript
import { setup, createActor } from 'xstate'

const machine = setup({}).createMachine({
  context: ({ input }) => ({ approved: input.approved ?? false, score: 0 }),
  initial: 'reviewing',
  states: {
    reviewing: {
      entry: ({ context }) => ({ context: { score: computeScore(context) } }),
      // 进入即分派：审批已通过且分数达标直接完成，否则等待事件
      always: [
        { guard: ({ context }) => context.approved && context.score >= 60, target: 'done' },
        { guard: ({ context }) => context.score < 30, target: 'rejected' },
        { target: 'waiting' },   // 兜底：无守卫命中则到 waiting
      ],
    },
    waiting: {
      on: { APPROVE: 'done', REJECT: 'rejected' },
    },
    rejected: {},
    done: { type: 'final', output: ({ context }) => ({ score: context.score }) },   // final：父级 onDone
  },
  output: ({ event }) => ({ result: event.output }),
})

function computeScore(c) { return 72 }
const actor = createActor(machine, { input: { approved: true } })
actor.start()
actor.subscribe((s) => console.log(s.value))
// approved=true 且 score=72 → 进入 reviewing 后 always 直接到 done（无事件迁移）
```
