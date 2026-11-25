---
title: [R19-065] 如何封装一个可复用的 ErrorBoundary？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-065：如何封装一个可复用的 ErrorBoundary？
**答**：
- class 组件无法被 Hooks 替代，getDerivedStateFromError 负责降级 UI，componentDidCatch 负责上报。
- fallback 设计成双形态：传 ReactNode 直接渲染，传函数则拿到 error 和手动 reset 能力。
- resetKeys 是关键工程能力：当路由参数等依赖变化时自动清空错误，避免用户卡在错误页。
- 业务上按路由级/模块级分层包裹，块级边界兜局部错误，页面级边界兜全局。

```jsx
import { Component } from 'react';

// 通用错误边界：fallback 可传节点或 render prop，resetKeys 变化自动恢复
export class ErrorBoundary extends Component {
  state = { error: null };

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidCatch(error, info) {
    this.props.onError?.(error, info.componentStack);
  }

  componentDidUpdate(prevProps) {
    if (!this.state.error) return;
    const changed = this.props.resetKeys?.some((key, i) => key !== prevProps.resetKeys?.[i]);
    if (changed) this.setState({ error: null });
  }

  render() {
    const { error } = this.state;
    if (!error) return this.props.children;
    if (typeof this.props.fallback === 'function') {
      return this.props.fallback(error, () => this.setState({ error: null }));
    }
    return this.props.fallback ?? <div>页面出错了</div>;
  }
}

// 用法：
// <ErrorBoundary
//   resetKeys={[userId]}
//   fallback={(err, reset) => <RetryPanel error={err} onRetry={reset} />}
// >
//   <OrderList userId={userId} />
// </ErrorBoundary>
```

**追问**：

1. `resetKeys` 用浅比较有什么坑？→ 父级每次 render 都新建数组，`some` 逐项比较看起来没问题，但如果 key 本身是对象就会永远判定"变化"，一有更新就 reset；应传稳定引用。
2. 多个边界嵌套时错误落到哪一层？→ 最近的祖先边界先接住；如果它渲染 fallback 时又抛错，会继续向上冒泡，形成级联降级，所以 fallback 本身要足够简单。
3. 边界能捕获兄弟组件的错误吗？→ 不能，只兜自己的子树；要兜住并列的两个兄弟，必须把边界提到它们的共同父级。
