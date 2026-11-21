---
title: [R19-005] use API 读取 Promise 是怎么工作的？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-005：use API 读取 Promise 是怎么工作的？
**答**：
- `use(promise)` 可以直接在组件中消费 Promise，未完成时组件 suspend，由最近的 Suspense 显示 fallback。
- 与 async/await 不同，use 不需要把组件标记成异步，渲染流程仍是同步调和。
- Promise 应该在组件外或缓存层创建，避免每次渲染重复发起请求导致无限 suspend。
- 也可以配合 throw promise 的旧式 Suspense 数据源无缝替换。

```jsx
import { use, Suspense } from 'react';

function Comments({ commentsPromise }) {
  // promise 未完成时组件挂起，完成后自动恢复渲染
  const comments = use(commentsPromise);
  return (
    <ul>
      {comments.map((c) => (
        <li key={c.id}>{c.text}</li>
      ))}
    </ul>
  );
}

export default function Page() {
  // 注意：Promise 要在组件外或缓存层创建（模块级变量、cache()、Suspense 缓存等），
  // 直接写在组件体里每次渲染都会重新 fetch，导致无限 suspend
  const commentsPromise = fetchComments();
  return (
    <Suspense fallback={<p>评论加载中...</p>}>
      <Comments commentsPromise={commentsPromise} />
    </Suspense>
  );
}
```
