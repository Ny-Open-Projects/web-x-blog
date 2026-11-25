---
title: [WCN-626] Signals 与框架自带的响应式（React setState / Vue ref）是什么关系，会取代它们吗？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-626：Signals 与框架自带的响应式（React setState / Vue ref）是什么关系，会取代它们吗？

**答**：
- 结论：Signals 是「细粒度的响应式原语」，与框架状态管理互补而非取代——框架管组件树与渲染调度，Signal 管依赖追踪与精准更新。
- 差异：setState 触发组件重渲染（粗粒度），Signal 只更新真正依赖它的 DOM 节点（细粒度，跳过 VDOM diff）；Vue ref 本质是 signal 的一种实现。
- 追问钩子：React 已内置 useSignal 提案，为何还要手写？考察对「标准落地前的工程过渡方案」与团队可控性的理解。

```javascript
// 一个最小 signal：读时收集依赖，写时通知订阅者
function signal(value) {
  const subs = new Set();
  return {
    get() { if (activeSub) subs.add(activeSub); return value; },
    set(v) { if (v === value) return; value = v; subs.forEach(f => f()); },
  };
}
let activeSub = null;
function effect(fn) { activeSub = fn; fn(); activeSub = null; }
const count = signal(0);
effect(() => console.log('count =', count.get())); // 订阅
count.set(1); // 只通知依赖它的 effect，不触发整棵组件树
```
