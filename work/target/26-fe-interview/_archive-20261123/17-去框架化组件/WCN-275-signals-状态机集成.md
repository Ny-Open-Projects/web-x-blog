---
title: [WCN-275] Signals 与状态机（XState 风格）集成的模式？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-275：Signals 与状态机（XState 风格）集成的模式？
**答**：
- 状态机是「写侧治理」：事件 → reducer → 新状态；signals 是「读侧分发」——互补。
- 模式：机器状态存 signal，transition 内 batch 写多个信号（状态+上下文原子更新）。
- 派生：computed 从状态派生 UI 视图（loading/blocked）。
- 反模式：在 effect 里发事件（信号变更触发机器转换）易形成环路——事件只来自用户/网络。

```javascript
const state = signal('idle');
const context = signal({ retries: 0 });
function send(event) {
  batch(() => {
    const [next, ctx] = reduce(state.value, context.value, event);
    state.value = next; context.value = ctx;   // 原子 transition
  });
}
const busy = computed(() => state.value === 'loading');   // 读侧派生
r
```
