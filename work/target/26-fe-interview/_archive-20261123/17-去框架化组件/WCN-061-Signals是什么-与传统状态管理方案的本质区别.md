---
title: [WCN-061] Signals 是什么？与 Redux/Zustand 这类状态管理库的本质区别是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Signals]
type: 面试题
---

## WCN-061：Signals 是什么？与 Redux/Zustand 这类状态管理库的本质区别是什么？

**答**：
- Signals 是"细粒度响应式原语"：一个 signal 是可读写的值单元，读取时自动建立依赖、写入时通知订阅者；`computed` 派生值惰性求值，`effect` 是有副作用的订阅。
- 本质区别：状态管理库（Redux/Zustand）只解决"状态放哪、怎么改"，更新视图仍靠框架重渲染 + diff；Signals 让"哪个 DOM 节点绑定哪个值"也明确了，更新是精确直改，无 diff。
- 两层关系：Signals 可以当 store 用（模块级单例），也可以下沉为渲染引擎的更新单位（Solid/Vue Vapor/Qwik 内核）。
- 关键特性：依赖追踪是运行时动态的（读了才算依赖）；自动批处理；computed 惰性 + 脏标记（只在被读时重算）；无渲染函数概念也可工作（裸 DOM/WC 直接用）。
- 追问钩子：Preact Signals、Solid signals、Vue ref、Qwik store、TC39 提案语义相近但 API/边角不同（比较题后续展开）。

```javascript
import { signal, computed, effect } from '@preact/signals-core';

const count = signal(1);
const double = computed(() => count.value * 2);

// 细粒度：只更新绑定 double 的文本节点
const el = document.querySelector('#d');
effect(() => { el.textContent = String(double.value); });

count.value = 5;          // el 立即变为 "10"，无任何重渲染
console.log(double.value); // 10
```
