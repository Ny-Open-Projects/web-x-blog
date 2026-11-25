---
title: [R19-156] React 应用的错误处理体系如何设计？ErrorBoundary 分层、全局兜底与上报如何组织？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-156：React 应用的错误处理体系如何设计？ErrorBoundary 分层、全局兜底与上报如何组织？
**答**：
- 分层思想：**局部边界**（可恢复的子树：卡片、表格区块）包在最易出错处，错误降级为局部占位；**路由级边界**兜住整页；**根边界**兜住所有未捕获并渲染全站错误页。
- 渲染外错误边界补位：事件处理器/异步回调的错误用 `window.onerror` + `unhandledrejection` 捕获；render 越界错误是边界专门管辖。
- 上报统一收口：一个 `reportError` 工具聚合（Sentry 类 SDK / 自建），携带组件栈、用户路径、release 版本；边界与全局监听都只调它。
- 重试能力：边界暴露 reset（key 变化或手动重置），让"重试"成为一等交互而不是刷新页面。

```tsx
// error-system.tsx —— 分层错误处理体系
import { Component, type ErrorInfo, type ReactNode } from 'react';
import { useRouteError } from 'react-router-dom';

// 统一上报收口：所有错误只走这一条路
export function reportError(error: Error, context: Record<string, unknown> = {}) {
  // Sentry.captureException(error, { extra: context }) 或自建上报
  fetch('/api/log/error', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: error.message,
      stack: error.stack,
      componentStack: context.componentStack,
      path: location.pathname,
      release: import.meta.env.VITE_RELEASE,
    }),
  }).catch(() => {});
}

// 可复用边界：支持自定义降级与重试
export class ErrorBoundary extends Component<{
  fallback: (info: { error: Error; reset: () => void }) => ReactNode;
  onError?: (e: Error) => void;
  children: ReactNode;
}, { error: Error | null }> {
  state = { error: null as Error | null };

  static getDerivedStateFromError(error: Error) {
    return { error };
  }
  componentDidCatch(error: Error, info: ErrorInfo) {
    reportError(error, { componentStack: info.componentStack });
    this.props.onError?.(error);
  }
  reset = () => this.setState({ error: null });

  render() {
    return this.state.error
      ? this.props.fallback({ error: this.state.error, reset: this.reset })
      : this.props.children;
  }
}

// 局部边界：图表卡片崩了不影响整页
function ChartCard() {
  return (
    <ErrorBoundary
      fallback={({ reset }) => (
        <div>图表加载失败 <button onClick={reset}>重试</button></div>
      )}
    >
      <HeavyChart />
    </ErrorBoundary>
  );
}

// 路由级兜底：react-router 的 errorElement
export function RouteErrorPage() {
  const error = useRouteError() as Error;
  return (
    <div>
      <h1>页面出错了</h1>
      <p>{error?.message}</p>
      <button onClick={() => location.assign('/')}>回首页</button>
    </div>
  );
}

// 入口：渲染外错误的最后防线
export function setupGlobalHandlers() {
  window.addEventListener('error', e => reportError(e.error ?? new Error(e.message)));
  window.addEventListener('unhandledrejection', e => reportError(new Error(String(e.reason))));
}
```
