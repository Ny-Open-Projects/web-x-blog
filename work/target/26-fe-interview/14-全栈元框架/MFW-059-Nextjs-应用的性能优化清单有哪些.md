---
title: [MFW-059] Next.js 应用的性能优化清单有哪些？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-059：Next.js 应用的性能优化清单有哪些？
**答**：
- 渲染层：默认 RSC 化（client component 越少越好）、`Suspense` 分层流式让 TTFB 后内容渐进出现、重交互岛 `next/dynamic` 按需加载。
- 数据层：并行取数治瀑布（`Promise.all` / preload 模式）、利用 Request Memoization 与 Data Cache 避免重复请求、列表页先渲染首屏再补长尾。
- 资源层：`next/image`（自动 AVIF/WebP + 尺寸标注防 CLS）、`next/font` 自托管字体零布局抖动、`optimizePackageImports` 或直接换轻量包（moment→dayjs）。
- 传输层：开启 Brotli/gzip、静态资源指纹 + `Cache-Control: immutable`、`experimental.optimizeCss` 内联关键 CSS。
- 度量闭环：以 LCP/INP/CLS 为北极星指标，用 Lighthouse CI + 真实用户上报（web-vitals）双轨验证，优化必须有 before/after 数据。

```tsx
// app/product/[id]/page.tsx —— 并行取数 + 流式分层
import { Suspense } from 'react';

export default function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  // 关键信息与次要信息并行发起，避免瀑布
  const reviewsPromise = getReviews(id); // 不 await，先拿 promise
  return (
    <>
      <Suspense fallback={<GallerySkeleton />}>
        <Gallery id={id} />            {/* LCP 内容优先流式 */}
      </Suspense>
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews promise={reviewsPromise} /> {/* 次要内容后到 */}
      </Suspense>
    </>
  );
}

async function Reviews({ promise }) {
  const reviews = await promise; // 复用同一 promise，不会二次请求
  return reviews.map((r) => <ReviewCard key={r.id} {...r} />);
}
```
