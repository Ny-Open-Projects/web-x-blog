---
title: [MFW-035] 笔试：手写 ErrorBoundary 组件（含 reset 重试与 fallback 函数式）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-035：笔试：手写 ErrorBoundary 组件（含 reset 重试与 fallback 函数式）
**答**：不用 error.js，手写一个通用 React ErrorBoundary（class 组件）：捕获子树渲染错误，支持 `fallbackRender({error, reset})`、`onError` 上报回调、`reset()` 重试。要求：fallback 自身抛错不能死循环；reset 改变 retryKey 强制重挂载子树；事件回调错误不在捕获范围（说明即可）。

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { error: null, retryKey: 0 };
  }

  static getDerivedStateFromError(error) {
    // 渲染期错误 -> 转为 state，触发降级渲染
    return { error };
  }

  componentDidCatch(error, info) {
    // 可拿到组件栈 info.componentStack，用于上报
    this.props.onError?.(error, info);
  }

  reset = () => {
    // 换 key 强制子树整体重挂载，重置所有内部 state
    this.setState((s) => ({ error: null, retryKey: s.retryKey + 1 }));
  };

  render() {
    const { error, retryKey } = this.state;
    if (error) {
      const fb = this.props.fallbackRender;
      if (typeof fb !== 'function') return <div>出错了</div>;
      try {
        return fb({ error, reset: this.reset });
      } catch (fbError) {
        // fallback 自身抛错：渲染内置兜底，避免死循环
        return <div>渲染降级 UI 时再次出错</div>;
      }
    }
    return <div key={retryKey}>{this.props.children}</div>;
  }
}

export default ErrorBoundary;

// ---- 用法 ----
// <ErrorBoundary fallbackRender={({ error, reset }) => (
//   <div>榜单挂了 <button onClick={reset}>重试</button></div>
// )} onError={(e, i) => report(e, i)}>
//   <Ranking />
// </ErrorBoundary>

// **评分点**
// 1. getDerivedStateFromError 与 componentDidCatch 职责区分：前者改渲染，后者做副作用上报。
// 2. reset 通过 retryKey 强制 remount，而不是只清 error state（子树内部脏 state 会被保留是常见 bug）。
// 3. fallback 抛错的防御性处理，避免「错误边界里再抛错」的死循环。
// 4. 明确局限：不捕获事件回调、异步回调、SSR 错误——这是 class 边界的天然边界，说明出来加分。
```
