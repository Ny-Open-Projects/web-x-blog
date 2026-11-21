---
title: [FRP-029] 为什么 Hooks 不能写在条件语句或循环里？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-029：为什么 Hooks 不能写在条件语句或循环里？

**答**：
- Hook 的身份完全由**链表位置**决定（见上一题）：update 时 React 按顺序从链表头逐个取节点，它不知道也不检查你的代码逻辑。
- 一旦某次渲染条件分支少调了一个 hook，链表位置就会**错位**：后续 hook 读到的是前面 hook 的 state 与 queue，数据错乱甚至崩溃。
- React 的对策：每个 hook 节点带 `DebugName`/调试器检查，开发环境会在错位时报 "Rendered fewer hooks than expected"。
- 正确做法：把条件移进 hook 内部（`if (ready) useEffect(...)`）或拆组件，而不是条件化 hook 调用本身。

```javascript
// 一一对应：条件调用导致的链表错位（演示性代码）
// 简化实现，帮助理解
function badComponent({ enabled }) {
  // 第一次渲染 enabled=true，链表：[useState, useEffect, useState]
  // 第二次渲染 enabled=false，只调了两个 hook：
  //   useState 读取第 1 个节点 —— 正常
  //   useState 读取第 2 个节点 —— 其实是 useEffect 的节点！
  // 第二个 useState 的值变成了 effect 的 memoizedState（undefined）
  // 第三个 useState 从此永远读到错的数据
  const [a, setA] = useState(0);
  // if (enabled) useEffect(() => {...}, []); // 错误写法
  const [b, setB] = useState(0);
  return <div>{a}{b}</div>;
}

// 正确写法一：条件放进 hook 内部
function goodComponent({ enabled }) {
  useEffect(() => {
    if (enabled) { /* ... */ } // 条件在 effect 体内
  }, [enabled]);
  const [a, setA] = useState(0);
  const [b, setB] = useState(0);
  return <div>{a}{b}</div>;
}

// 正确写法二：条件部分拆成独立组件，各组件有自己的 hook 链
function bestComponent({ enabled }) {
  return enabled ? <EnabledPanel /> : <DisabledPanel />;
}
```
