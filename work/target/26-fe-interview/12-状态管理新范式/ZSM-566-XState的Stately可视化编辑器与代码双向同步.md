---
title: [ZSM-566] XState 的 Stately 可视化编辑器与代码双向同步是怎么回事
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-566：XState 的 Stately 可视化编辑器与代码双向同步是怎么回事

**答**：
- Stately（stately.ai）把状态机定义（JSON/TS）渲染成可交互的状态图：圆角矩形是状态、箭头是事件迁移、守护条件标在箭头上；可以在图上**直接拖拽/连线编辑**，编辑器产出等价的 machine 定义代码。
- 双向同步的关键前提：machine 定义是**声明式纯数据**（states/on/guard 的结构化描述），与图形同构——这和「代码即图」的抽象语法树思路一致。运行时如果 machine 里混入了副作用（inline async 函数），双向就会退化成单向（图只读）。
- 调试视角：Stately 的 inspector 能在运行时实时高亮当前激活状态、显示事件流历史、逐事件单步发送——配合 v5 的 `inspect` 参数把运行实例接到面板，得到「理论图 + 实际轨迹」的对照，这是状态机方案相对散装布尔标志最大的可观测性优势。
- 工程价值：产品/测试能看懂状态图，直接评审「这个退款流程漏了超时迁移吗」——状态机让业务规则可视化评审成为可能。
- 追问钩子：可视化只覆盖拓扑结构，guard/assign 里的逻辑仍在代码里——「图管流程、代码管逻辑」的分层是维护边界。

```javascript
import { setup, createActor, inspect } from '@xstate/inspect'

const machine = setup({
  guards: {
    canRefund: ({ context }) => context.paid && Date.now() - context.paidAt < 7 * 864e5,
  },
}).createMachine({
  id: 'order',          // ← 图上节点 id
  initial: 'created',
  context: { paidAt: 0, paid: false },
  states: {             // ← 图上圆角矩形
    created: { on: { PAY: 'paid' } },              // ← 图上箭头 PAY
    paid: {
      entry: ({ context }) => { context.paidAt = Date.now() },
      on: {
        REFUND: [{ guard: 'canRefund', target: 'refunded' }, { target: 'paid' }],  // 箭头+守卫
        SHIP: 'shipped',
      },
    },
    shipped: {},
    refunded: { type: 'final' },
  },
})

// 开发环境接入 inspector：实时高亮激活状态 + 事件历史
if (import.meta.env.DEV) {
  const actor = createActor(machine, { inspect: inspect(window) })  // devtools 面板
  actor.subscribe((s) => console.log(s.value))
  actor.start()
}
```
