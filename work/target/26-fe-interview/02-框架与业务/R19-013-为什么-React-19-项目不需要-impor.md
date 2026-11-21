---
title: [R19-013] 为什么 React 19 项目不需要 import React 就能写 JSX？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-013：为什么 React 19 项目不需要 import React 就能写 JSX？
**答**：
- React 17 引入的新 JSX Transform 让编译器自动从 `react/jsx-runtime` 导入 jsx 函数，不再依赖作用域中的 React。
- 这意味着 JSX 文件没有"必须引入 React"的副作用，产物也略小。
- React 19 延续该机制；旧写法 `React.createElement` 依然可用但不再必要。
- 需要显式 import 的是用到的具名 API，例如 useState、useEffect、Fragment 等。

```jsx
// 旧写法：必须引入 React，因为编译产物要用 React.createElement
import React from 'react';
function Old() {
  return <p>旧写法</p>;
}

// 新 JSX Transform：编译器自动注入 jsx-runtime 的导入
// 这里只 import 真正用到的 Hook
import { useState } from 'react';
function New() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```
