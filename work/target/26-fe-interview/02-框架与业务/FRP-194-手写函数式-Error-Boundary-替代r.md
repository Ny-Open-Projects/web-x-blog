---
title: [FRP-194] 手写函数式 Error Boundary 替代：react-error-boundary 的 resetKeys 与 retry 思想？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-194：手写函数式 Error Boundary 替代：react-error-boundary 的 resetKeys 与 retry 思想？

**答**：
- 函数组件自身无法成为 boundary（没有 getDerivedStateFromError），所以库的方案是：**内部用类组件承担捕获**，把 API 做成声明式的 props（fallback/fallbackRender/onReset/resetKeys）。
- `resetKeys` 的精髓：数组中任一值变化就**自动重置**错误态——利用 key/比较触发重建（同 FRP-160 的 key 思想），调用方无需手动 retry。
- `resetErrorBoundary` 回调：先调用 onReset（让调用方清理状态/重新请求），再清空内部错误态重渲染子树。
- 组合 Suspense：同一层级用 `useQuery`/resource 的错误自然落入该 boundary，形成"加载用 Suspense、失败用 Boundary"的对称结构。

```javascript
// 简化实现，帮助理解函数式 Error Boundary
import React from 'react';

// 对外暴露的函数式 API —— 内核仍是类组件
function ErrorBoundary({ fallback, fallbackRender, FallbackComponent, onReset, resetKeys, children }) {
  return (
    <ErrorBoundaryInner
      fallback={fallback}
      fallbackRender={fallbackRender}
      FallbackComponent={FallbackComponent}
      onReset={onReset}
      resetKeys={resetKeys}
    >
      {children}
    </ErrorBoundaryInner>
  );
}

class ErrorBoundaryInner extends React.Component {
  constructor(props) {
    super(props);
    this.state = { error: null, resetKeys: props.resetKeys };
  }

  static getDerivedStateFromError(error) {
    return { error };
  }

  componentDidUpdate(prevProps) {
    // 核心 1：resetKeys 自动重置 —— 任一 key 变化就清空错误态
    const { resetKeys } = this.props;
    if (this.state.error && resetKeys && keysChanged(prevProps.resetKeys, resetKeys)) {
      this.resetErrorBoundary();
    }
  }

  componentDidCatch(error, info) {
    this.props.onError?.(error, info);
  }

  // 核心 2：统一的重置入口
  resetErrorBoundary = (...args) => {
    this.props.onReset?.({ ...args, error: this.state.error });  // 先让调用方清理
    this.setState({ error: null });                               // 再重渲染 children
  };

  render() {
    const { error } = this.state;
    if (error === null) return this.props.children;
    const { fallback, fallbackRender, FallbackComponent } = this.props;
    const props = { error, resetErrorBoundary: this.resetErrorBoundary };
    if (React.isValidElement(fallback)) return fallback;
    if (fallbackRender) return fallbackRender(props);
    if (FallbackComponent) return <FallbackComponent {...props} />;
    throw error;   // 没提供 fallback：继续上抛给更外层
  }
}

function keysChanged(a = [], b = []) {
  return a.length !== b.length || a.some((v, i) => !Object.is(v, b[i]));
}

// 使用：
// <ErrorBoundary
//   resetKeys={[query]}                    // 搜索词变化 -> 自动重试渲染
//   fallbackRender={({ error, resetErrorBoundary }) => (
//     <div>
//       {error.message}
//       <button onClick={() => resetErrorBoundary()}>重试</button>
//     </div>
//   )}
// >
//   <ResultList query={query} />
// </ErrorBoundary>
// 对称结构：<Suspense fallback={骨架}> + <ErrorBoundary fallback={错误态}> 包同一棵子树
```
