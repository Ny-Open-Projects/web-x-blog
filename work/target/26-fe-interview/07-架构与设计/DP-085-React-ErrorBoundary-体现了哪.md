---
title: [DP-085] React ErrorBoundary 体现了哪些模式？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-085：React ErrorBoundary 体现了哪些模式？
**答**：
- ErrorBoundary 用类组件 `getDerivedStateFromError`（渲染降级 UI）+ `componentDidCatch`（上报副作用）捕获子树渲染错误。
- 模式视角：**组合模式**（包裹子树，树形粒度可控）、**模板方法**（框架固定"捕获→降级→上报"骨架，用户填钩子）、**策略**（不同边界可注入不同降级 UI）。
- 工程规范：路由级/页面级/组件级分层部署边界；边界本身崩溃时由上层兜底；事件回调/异步错误不在捕获范围（需全局兜底）。
- 现代补充：`react-error-boundary` 库的 `useQueryErrorResetBoundary`、Suspense 与 ErrorBoundary 配合。

```jsx
// ErrorBoundary：模板方法（框架骨架）+ 策略（可配置降级 UI）
class ErrorBoundary extends React.Component {
  state = { error: null };
  static getDerivedStateFromError(error) {   // 框架固定调用：渲染期捕获 -> 触发降级
    return { error };
  }
  componentDidCatch(error, info) {           // 框架固定调用：副作用阶段（上报/日志）
    reportToSentry(error, info.componentStack);
  }
  render() {                                 // 策略：降级 UI 可注入，默认兜底
    if (this.state.error) {
      const Fallback = this.props.fallback;  // 不同场景注入不同降级策略
      return Fallback
        ? <Fallback error={this.state.error} reset={() => this.setState({ error: null })} />
        : <div>页面出错了</div>;
    }
    return this.props.children;              // 组合模式：包裹任意子树
  }
}
function reportToSentry(err, stack) { console.log('[监控]', err.message); }
// 分层部署：路由级兜底 + 组件级细粒度
function Page() {
  return (
    <ErrorBoundary fallback={({ error }) => <div>模块降级 {error.message}</div>}>
      <RiskyChart />          {/* 图表挂了只降级图表 */}
    </ErrorBoundary>
  );
}
function RiskyChart() { throw new Error('data undefined'); } // 模拟渲染错误
// <Page /> -> [监控] data undefined -> 模块降级 data undefined
// 边界外仍有整页 <ErrorBoundary> 兜底 —— 树形分层（组合模式）
```

## 十一、框架源码中的模式识别综合
