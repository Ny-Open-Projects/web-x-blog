---
title: [DP-056] xstate 这类状态机库的核心思想是什么？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-056：xstate 这类状态机库的核心思想是什么？（高频）
**答**：
- xstate 把状态模式工程化：状态（state）+ 事件（event）+ 转移（transition）+ 上下文（context 扩展数据）+ 副作用（action/service）。
- 核心价值：**非法状态不可达**（转移表外的事件直接拒绝）、状态可序列化、可可视化（状态图）、可测试（纯函数 transition）。
- 关键概念：层级状态、并行状态、guarded transitions（条件转移）、final state。
- 对比手写：业务复杂到手写转移表难维护时上库；简单二态按钮没必要。

```javascript
// 用 xstate 的思想手写一个 mini createMachine
function createMachine(config) {
  return {
    initial: config.initial,
    transition(state, event) {         // 纯函数：状态+事件 -> 下一状态
      const node = config.states[state];
      const t = node?.on?.[event.type];
      if (!t) return state;            // 非法事件：维持原状（不崩溃）
      const target = typeof t === 'string' ? t : t.target;
      const cond = typeof t === 'object' ? t.cond : undefined;
      if (cond && !cond(state.context, event)) return state; // 守卫不通过
      // 执行 actions（副作用）+ 合并 context
      const actions = typeof t === 'object' ? t.actions : undefined;
      let context = state.context;
      if (actions) context = actions.reduce((c, a) => config.actions[a](c, event), context);
      return { value: target, context };
    },
  };
}
const toggleMachine = createMachine({
  initial: 'idle',
  states: {
    idle: { on: { FETCH: { target: 'loading', actions: [] } } },
    loading: {
      on: {
        RESOLVE: { target: 'success', actions: ['assignData'] },
        REJECT: 'error',
      },
    },
    success: { final: true },
    error: { on: { RETRY: 'loading' } },
  },
  actions: {
    assignData: (context, event) => ({ ...context, data: event.data }),
  },
});
let state = { value: 'idle', context: { data: null } };
state = toggleMachine.transition(state, { type: 'FETCH' });
console.log(state.value);                       // loading
state = toggleMachine.transition(state, { type: 'RESOLVE', data: [1, 2] });
console.log(state.value, state.context.data);   // success [1, 2]
state = toggleMachine.transition(state, { type: 'FETCH' }); // success 是 final，事件被忽略
console.log(state.value);                       // success
```
