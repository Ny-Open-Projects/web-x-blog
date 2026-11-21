---
title: [FRP-147] RSC 的错误处理与重试边界是怎么设计的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-147：RSC 的错误处理与重试边界是怎么设计的？

**答**：
- 服务端流式渲染中某洞出错：该洞的 promise 被 reject，流里输出**错误 chunk**；客户端在最近的 `error boundary` 渲染降级 UI，其余洞不受影响。
- 框架层重试：服务端可对洞级失败做有限次重试（Next 会对部分渲染错误重新执行该段）；客户端可用 error boundary 的 **reset** 触发重新请求（重新调用 refetch/action）。
- 分层兜底：`error.tsx`（路由级 boundary + reset）、`global-error.tsx`（根级兜底）、`not-found.tsx`（404 语义）；开发态有 overlay，生产态只输出边界 UI。
- 关键认知：流已经发出的部分**无法撤回**——错误处理是"洞级隔离"而不是"整页重试"；整页失败才走全局兜底。

```javascript
// 简化实现，帮助理解洞级错误与重试
// —— 服务端：洞失败 -> 输出错误 chunk ——
function serializeHole(node, out) {
  node.promise.then(
    v  => out.push(`${node.id}:${serialize(v)}`),
    e  => out.push(`${node.id}:{"error":${serializeError(e)}}`)  // 错误也是普通 chunk
  );
}

// —— 客户端：错误 chunk 触发最近边界 ——
function onChunk(id, payload) {
  if (payload.error) {
    pendingHoles.get(id).reject(new Error(payload.error.message));
    // React 内部：该 Suspense 子树抛错 -> 冒泡到最近 error boundary
  } else {
    pendingHoles.get(id).resolve(payload);
  }
}

// —— error.tsx：客户端组件，接收 reset ——
'use client';
function ErrorPage({ error, reset }) {
  return (
    <div>
      <p>{error.message}</p>
      <button onClick={() => reset()}>重试</button>
      {/* reset 的实现：重置 boundary 状态并重新触发该子树的渲染请求 */}
    </div>
  );
}

// —— reset 的简化原理 ——
class ErrorBoundary extends React.Component {
  state = { error: null };
  reset = () => {
    this.setState({ error: null });   // 清掉错误态 -> React 重新渲染 children
    this.props.onReset?.();           // 框架 hook：重新发起对应 RSC 请求
  };
  static getDerivedStateFromError(error) { return { error }; }
  render() { return this.state.error ? this.props.fallback : this.props.children; }
}

// 重试策略链：洞级 retry（服务端内部，如 3 次）-> 边界 UI + reset（用户手动）-> global-error（最后一道）
```

## 二十二、React 并发与调度深入
