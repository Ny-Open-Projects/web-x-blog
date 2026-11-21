---
title: [DP-245] 源码识别：XState 源码中的状态模式范式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-245：源码识别：XState 源码中的状态模式范式？
**答**:
- 状态模式（教科书级）：配置即状态图（states/initial/on），send(event) 是唯一转移入口；每个状态节点决定"收到某事件走哪个转移、执行哪些动作"。
- 命令+守卫：transition(event, context) → { state, actions }，guard 条件转移；actions 是副作用命令（脱离纯转移）。
- 观察者：actor.subscribe(state => ...) 订阅状态流；invoke 是嵌套 actor（组合模式——子状态机作为服务）。
- 识别要点：能对比"手写 if-else 状态" vs XState——配置化状态图让非法转移不可能发生（send('play') 在 idle 态被显式定义或忽略）。

```javascript
// XState 源码级简化
function createMachine(config) {
  return { config, transition(state, event) {
    const node = config.states[state.value];
    for (const [evt, t] of Object.entries(node.on ?? {})) {
      if (evt !== event.type) continue;
      if (t.guard && !t.guard(state.context, event)) continue;   // 守卫
      const actions = (t.actions ?? []).map(a => a(state.context, event));   // 命令执行
      const nextValue = typeof t.target === 'string' ? t.target : state.value;
      return { value: nextValue, context: { ...state.context, ...assignReduce(actions) } };
    }
    return state;                                                // 未定义事件：维持（非法转移被吞）
  } };
}
const actor = interpret(machine).start();          // 观察者
actor.subscribe(s => render(s.value, s.context));
actor.send({ type: 'EDIT' });
// invoke：invoke: { src: 'fetchUser', onDone: 'ready' } —— 子 actor 组合，完成事件驱动父转移
```
