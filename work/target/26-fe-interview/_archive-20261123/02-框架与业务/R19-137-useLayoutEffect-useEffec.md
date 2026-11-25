---
title: [R19-137] useLayoutEffect、useEffect 与 useInsertionEffect 的执行时机差别是什么？如何演示？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-137：useLayoutEffect、useEffect 与 useInsertionEffect 的执行时机差别是什么？如何演示？
**答**：
- 执行顺序固定：`useInsertionEffect`（DOM 变更前，css-in-js 注入样式用）→ `useLayoutEffect`（DOM 变更后、**paint 前**，同步执行，可测量布局）→ paint → `useEffect`（**paint 后**异步，不阻塞绘制）。
- useLayoutEffect 里读 getBoundingClientRect 再改样式，用户看不到中间态；改用 useEffect 则可能闪烁。
- useInsertionEffect 不能读 DOM，专为样式表注入设计，普通业务代码不该用。
- 演示方式：三个 hook 各打一行 log，配合一次强制 reflow，观察顺序。

```jsx
// TimingDemo.jsx —— 三种 effect 的执行时机演示
import { useEffect, useLayoutEffect, useInsertionEffect, useRef, useState } from 'react';

export function TimingDemo() {
  const [n, setN] = useState(0);
  const boxRef = useRef(null);

  useInsertionEffect(() => {
    // 1st：DOM 变更前。css-in-js 库在此动态插入 <style>
    console.log('1 useInsertionEffect —— 不能读 DOM');
  }, [n]);

  useLayoutEffect(() => {
    // 2nd：DOM 已更新、浏览器还没画。适合测量并同步改布局
    const rect = boxRef.current.getBoundingClientRect();
    console.log('2 useLayoutEffect —— paint 前同步执行, width =', rect.width);
    // 修改样式在这里不会产生"闪烁"，因为用户还没看到这一帧
  }, [n]);

  useEffect(() => {
    // 3rd：paint 之后异步执行。数据请求、订阅、日志都在这里
    console.log('3 useEffect —— paint 后异步执行');
  }, [n]);

  return (
    <div ref={boxRef} style={{ width: 100 + n * 10, height: 40, background: '#eee' }}>
      <button onClick={() => setN(v => v + 1)}>resize</button>
    </div>
  );
}
// 点击后控制台顺序恒为：1 useInsertionEffect -> 2 useLayoutEffect -> 3 useEffect
// SSR 场景注意：useLayoutEffect 在服务端不执行并会告警，
// "首屏就要测量"的需求应改用 useEffect + 一次 setState 触发的重渲染。
```

## 第二十章 并发模式实战（R19-138 ~ R19-143）
