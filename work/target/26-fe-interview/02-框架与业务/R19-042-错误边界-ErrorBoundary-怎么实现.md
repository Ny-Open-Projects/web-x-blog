---
title: [R19-042] 错误边界 ErrorBoundary 怎么实现？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-042：错误边界 ErrorBoundary 怎么实现？
**答**：
- 错误边界是实现了 getDerivedStateFromError 或 componentDidCatch 的 class 组件（目前仍需 class）。
- getDerivedStateFromError 渲染降级 UI；componentDidCatch 拿到 error 与 componentStack，适合上报。
- 它捕获的是子树的渲染期、生命周期内的错误，把它包在路由、区块级别做兜底。
- React 19 生态中也可以用 react-error-boundary 库的组件化封装。

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, info) {
    // 在这里上报监控：error 与组件栈
    console.error(error, info.componentStack);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ?? <p>出错了</p>;
    }
    return this.props.children;
  }
}

function App() {
  return (
    <ErrorBoundary fallback={<p>面板崩了，请刷新</p>}>
      <Widget />
    </ErrorBoundary>
  );
}
```
