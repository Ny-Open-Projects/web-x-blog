---
title: [FRP-040] Suspense 的原理是什么？"throw Promise" 是怎么工作的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-040：Suspense 的原理是什么？"throw Promise" 是怎么工作的？

**答**：
- 核心机制：渲染过程中如果数据/模块没就绪，组件**throw 一个 thenable**；React 在 beginWork 外层 try-catch 捕获，识别为 Promise 后，在 promise resolve 前展示 fallback。
- 捕获后 React 给 Suspense 边界打上标记，commit fallback 树；Promise resolve 后以**重试 lane** 重新调度该子树渲染，这次组件正常返回。
- `React.lazy` 就是 throw promise 的内置实现（模块未加载完时 throw `import()` 的 promise）。
- 数据请求配合（React 18+ `use`/React Query suspense 模式）：读取缓存未命中时 throw 请求 promise，命中则直接返回数据，实现"组件里 await"的声明式写法。

```jsx
// 一一对应：手写一个 throw promise 的组件，理解 Suspense 机制
import { Suspense } from 'react';

const cache = new Map();

function readData(id) {
  if (cache.has(id)) return cache.get(id);          // 已就绪：同步返回
  // 未就绪：发起请求并 throw promise —— React 捕获它
  const promise = fetch(`/api/user/${id}`).then((r) => r.json());
  const wrapped = promise.then((data) => {
    cache.set(id, data);
    return data;
  });
  throw wrapped; // 关键：渲染被"挂起"，Suspense 边界捕获
}

function User({ id }) {
  const user = readData(id); // 就绪前 throw，就绪后同步读
  return <h1>{user.name}</h1>;
}

export default function Page() {
  return (
    <Suspense fallback={<h1>加载中...</h1>}>
      {/* 首次渲染：User throw promise -> React 渲染 fallback
          promise resolve -> React 以 retry lane 重新渲染 User -> 正常显示 */}
      <User id={1} />
    </Suspense>
  );
}

// 简化实现，帮助理解边界的捕获逻辑：
// function renderWithSuspense(children, fallback) {
//   try {
//     return render(children);
//   } catch (thrown) {
//     if (typeof thrown?.then === 'function') {   // throw 的是 promise
//       thrown.then(() => retryLaneRender(children)); // resolve 后重试
//       return render(fallback);                      // 先提交 fallback
//     }
//     throw thrown; // 其它错误交给 ErrorBoundary
//   }
// }
```
