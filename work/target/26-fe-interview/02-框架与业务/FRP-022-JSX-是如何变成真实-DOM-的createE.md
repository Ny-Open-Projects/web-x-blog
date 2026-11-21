---
title: [FRP-022] JSX 是如何变成真实 DOM 的？createElement 与 jsx-runtime 有何区别？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-022：JSX 是如何变成真实 DOM 的？createElement 与 jsx-runtime 有何区别？

**答**：
- JSX 本身不是 JS，Babel/SWC 在编译期把它转成函数调用：旧转换是 `React.createElement(...)`（需手动 import React），React 17+ 新转换是 `react/jsx-runtime` 的 `jsx(...)`（自动引入，无需 import）。
- createElement 返回的是一个**普通对象（React element）**：`{ $$typeof, type, props, key, ref }`，不是 DOM，也不是 Fiber。
- jsx-runtime 的差别只是 API 形状：children 与 key 从 props 中拆出为独立参数、内部处理 `__source`/`__self`（调试信息），本质产物相同。
- 渲染链条：JSX → element 对象 → （render 时）Fiber 节点 → commit 阶段操作真实 DOM。

```jsx
// 一一对应：JSX 源码与其编译产物对照
// —— 源码 ——
// <div className="box" key="k1">
//   <h1>标题</h1>
//   <p>{count}</p>
// </div>

// —— React 16 及以前：Classic 转换，需要 import React ——
import React from 'react';

const el1 = React.createElement(
  'div',
  { className: 'box', key: 'k1' },
  React.createElement('h1', null, '标题'),
  React.createElement('p', null, count)
);

// —— React 17+：Automatic 转换，编译器自动引入 jsx-runtime ——
import { jsx as _jsx } from 'react/jsx-runtime';

const el2 = _jsx(
  'div',
  { className: 'box', children: [_jsx('h1', { children: '标题' }), _jsx('p', { children: count })] },
  'k1' // key 作为第三参独立传入
);

// 产物是一个普通 element 对象（可 console.log 验证）
console.log(el1.type);        // 'div'
console.log(el1.$$typeof);    // Symbol(react.element)：element 的类型标识
console.log(el1.props.children); // 子 element 数组
```
