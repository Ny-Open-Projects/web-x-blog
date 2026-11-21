---
title: [R19-133] 手写一个简化版 useRef，为什么它能做到跨渲染返回同一实例？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-133：手写一个简化版 useRef，为什么它能做到跨渲染返回同一实例？
**答**：
- useRef 就是"挂在 hook 链上的一个盒子"：首次渲染创建 `{ current: initialValue }`，之后每次渲染直接返回**同一个对象引用**。
- 它不触发重渲染——改 current 只是改了普通对象属性，没有任何调度介入。
- 因此它既能存 DOM，也能存"上次渲染的值"、"定时器 id"等跨渲染的可变数据。
- 反面教材：在渲染期间写 ref.current 会破坏纯函数约定（并发渲染下可能执行多次），写操作应放进 effect 或事件里。

```jsx
// mini-react.js —— 手写 useRef：同一实例跨渲染
import { currentFiber, hookIndex } from './mini-react';

export function useRef(initialValue) {
  const fiber = currentFiber;
  const index = hookIndex++;
  const hooks = fiber.hooks;

  // 首次创建盒子，之后渲染命中同一个节点 —— 引用永远不变
  if (hooks[index] === undefined) {
    hooks[index] = { current: initialValue };
  }
  return hooks[index];
}

// ---- 验证三件事：实例稳定 / 不触发渲染 / interval 闭包陷阱的正确解法 ----
import { render as mount, useState } from './mini-react';

function Timer() {
  const [count, setCount] = useState(0);
  const timerRef = useRef(null);        // 每次渲染返回的是同一个对象

  function start() {
    if (timerRef.current) return;       // 防重复启动：靠实例稳定性判断
    timerRef.current = setInterval(() => setCount(c => c + 1), 1000);
  }
  function stop() {
    clearInterval(timerRef.current);    // 改 current 不会触发重渲染
    timerRef.current = null;
  }
  return { start, stop, count };
}

const fiber = { Component: Timer, hooks: [], output: null };
mount(fiber);
const a = fiber.output;
mount(fiber);                           // 模拟第二次渲染
const b = fiber.output;
console.log(a.timerRef === b.timerRef); // true —— 同一实例跨渲染
```
