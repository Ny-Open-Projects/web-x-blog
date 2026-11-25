---
title: [ZSM-247] Signals 为什么可能成为跨框架状态标准
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-247：Signals 为什么可能成为跨框架状态标准

**答**：
- Signals 是「值 + 依赖追踪 + 订阅」的一等公民抽象：读时收集依赖、写时精准通知，天然框架无关，Preact/Solid/Qwik/Angular/Svelte runes 各自实现、API 趋同
- 与 React 模型的根本差异：Signal 更新不重跑组件函数，直接精准更新绑定处；React 是重渲染 + 协调模型，所以 React 官方目前没跟进 Signal
- 跨框架价值：同一份 Signal 核心库（如 @preact/signals-core）在多框架绑包下发，微前端/多栈团队可共享状态层
- 局限：与 React 并发模型（tearing/useSyncExternalStore）的适配靠桥接实现，Signal 直连 React 仍需包装；生态成熟度不及主流状态库

```javascript
import { signal, computed, effect } from '@preact/signals-core'
const count = signal(0)
const double = computed(() => count.value * 2)   // 依赖追踪
effect(() => console.log(double.value))          // count 变 → 只通知 effect
count.value = 1
```
