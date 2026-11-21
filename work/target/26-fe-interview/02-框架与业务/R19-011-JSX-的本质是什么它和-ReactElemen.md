---
title: [R19-011] JSX 的本质是什么？它和 ReactElement 的关系？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-011：JSX 的本质是什么？它和 ReactElement 的关系？
**答**：
- JSX 是 JavaScript 的语法扩展，本质是语法糖，编译后产出描述 UI 结构的普通 JS 对象（ReactElement）。
- 现代编译产物调用 `react/jsx-runtime` 的 jsx 函数，而不是旧的 React.createElement。
- ReactElement 只是"描述"，真正的 DOM 创建发生在渲染器（react-dom）的 commit 阶段。
- 因此 JSX 可以出现在变量、参数、返回值等任何 JS 表达式可用的位置。

```jsx
// 源码中的 JSX
const element = <h1 className="title">Hello</h1>;

// 编译后等价于（新 JSX transform）
import { jsx as _jsx } from 'react/jsx-runtime';
const compiled = _jsx('h1', { className: 'title', children: 'Hello' });

// element 和 compiled 都是普通对象：type、props、key 组成的描述
console.log(element.type, element.props.className);
```
