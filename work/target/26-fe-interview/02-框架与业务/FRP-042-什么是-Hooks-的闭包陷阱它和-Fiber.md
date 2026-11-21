---
title: [FRP-042] 什么是 Hooks 的闭包陷阱？它和 Fiber 有什么关系？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-042：什么是 Hooks 的闭包陷阱？它和 Fiber 有什么关系？

**答**：
- 函数组件每次渲染都是**一次新的函数调用**，本次的 state/props 是本次 render 的闭包快照——定时器、事件监听里拿到的往往是"注册那一刻"的旧值，这就是闭包陷阱。
- 与 Fiber 的关系：每个 Fiber 对应多次渲染，每次渲染有自己的一套 hook 值（链表节点被更新，但**函数执行时的局部变量已被闭包捕获**）；旧渲染的闭包不会因 state 更新而自动刷新。
- 解法一：`useRef` 存最新值（引用不变，内容可变）；解法二：setState 传函数 `setCount(n => n + 1)` 让 React 在 update 时基于最新值计算；解法三：依赖数组写全 + 清理函数。
- 在 Concurrent 下更要注意：被中断重放的 render 可能产生多个"平行快照"，依赖旧闭包的逻辑会更早暴露问题。

```jsx
// 一一对应：闭包陷阱复现与三种解法
import { useState, useEffect, useRef } from 'react';

export default function ClosureTrap() {
  const [count, setCount] = useState(0);

  // 陷阱：定时器闭包捕获的是首次渲染的 count（永远 0）
  useEffect(() => {
    const t = setInterval(() => {
      console.log('count is', count); // 一直是 0！
    }, 1000);
    return () => clearInterval(t);
  }, []); // 空依赖：effect 只注册一次，闭包定格在第一次渲染

  // 解法一：函数式更新，不依赖闭包里的 count
  useEffect(() => {
    const t = setInterval(() => {
      setCount((n) => n + 1); // n 由 React 基于 hook 队列最新值计算
    }, 1000);
    return () => clearInterval(t);
  }, []);

  // 解法二：useRef 保存最新值
  const countRef = useRef(count);
  useEffect(() => { countRef.current = count; });
  useEffect(() => {
    const t = setInterval(() => {
      console.log('latest count', countRef.current); // 总是最新
    }, 1000);
    return () => clearInterval(t);
  }, []);

  return <p>{count}</p>;
}
```
