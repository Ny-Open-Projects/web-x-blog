---
title: [DP-213] 源码识别：React ErrorBoundary 与 Suspense 的源码模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-213：源码识别：React ErrorBoundary 与 Suspense 的源码模式？
**答**：
- ErrorBoundary：getDerivedStateFromError + componentDidCatch 是 React 内建的**责任分派**——渲染错误向上冒泡直到最近的边界（职责链，边界即处理者）。
- Suspense：throw promise 的机制——数据组件 throw 一个 thenable，React 捕获后登记到最近的 Suspense 边界，promise resolve 后重渲染，这是"异常控制流"承载的**状态通知**（promise resolve → 通知 React）。
- 组合：ErrorBoundary（捕获 throw error）+ Suspense（捕获 throw promise）+ ErrorBoundary fallback——两个边界各管一种 throw。
- 识别要点：面试说清"throw promise 不是错误，是被语言特性借用的信号机制"，以及为什么异步错误进不了 ErrorBoundary（不在渲染管线内）。

```tsx
// Suspense 心智模型（简化实现）
function SuspenseLike({ fallback, children }) {
  const [resolved, setResolved] = useState(false);
  try {
    return children;                            // 正常渲染
  } catch (thrown) {
    if (isThenable(thrown)) {                   // throw 的是 promise → 数据未就绪
      thrown.then(() => setResolved(r => r + 1));   // resolve → 重渲染（观察 promise）
      return fallback;
    }
    throw thrown;                               // 非 promise → 继续上抛给 ErrorBoundary（职责链）
  }
}
// 真实 React 在 render 阶段处理：workLoop 捕获 thrown promise → 挂起 → resolve 后续 render
// 组合使用：
// <ErrorBoundary fallback={<ErrorBox/>}>
//   <Suspense fallback={<Skel/>}><ProfileData/></Suspense>
// </ErrorBoundary>
```
