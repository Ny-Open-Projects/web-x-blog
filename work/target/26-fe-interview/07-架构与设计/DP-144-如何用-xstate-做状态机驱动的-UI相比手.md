---
title: [DP-144] 如何用 xstate 做状态机驱动的 UI？相比手写状态字段好在哪？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-144：如何用 xstate 做状态机驱动的 UI？相比手写状态字段好在哪？（高频）
**答**：
- xstate 三要素：states（状态节点）、events（事件）、transitions（转移），声明式定义后 UI 完全由 `state.value` 驱动渲染——非法状态（loading 且 error 同时为真）从模型上不可能出现。
- 相比手写布尔标志（isLoading/isError/isEmpty 组合爆炸），状态机把"合法组合"收敛进结构，配合可视化（stately）可直接给产品看流程。
- 实战要点：context 放数据、states 放形态、`invoke` 声明异步服务（成功/失败自动转移）。

```jsx
import { createMachine, assign } from 'xstate';
import { useMachine } from '@xstate/react';
// 状态机：登录表单（状态驱动 UI 的标准范式）
const loginMachine = createMachine({
  id: 'login',
  initial: 'idle',
  context: { form: { user: '', pwd: '' }, error: null },
  states: {
    idle: { on: { SUBMIT: 'submitting', INPUT: { actions: 'saveForm' } } },
    submitting: {
      invoke: {                                               // 异步服务内置成功/失败转移
        src: (ctx) => api.login(ctx.form),
        onDone: 'success',
        onError: { target: 'idle', actions: assign({ error: (_, e) => e.data.message }) },
      },
    },
    success: { type: 'final' },
  },
}, { actions: { saveForm: assign({ form: (_, e) => e.value, error: null }) } });
function LoginPage() {
  const [state, send] = useMachine(loginMachine);
  // UI 完全由状态值驱动：三态互斥由机器保证
  return (
    <form onSubmit={(e) => { e.preventDefault(); send({ type: 'SUBMIT' }); }}>
      <input onChange={(e) => send({ type: 'INPUT', value: { ...state.context.form, user: e.target.value } })} />
      <button disabled={state.matches('submitting')}>登录</button>
      {state.context.error && <p role="alert">{state.context.error}</p>}
      {state.matches('success') && <p>欢迎回来</p>}
    </form>
  );
}
```
