---
title: [204] RSC 流式渲染中，Server 组件抛错后 UI 如何优雅降级
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, RSC, 错误边界]
type: 面试题
---

## MFW-204：RSC 流式渲染中，Server 组件抛错后 UI 如何优雅降级？

**答**：
- 流式 SSR 下响应头已发出（200），错误无法再变成 500 页，只能靠已发送 HTML 中的 Suspense boundary 做「插槽内降级」。
- 每个 `<Suspense>` 包裹的异步 Server 子树是独立出错单元：该 slot 通过注入的脚本触发 client 端 error boundary 兜底 UI，其余 slot 正常完成流式。
- `loading.tsx` 只管「未完成」，`error.tsx` 才管「出错了」；两者都要写，否则白屏或整页报错。
- 生产模式会抹掉错误细节，只给 digest 哈希，日志侧需用该哈希关联服务端 stack。
- 追问钩子：`generateMetadata` 抛错为什么会导致整个页面失败？——它不在 Suspense 边界内。

```jsx
// app/product/[id]/page.tsx
import { Suspense } from 'react';
export default function Page({ params }) {
  return (
    <div>
      {/* 主内容：失败只降级这一块 */}
      <Suspense fallback={<ProductSkeleton />}>
        <ProductInfo id={params.id} />
      </Suspense>
      <Suspense fallback={<ReviewSkeleton />}>
        <Reviews id={params.id} /> {/* 挂了不影响上面 */}
      </Suspense>
    </div>
  );
}
async function ProductInfo({ id }) {
  const data = await getProduct(id); // 抛错 -> 被最近的 Suspense 捕获
  return <h1>{data.name}</h1>;
}

// app/product/[id]/error.tsx —— client 组件，slot 级兜底
'use client';
export default function Error({ error, reset }) {
  return <button onClick={reset}>加载失败（{error.digest}），点我重试</button>;
}
```
