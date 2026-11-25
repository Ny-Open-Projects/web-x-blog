---
title: [R19-427] 笔试：手写 lazy 组件与 ErrorBoundary 类
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## R19-427：笔试：手写 lazy 与 ErrorBoundary

**答**：实现：① `lazy(loader)`：返回包装组件——首次渲染触发 loader，throw promise（配合 Suspense），resolve 缓存，reject 交 ErrorBoundary；② ES 模块 default 解包；③ ErrorBoundary class 组件：getDerivedStateFromError + componentDidCatch + 重试（resetKeys 支持路由变化自动重置）；④ retry 计数熔断。写出实现。

```javascript
function lazy(loader) {
  let cached = null, promise = null;
  return function LazyWrapper(props) {
    if (cached) return h(cached, props);
    promise ??= loader().then((m) => {
      cached = m.default ?? m;                      // ES 模块解包
      return cached;
    });
    throw promise;                                  // 未就绪 → throw 给 Suspense
  };
}

class ErrorBoundary extends Component {
  state = { error: null, retries: 0 };
  static getDerivedStateFromError(error) { return { error }; }
  componentDidCatch(error, info) { this.props.onError?.(error, info); }
  componentDidUpdate(prev) {
    // resetKeys 变化自动重置(路由切换恢复)
    if (this.state.error && prev.resetKeys?.some((k, i) => k !== this.props.resetKeys?.[i]))
      this.setState({ error: null });
  }
  render() {
    if (this.state.error) {
      if (this.state.retries < (this.props.maxRetries ?? 3))
        return h('button', { onClick: () => this.setState(s => ({ error: null, retries: s.retries + 1 })) }, '重试');
      return this.props.fallback ?? h('div', null, '出错了');
    }
    return this.props.children;
  }
}
```

**评分点**：
- lazy 的 promise 缓存 + throw 协议（与 Suspense 配合）
- default 解包与 resolve 后同步渲染
- getDerivedStateFromError 与 componentDidCatch 的分工（状态 vs 副作用）
- resetKeys 路由联动重置 + 重试熔断
