---
title: [R19-126] React 与 Solid、Svelte 的概念级对比？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-126：React 与 Solid、Svelte 的概念级对比？
**答**：
- React：虚拟 DOM + 重渲染模型——状态变化重新执行组件函数，diff 后更新；"每次渲染都是快照"是所有闭包陷阱的根源。
- Solid：细粒度响应式，组件函数只执行一次，signal 直达 DOM，没有重渲染，自然没有 memo/useMemo。
- Svelte：编译时框架，构建期分析依赖生成命令式 DOM 操作，产物更小。
- 面试重点讲心智模型差异与更新粒度，而不是性能数字；React 的生态与"服务端组件"路线是其最大护城河。

```jsx
// React 与 Solid / Svelte 的概念级对比
// React：虚拟 DOM + 重渲染模型。状态变化 -> 重新执行组件函数 -> diff -> 更新
import { useState } from 'react';

function CounterReact() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}

// Solid：细粒度响应式。组件函数只执行一次，count 是信号，更新直达 DOM
// function CounterSolid() {
//   const [count, setCount] = createSignal(0);
//   return <button onClick={() => setCount(count() + 1)}>{count()}</button>;
// }

// Svelte：编译时框架。构建期分析依赖，产物是直接操作 DOM 的命令式代码

// 迁移启示：
// 1. React 的心智是"每次渲染都是快照"，闭包陷阱与旧值问题源于此
// 2. Solid/Svelte 没有重渲染，自然没有 memo/useMemo 这类补救 API
// 3. 对比重点是更新粒度与心智模型，而不是性能数字
```
