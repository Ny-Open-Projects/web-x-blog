---
title: [WCN-069] TC39 Signals 提案现在到哪一步了？核心 API 与设计目标是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-069：TC39 Signals 提案现在到哪一步了？核心 API 与设计目标是什么？

**答**：
- 现状：由 Rob Eisenberg（Aurelia）、Daniel Ehrenberg 等推动，2024 年进入 Stage 1（探索），尚在 API 形态讨论中，未到 Stage 2；本文按 2026-11 视角判断其仍在推进。
- 目标：把"信号语义"标准化为语言原语——各框架（Vue/Solid/Preact/Aurelia 等）的 signal 实现共享同一底层，跨框架状态可互操作，减少每库自研的边角 bug。
- 核心 API 草案形态：`Signal.state(initial)`（可写信号）、`Signal.computed(fn)`（派生）、computed 与 effect 的依赖自动追踪、`untrack(fn)` 逃逸追踪、相等性可定制；effect 是否内置仍是争论点（副作用归属运行环境）。
- 设计原则：只有最小响应式核心，不含渲染/调度策略（留给上层框架）；同步一致性读（transaction 内读写一致）。
- 对前端的影响：跨框架 store（如微前端共享状态）可直接用原生 Signal；WC + 原生 Signals 成为完全无依赖组件模型。

```javascript
// 提案草案风格 API（示意）
import { Signal } from 'signals-proposal';

const a = Signal.state(1);
const b = Signal.computed(() => a.get() * 2);
console.log(b.get());        // 2
a.set(5);                    // 标脏
console.log(b.get());        // 10（读取时重算，push-pull）

Signal.subtle.untrack(() => Math.random()); // 不参与依赖收集
```
