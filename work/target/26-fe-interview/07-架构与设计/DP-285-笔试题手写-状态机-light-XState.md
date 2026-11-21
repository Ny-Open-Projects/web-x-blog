---
title: [DP-285] 笔试题：手写状态机（light-XState）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-285：笔试题：手写状态机（light-XState）？
**题目**：实现 createMachine + interpret：1) 配置式状态图（states/on/guard/actions）；2) send 触发转移，非法事件保持原态；3) guard 条件转移；4) 订阅状态变化（subscribe）。
**评分点**：
- 转移查找正确（当前态的 on 表 + guard 求值）。
- 非法事件不转移（显式忽略并记录）。
- actions 在转移时按序执行并收集副作用。
- subscribe 返回解绑。
```javascript
function createMachine(config) {
  return { initial: config.initial,
    transition(state, event) {
      const node = config.states[state.value];
      for (const t of [].concat(node.on?.[event.type] ?? [])) {
        if (t.guard && !t.guard(state.context, event)) continue;      // 3) guard
        const ctx = { ...state.context };
        (t.actions ?? []).forEach(a => { const r = a(ctx, event); r && Object.assign(ctx, r); });  // 4)
        return { value: t.target ?? state.value, context: ctx };
      }
      return state;                                                    // 2) 非法事件维持
    } };
}
function interpret(machine) {
  let state = { value: machine.initial, context: config.context ?? {} };
  const subs = new Set();
  const service = {
    send(event) {
      const next = machine.transition(state, event);
      if (next !== state) { state = next; subs.forEach(s => s(state)); }
    },
    subscribe(fn) { subs.add(fn); fn(state); return () => subs.delete(fn); },
    get state() { return state; },
  };
  return service;
}
// 用：const toggle = createMachine({ initial: 'off', context: { count: 0 },
//   states: { off: { on: { TOGGLE: { target: 'on', actions: [c => ({ count: c.count + 1 })] } } },
//             on:  { on: { TOGGLE: 'off' } } } });
```
