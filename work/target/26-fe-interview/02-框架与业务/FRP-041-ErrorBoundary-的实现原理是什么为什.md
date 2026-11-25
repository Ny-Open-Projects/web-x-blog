---
title: [FRP-041] ErrorBoundary 的实现原理是什么？为什么捕获不了事件与异步错误？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-041：ErrorBoundary 的实现原理是什么？为什么捕获不了事件与异步错误？

**答**：
- ErrorBoundary 是**类组件**的静态方法 `getDerivedStateFromError`（渲染 fallback UI）与实例方法 `componentDidCatch`（上报日志）——React 在 commit 阶段前对子树渲染错误做 try-catch，捕获后**卸载出错的子树**并重渲 fallback。
- 传播规则：沿 Fiber 向上找最近的 boundary；boundary 自身抛错则继续向上；没有 boundary 时整棵树卸载（白屏）。
- 捕获不了三类错误：**事件处理器**（不在 render 流程内，用 try-catch 或全局 onerror）、**异步回调/定时器**、**SSR/服务端错误**——因为它们不发生在 React 的渲染调用栈里。
- 实际落地：根级一个兜底 boundary + 路由级/组件级局部 boundary，配合 09 章的上报通道。

```jsx
// 一一对应：手写 ErrorBoundary 与边界说明
import { Component } from 'react';

class ErrorBoundary extends Component {
  state = { error: null };

  static getDerivedStateFromError(error) {
    // 阶段一 render：子树抛错后调用，返回值作为新 state —— 用于渲染 fallback
    return { error };
  }

  componentDidCatch(error, info) {
    // 阶段二 commit：记录副作用，如上报
    // info.componentStack 是 React 生成的组件调用栈
    reportToMonitor('render-error', { message: error.message, stack: info.componentStack });
  }

  render() {
    if (this.state.error) {
      return this.props.fallback ?? <h1>页面出错了</h1>;
    }
    return this.props.children; // 无错误时正常渲染子树
  }
}

// 用法：按层级包裹
// <ErrorBoundary fallback={<WidgetError />}>
//   <RiskyWidget />
// </ErrorBoundary>

// 捕获不到的场景演示：
class Demo extends Component {
  componentDidMount() {
    // 异步错误：不在 React 渲染栈内，boundary 捕获不到 —— 需要全局兜底
    setTimeout(() => { throw new Error('异步错误 boundary 捕获不到'); }, 0);
  }
  handleClick = () => {
    // 事件错误：同样捕获不到 —— 在事件处理器里 try-catch 或全局 onerror
    try {
      JSON.parse('{bad json}');
    } catch (e) {
      reportToMonitor('event-error', e);
    }
  };
  render() { return <button onClick={this.handleClick}>click</button>; }
}
```

## 追问（补充）

**追问**：

1. React 19 的 onCaughtError / onUncaughtError 和 boundary 是什么关系？ → 正交关系。root 选项里的三个回调只负责统一上报，fallback 仍由 boundary 渲染；19 的好处是不必再在每个 boundary 的 componentDidCatch 里重复接监控。
2. Suspense 抛的 promise 会被 error boundary 接住吗？ → 不会。Suspense 认的是 thenable，不走错误通道；只有真正 throw 的 Error 才进 boundary。异步取数失败要先把 promise reject 转成在 render 期 throw，才能被兜住。
3. boundary 里做了 reset 为什么还显示错误页？ → 因为 getDerivedStateFromError 已把 error 写进 state，reset 必须显式把 error 置回 null；而且旧子树 fiber 仍是坏的，通常还要把重试计数当 key 重建子树才彻底恢复，只清 state 会停在半坏的树上。
