---
title: [FRP-192] 手写 Suspense 边界：throw Promise 与 then 触发重试的完整机制？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-192：手写 Suspense 边界：throw Promise 与 then 触发重试的完整机制？

**答**：
- 协议：子组件数据未就绪时 **throw 一个 promise**（React 内部通过 throw 的东西判断是不是 thenable）——这是"挂起"的表达方式。
- 边界捕获 promise 后：渲染 fallback + 挂 then 回调；promise resolve 时把边界状态从"挂起"切回"渲染子树"——**重试**（重新 render children，此时数据已就绪）。
- 失败路径：promise reject 时冒泡到最近的 error boundary。
- 缓存一致性：真实 React 要求渲染函数幂等——promise resolve 后重试时，缓存层（如 resource.read 的实现）必须能同步返回已缓存值。

```javascript
// 简化实现，帮助理解 Suspense 的 throw promise 机制
// —— 资源包装：读缓存，未命中 throw promise ——
function createResource(promise) {
  let status = 'pending';
  let result;
  const suspender = promise.then(
    (v) => { status = 'success'; result = v; },
    (e) => { status = 'error'; result = e; }
  );
  return {
    read() {
      if (status === 'pending') throw suspender;   // 核心：挂起！
      if (status === 'error')   throw result;      // 交给 error boundary
      return result;                               // 就绪：同步返回
    },
  };
}

// —— 简化边界（类组件实现） ——
class Suspense extends React.Component {
  state = { pending: false };
  // React 内部不是 error boundary 实现，但"捕获 thenable"的语义等价：
  static getDerivedStateFromError(error) {
    if (error && typeof error.then === 'function') {
      return { pending: true, promise: error };   // 是 thenable：进入挂起态
    }
    throw error;                                   // 其他错误：继续冒泡给 error boundary
  }
  componentDidUpdate() {
    const { promise } = this.state;
    if (promise && this.state.pending) {
      promise.then(() => {
        // resolve：重试！重新渲染 children —— 此时 resource.read() 同步返回
        this.setState({ pending: false, promise: null });
      }, (err) => {
        this.setState({ pending: false, promise: null, error: err });
      });
    }
  }
  render() {
    if (this.state.pending) return this.props.fallback;
    if (this.state.error) throw this.state.error;
    return this.props.children;
  }
}

// —— 使用 ——
const userResource = createResource(fetchUser(1));
function Profile() {
  const user = userResource.read();   // 首次 throw suspender -> fallback
  return <h1>{user.name}</h1>;        // resolve 后重试 -> 同步拿到 -> 上屏
}
// <Suspense fallback={<Spinner />}><Profile /></Suspense>

// —— 渲染器内的真实集成（简化）：workLoop 中 throw 的处理 ——
function renderNode(node) {
  try { return node.type(node.props); }
  catch (thrown) {
    if (typeof thrown?.then === 'function') {
      thrown.then(() => retryRender(node));   // resolve 后重试该子树
      return createPlaceholder();              // 该位置渲染占位
    }
    throw thrown;
  }
}
```
