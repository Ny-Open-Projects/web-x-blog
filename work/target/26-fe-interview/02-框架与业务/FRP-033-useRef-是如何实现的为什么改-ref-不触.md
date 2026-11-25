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

**追问**：

1. 为什么不能在 render 期间读写 ref 来"传值"？→ render 可能被丢弃或重复执行（StrictMode 会双调），写 ref 属于副作用，而且本次读到的还是上一次渲染留下的值；读写都放到事件或 effect 里。
2. `useRef` 和 `useMemo` 存实例有什么区别？→ `useMemo` 只是缓存提示，内存压力下 React 可以丢弃重算；`useRef` 保证同一对象存活到卸载，存定时器 ID、图表实例、WebSocket 必须用它。
3. 既想改 ref 又想更新视图怎么办？→ 别给 ref 加订阅，那不叫 ref 了；用 `useCallback` 包一层 setState 触发器，或者直接换成 useState / useSyncExternalStore。
