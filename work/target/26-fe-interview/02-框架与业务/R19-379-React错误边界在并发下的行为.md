---
title: [R19-379] React 错误边界在并发下的行为
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## R19-379：React 错误边界在并发下的行为

**答**：
- 边界捕获范围：render 期错误、生命周期/hook 错误、子树错误——不捕获：事件处理器、异步回调、SSR 错误、Error Boundary 自身
- 并发下的语义：render 中途抛错 → 边界以「当前快照」渲染 fallback——被中断的低优渲染抛错不会污染已提交的旧 UI；fallback 提交是原子的
- 边界粒度设计：路由级（页面 404/500）、模块级（一个面板挂不拖垮整页）、关键组件级——React 19 的 onCaughtError/onUncaughtError root 选项统一上报
- 恢复策略：边界内「重试 key」（强制重建子树）+ 失败次数熔断（连续 3 次失败改永久错误态）——无限重试风暴防护
- async 错误桥接：异步错误需要「同步抛出」才能进边界——组件内 throw 被 Suspense/边界捕获的模式（use 的 promise reject → 边界）

```jsx
class PanelBoundary extends Component {
  state = { error: null, retries: 0 };
  static getDerivedStateFromError(error) { return { error }; }
  componentDidCatch(error, info) { report(error, info); }
  render() {
    if (this.state.error && this.state.retries < 3)
      return <RetryUI onRetry={() => this.setState(s => ({ error: null, retries: s.retries + 1 }))} />;
    if (this.state.error) return <PermanentError />;
    return this.props.children;
  }
}
```

**追问**：

1. 并发下 fallback 本身的渲染会不会被打断？→ 会，fallback 也是普通 render，可被更高优先级更新抢断；但一旦提交就是完整错误态，不会出现半截 fallback 被用户看到。
2. `use(promise)` 的 promise reject 后点重试还是同一个错误，为什么？→ promise 被缓存在 thenable 上，重试必须让数据源产生**新的** promise（失效缓存/换 key），否则读到的是同一个已 reject 的结果。
3. `onCaughtError` 和 `componentDidCatch` 有什么分工？→ `onCaughtError` 是 root 级统一钩子，能拿到 error 与组件栈但不改变边界渲染行为；`componentDidCatch` 在边界内执行，适合做局部埋点和差异化降级。
