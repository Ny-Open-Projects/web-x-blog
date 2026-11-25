---
title: [MFW-014] React 挂起（throw Promise）机制是什么？和 RSC 流式怎么配合？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-014：React 挂起（throw Promise）机制是什么？和 RSC 流式怎么配合？
**答**：
- 挂起协议：Promise 未 resolve 时组件直接 `throw promise`，React 捕获后渲染最近的 Suspense fallback；resolve 后 React 重试该子树。这就是「组件直接 await 数据」的底层实现。
- 服务端（RSC 流式）：React 渲染树遇到挂起点，先发 fallback 到流里，把该分支标记 pending；Promise settle 后把结果序列化成 RSC Payload 补发，客户端 React 用补发的数据替换占位。
- 客户端（导航预取）：跳转新页面时 Client Component 里 use() 读到的 Promise 若来自服务端预取，也会走同一套 Suspense 机制，只是 fallback 显示在客户端。
- 关键细节：**同一个 Promise 的状态被 React 缓存**（同一次渲染里重复 throw 不会重启任务）；若 Promise 每次渲染都新建，会陷入无限 fallback——需要 cache/wrapped promise。
- 追问：`use(promise)` 与 throw Promise 等价，但 use() 允许在条件分支后调用，比 hooks 规则宽松。

```jsx
import { use } from 'react';

// 服务端组件：慢数据组件
async function MovieDetail({ id }) {
  // 框架层面：await 未完成时该分支被挂起，最近 Suspense 先发 fallback
  const detail = await getMovie(id); // 内部 throw promise 等价
  return <h1>{detail.title}</h1>;
}

// 客户端组件：use() 读服务端传来的 Promise
'use client';
export function Comments({ commentsPromise }) {
  const comments = use(commentsPromise); // 挂起直到 Promise resolve
  return comments.map((c) => <p key={c.id}>{c.text}</p>);
}

// 父组件（Server）：发起 Promise 不 await —— 传下去，边界先行
export default async function Page({ params }) {
  const commentsPromise = getComments(params.id); // 不 await，立即返回
  return (
    <>
      <MovieDetail id={params.id} />
      <Suspense fallback={<p>评论加载中…</p>}>
        <Comments commentsPromise={commentsPromise} />
      </Suspense>
    </>
  );
}
```
