---
title: [MFW-139] RRv7 的 ErrorBoundary 与 shouldRevalidate 分别控制什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-139：RRv7 的 ErrorBoundary 与 shouldRevalidate 分别控制什么？
**答**：
- ErrorBoundary：路由模块内导出，捕获**该路由及子树**的渲染错误、loader/action 抛出的 Response（4xx/5xx）。就近渲染原则：错误发生在哪一层，哪一层的 boundary 接管，父级布局保持渲染（比 Next 全局 error.tsx 更细）。
- `isRouteErrorResponse(error)` 区分「主动 throw 的 HTTP 错误」与「意外异常」，前者展示 statusText、后者上报。
- shouldRevalidate：mutation（action 提交）后**精细控制哪些 loader 要不要重跑**——默认全重跑，签名里可拿到 currentUrl/formData/actionResult 等，按条件返回 false 跳过，省请求。
- 组合心智：ErrorBoundary 管「坏状态」，shouldRevalidate 管「好状态下的刷新成本」。

```tsx
// app/routes/products.tsx
import { isRouteErrorResponse, useRouteError, useLoaderData } from 'react-router';

export async function loader({ params }: any) {
  return { items: await getProducts(params.category) };
}

export function ErrorBoundary() {
  const error = useRouteError();
  if (isRouteErrorResponse(error)) {
    // 主动抛出的 HTTP 错误：404/403 等
    return <h1>{error.status} {error.statusText}</h1>;
  }
  // 意外异常：上报 + 兜底 UI
  reportError(error);
  return <h1>页面出错了</h1>;
}

// mutation 后的刷新控制
export function shouldRevalidate({
  currentUrl, nextUrl, formData, actionResult,
}: any) {
  // 删除单个商品：本路由 loader 不用重跑（fetcher 局部已处理）
  if (formData?.get('intent') === 'remove') return false;
  // 分类变了才重跑
  return currentUrl.pathname !== nextUrl.pathname
    || currentUrl.searchParams.get('category') !== nextUrl.searchParams.get('category');
}
```
