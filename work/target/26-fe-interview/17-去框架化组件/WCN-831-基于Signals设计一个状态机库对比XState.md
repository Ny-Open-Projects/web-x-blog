---
title: [WCN-831] 基于 Signals 设计一个状态机库，对比 XState 有什么取舍？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-831：基于 Signals 设计一个状态机库，对比 XState 有什么取舍？

**答**：
- 结论先行：Signals 做状态机的优势是「状态即 signal、派生即 computed」，天然细粒度、易与框架集成；缺的是 XState 的可视化、层级状态机、形式化验证等重型能力——适合中小型、状态不太深的场景。
- 核心设计：用 `signal` 存当前状态与上下文（context），用 `computed` 派生「某事件在当前状态是否可用」，用 `effect` 在进入某状态时触发副作用；`send(event)` 是唯一的状态变更入口，内部做转移表查找与守卫判断。
- 转移约束：定义转移表 `{ state: { EVENT: nextState } }`，`send` 时查表，非法转移拒绝（可抛错或忽略），保证状态机「不能乱跳」。
- 对比 XState：XState 强在层级/并行状态、可视化、actor 模型、严格的进入/退出动作；Signals 版轻量、无依赖、与响应式 UI 无缝，但复杂状态机要自己实现层级与可视化。
- 追问钩子：面试官会问「守卫（guard）怎么实现」——答：守卫是读 context signal 的纯函数，`send` 时先算 guard，通过才转移；因为 guard 用了 signal，context 变化也会让「可用事件」的 computed 自动更新。

```javascript
import { signal, computed } from '@preact/signals-core';

function createMachine({ initial, context, transitions, guards = {}, actions = {} }) {
  const state = signal(initial);
  const ctx = signal({ ...context });
  const can = (event) => !!transitions[state.value]?.[event];
  function send(event, payload) {
    const t = transitions[state.value]?.[event];
    if (!t) return false;                              // 非法转移拒绝
    const guard = guards[t.guard];
    if (guard && !guard(ctx.value, payload)) return false;
    const prev = state.value;
    state.value = t.to;                                // 转移
    actions[t.action]?.(ctx.value, payload);           // 副作用
    return true;
  }
  return { state, ctx, send, can };
}
const machine = createMachine({
  initial: 'idle',
  context: { retries: 0 },
  transitions: { idle: { FETCH: { to: 'loading' } },
                 loading: { OK: { to: 'success' }, FAIL: { to: 'idle', guard: 'canRetry', action: 'inc' } } },
  guards: { canRetry: c => c.retries < 3 },
  actions: { inc: c => c.retries++ },
});
machine.send('FETCH'); machine.send('FAIL');
```
