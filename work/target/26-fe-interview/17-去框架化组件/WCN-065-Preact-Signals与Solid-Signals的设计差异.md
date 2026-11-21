---
title: [WCN-065] Preact Signals 与 Solid signals 的设计差异是什么？（value 访问、集成方式、性能取舍）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-065：Preact Signals 与 Solid signals 的设计差异是什么？（value 访问、集成方式、性能取舍）

**答**：
- 访问语义：Solid 的 signal 是函数调用 `count()`（显式读取边界，编译器可静态识别）；Preact/Vue 风格是 `.value`（getter 拦截，可在任意代码里动态追踪）。
- 与渲染的关系：Solid 编译期把 JSX 表达式包成"读取即追踪"的单元，组件函数只跑一次，粒度精确到表达式；Preact Signals 是可选层——组件正常 VDOM 渲染，但 signal 在 diff 中按引用相等短路，未变的子树整棵跳过。
- 细粒度策略：Solid 靠编译器做到"表达式级"；Preact 靠"signal 驻留在 VDOM 属性中 + 相等性短路"做到"子树级"。
- 跨框架能力：Preact 的 `@preact/signals-core` 是独立实现，React/Vue/Svelte 适配包共享同一语义，适合 WC/微前端共享 store；Solid signals 与其编译器深度耦合，跨端要靠 solid-js 独立运行。
- 内存与安全：Solid 组件只跑一次意味着 effect 生命周期与组件销毁绑定；Preact 的 signal effect 需要手动管理或靠 React 集成层的 useEffect 生命周期。

```javascript
// Solid：函数调用 + 组件只跑一次
import { createSignal, createEffect } from 'solid-js';
const [count, setCount] = createSignal(0);
createEffect(() => console.log('solid:', count())); // 依赖=函数体内读取

// Preact：.value + 渲染短路
import { signal } from '@preact/signals-core';
const s = signal(0);
s.value = 0;               // 相等 → 不触发任何订阅者（Object.is 短路）
```
