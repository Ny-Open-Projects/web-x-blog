---
title: [R19-071] 手写一个通用的 useEventListener？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-071：手写一个通用的 useEventListener？
**答**：
- 三层设计：target 支持 ref、DOM 节点或返回节点的函数；handler 用 useLatest 包一层，保证监听器里永远执行最新闭包而无需重建监听。
- 自动清理：effect 返回 removeEventListener，重复挂载/卸载不泄漏。
- 关键点：handler 不进依赖数组——否则每次渲染都重新 add/remove，性能差且可能丢事件。

```jsx
// useEventListener：自动清理 + ref 目标 + 最新回调
import { useEffect, useRef } from 'react';

export function useLatest(value) {
  const ref = useRef(value);
  ref.current = value;
  return ref;
}

export function useEventListener(target, event, handler, options) {
  const handlerRef = useLatest(handler);   // 永远拿到最新回调，无需写进依赖

  useEffect(() => {
    const el = typeof target === 'function' ? target() : (target?.current ?? target);
    if (!el?.addEventListener) return;
    const listener = (e) => handlerRef.current(e);
    el.addEventListener(event, listener, options);
    return () => el.removeEventListener(event, listener, options);
  }, [event, target, options, handlerRef]);
}

// 用法
function ScrollBox() {
  const boxRef = useRef(null);
  useEventListener(boxRef, 'scroll', e => console.log(e.target.scrollTop));
  useEventListener(() => window, 'resize', () => console.log(window.innerWidth));
  return <div ref={boxRef} style={{ height: 200, overflow: 'auto' }}>长内容</div>;
}
```
