---
title: [ARC-325] 笔试题：实现组件库错误边界与降级 UI？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-325：笔试题：实现组件库错误边界与降级 UI？
**题目**：实现 `ErrorBoundary`：1) 捕获渲染错误展示降级 UI；2) 支持自定义 fallback（函数式，接收错误与重置回调）；3) resetKeys 变化时自动重置子树；4) 错误上报钩子；5) 不捕获事件处理与异步错误（说明原因）。
**评分点**：
- 生命周期方法使用正确（getDerivedStateFromError 设置降级态、componentDidCatch 上报）。
- resetKeys 比较逻辑正确（浅比较，变化即重置）。
- fallback 签名设计合理（error + resetErrorBoundary）。
- 说清边界局限：class 边界只捕获渲染/lifecycle 同步错误，异步与事件回调需全局兜底。
```tsx
interface EBProps {
  fallback: React.ReactNode | ((p: { error: Error; reset: () => void }) => React.ReactNode);
  resetKeys?: unknown[];
  onError?: (e: Error, info: React.ErrorInfo) => void;
}
class ErrorBoundary extends React.Component<EBProps, { error: Error | null }> {
  state = { error: null };
  static getDerivedStateFromError(error: Error) { return { error }; }
  componentDidCatch(error, info) { this.props.onError?.(error, info); }         // 4) 上报
  componentDidUpdate(prev) {
    if (!this.state.error) return;
    const changed = this.props.resetKeys?.some((k, i) => k !== prev.resetKeys?.[i]);
    if (changed) this.setState({ error: null });                                // 3) 自动重置
  }
  reset = () => this.setState({ error: null });
  render() {
    if (this.state.error) {
      const fb = this.props.fallback;
      return typeof fb === 'function' ? fb({ error: this.state.error, reset: this.reset }) : fb;
    }
    return this.props.children;
  }
}
// 5) 局限：onClick 内 throw / promise reject 不经过 React 渲染管线 → 用 window.onerror/unhandledrejection 全局兜底
```
