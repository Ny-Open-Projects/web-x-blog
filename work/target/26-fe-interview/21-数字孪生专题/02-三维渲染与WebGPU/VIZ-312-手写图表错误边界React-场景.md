---
title: [VIZ-312] 手写图表错误边界（React 场景）（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-312：手写图表错误边界（React 场景）（笔试）

**答**：
- 题目：React 图表组件错误边界——渲染异常捕获 → 降级 UI（占位/重试）→ 错误上报。类组件 getDerivedStateFromError 与 componentDidCatch。
- 思路：ErrorBoundary 包裹图表；fallback 按 props 可配；上报带图表类型与数据摘要。
- 评分点：ErrorBoundary 正确用法；fallback 设计；上报上下文。

```javascript
class ChartErrorBoundary extends React.Component {
  state = { error: null };
  static getDerivedStateFromError(error) { return { error }; }
  componentDidCatch(error, info) {
    report('chart-crash', {                                 // 上报
      message: error.message.slice(0, 100),
      chartType: this.props.chartType,
      componentStack: info.componentStack?.slice(0, 500),
    });
  }
  render() {
    if (this.state.error) {
      return this.props.fallback?.(this.state.error) ?? (
        <div className="chart-error" role="alert">
          <p>图表渲染失败</p>
          <button onClick={() => this.setState({ error: null })}>重试</button>
        </div>);                                             // 重试清 error 重渲染
    }
    return this.props.children;
  }
}
// 用法：<ChartErrorBoundary chartType="line"><LineChart data={data}/></ChartErrorBoundary>
```
