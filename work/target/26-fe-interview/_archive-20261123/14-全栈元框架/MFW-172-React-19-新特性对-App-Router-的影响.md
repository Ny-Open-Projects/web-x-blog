---
title: [MFW-172] React 19 的新特性对 App Router 的影响有哪些？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-172：React 19 的新特性对 App Router 的影响有哪些？
**答**：
- Actions 体系（`useActionState`/`useFormStatus`/`useOptimistic`）把「表单提交」变成一等公民，App Router 的 Server Action 直接建立在这套协议上，表单不写 JS 也能提交（渐进增强）。
- `use(Promise)` / `use(Context)` 可以在渲染期间读取 Promise 并配合 Suspense，替代部分 `useEffect + setState` 取数，RSC 传下来的 Promise 直接在 Client Component 里 `use`。
- `cache()` 取代手动 Request Memoization，在单次请求内对同一入参去重，RSC 里跨组件共享取数结果。
- `ref` 作为 prop、`forwardRef` 废弃；`<Context.Provider>` 被 `<Context>` 取代——写 Client 组件时注意 API 更新。
- metadata 相关：`<title>`/`<meta>` 可以直接写在组件里，由 React hoist 到 head，和 Next 的 Metadata API 是两层机制，别混用重复。

```javascript
// RSC：把 Promise 直接传给客户端
export default async function Page() {
  const userPromise = getUser(); // 不 await，让子组件各自 use + Suspense
  return <Suspense fallback={<Skeleton />}><Profile userPromise={userPromise} /></Suspense>;
}

'use client';
import { use } from 'react';
function Profile({ userPromise }) {
  const user = use(userPromise); // 挂起时由 Suspense 接管
  return <h1>{user.name}</h1>;
}
```
