---
title: [FRP-193] 手写 Error Boundary（类组件版）：getDerivedStateFromError 与 componentDidCatch 的分工？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-193：手写 Error Boundary（类组件版）：getDerivedStateFromError 与 componentDidCatch 的分工？

**答**：
- 两个生命周期分工：`getDerivedStateFromError` **渲染阶段**调用，返回降级 state（不能有副作用）；`componentDidCatch` **commit 阶段**调用，做日志/上报（可以副作用）。
- 捕获范围：子树的**渲染期错误、生命周期错误、构造函数错误**；不捕获：事件回调（要 try/catch）、异步回调、自身错误、SSR 错误。
- 卸载策略：React 的"不可恢复错误"（error boundary 自身渲染出错且无更外层边界）会**卸载整棵树**——所以根级必须有兜底。
- 恢复：reset state（配合 key 或重置回调）即可重新渲染子树（见 FRP-147 的 reset 与 FRP-160 的 key 重置）。

```javascript
// 简化实现，帮助理解类组件 Error Boundary
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { error: null };      // error 非空 -> 渲染 fallback
  }

  // 1. 渲染阶段：同步、无副作用、返回新 state —— 决定"降级 UI"
  static getDerivedStateFromError(error) {
    return { error };
  }

  // 2. commit 阶段：副作用合法 —— 日志、上报、通知
  componentDidCatch(error, info) {
    // info.componentStack: 出错组件的组件栈
    reportError(error, info.componentStack);
    this.props.onError?.(error, info);
  }

  reset = () => this.setState({ error: null });   // 手动恢复：重新渲染 children

  render() {
    if (this.state.error) {
      return this.props.fallback
        ? this.props.fallback(this.state.error, this.reset)
        : <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}

// —— React 内部的捕获点（简化） ——
function commitRoot(root) {
  // commit 阶段遍历 effectList 时，每个生命周期调用都被 try/catch 包住：
  try {
    safelyCallComponentDidMount(fiber);
  } catch (error) {
    captureCommitPhaseError(fiber, error);   // 上抛给最近 boundary
  }
}
function renderRootWithError(error, boundaryFiber) {
  // render 阶段捕获：标记 boundaryFiber 有错误态，本次 commit 渲染其 fallback
  boundaryFiber.stateNode.setState({ error });   // 概念示意
}

// 捕获边界演示：
// <Boundary>                       捕获渲染/生命周期错误
//   <button onClick={() => { throw ... }} />   不捕获！事件回调要用 try/catch
//   <span>{setTimeout(() => { throw ... })}</span>  不捕获！异步错误要全局 handler
// </Boundary>
// window.addEventListener('error', ...) + unhandledrejection 是异步兜底的最后一道
```
