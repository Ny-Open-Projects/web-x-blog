---
title: [FRP-033] useRef 是如何实现的？为什么改 ref 不触发重渲染？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-033：useRef 是如何实现的？为什么改 ref 不触发重渲染？

**答**：
- 实现：mount 时创建 `{ current: initialValue }` 对象存进 hook 节点的 memoizedState；update 时**直接返回同一个对象**——跨渲染的稳定性来自 Fiber 节点本身长存。
- 修改 `ref.current` 只是普通对象属性赋值，**不触发任何更新调度**，所以不重渲；这正是它"跨渲染存值但不驱动视图"的定位。
- 挂到 DOM 的 ref（`ref={inputRef}`）在 commit 阶段由 React 写入 `current`（ref attach/detach 在 mutation/layout 子阶段）。
- 与 useState 的对比：state 是"改了要重渲的值"，ref 是"改了不想重渲的值"（定时器 ID、上一次值、DOM 引用、可变标志位）。

```javascript
// 简化实现，帮助理解 useRef
function useRef(initialValue) {
  const hook = workInProgressHook;
  if (isMount) {
    // mount：创建一个可变对象存进 hook 节点
    hook.memoizedState = { current: initialValue };
  }
  // update：hook 节点还是同一个（链表位置没变），memoizedState 还是同一个对象
  return hook.memoizedState; // 引用跨渲染稳定，改 current 不触发 render
}

// 一一对应：三个典型用法
import { useRef, useState, useEffect } from 'react';

function Demo() {
  const inputRef = useRef(null);       // 1. DOM 引用
  const timerRef = useRef(null);       // 2. 存定时器，不因它重渲
  const prevRef = useRef(0);           // 3. 保存上一次渲染的值

  const [count, setCount] = useState(0);

  useEffect(() => {
    prevRef.current = count;           // 每次渲染后记录，下轮可读
  });

  useEffect(() => {
    timerRef.current = setInterval(() => setCount((n) => n + 1), 1000);
    return () => clearInterval(timerRef.current); // 卸载时清理
  }, []);

  return (
    <>
      <input ref={inputRef} />
      <p>上一次 {prevRef.current}，当前 {count}</p>
      <button onClick={() => inputRef.current.focus()}>聚焦</button>
    </>
  );
}
```
