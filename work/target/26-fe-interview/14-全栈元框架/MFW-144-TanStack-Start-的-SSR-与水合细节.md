---
title: [MFW-144] TanStack Start 的 SSR 与水合细节是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-144：TanStack Start 的 SSR 与水合细节是什么？
**答**：
- SSR 管线：请求进来 → router 匹配 → loader 并行执行（server function 进程内直调）→ DehydrateRouter 把路由树状态（loader 数据、search params）序列化进 HTML → 客户端 hydration 时 Rehydrate 复水、不重跑 loader。
- 流式：loader 返回 promise 时配合 `Await`/Suspense 流式下发（与 RRv7 同机制）。
- 水合心智与 Next 不同：SSR 的全部组件都在客户端 bundle 里（无 RSC），水合成本 = 全组件树；换来的是单一渲染模型、没有 'use client' 边界焦虑。
- 降级开关：`ssr: false` 可整体变 SPA（router 保留），或按 route `ssr: false` 跳过 SSR——渐进策略和 RRv7 类似。

```tsx
// __root.tsx —— SSR 全局壳
import { createRootRouteWithContext, Outlet, HeadContent, Scripts } from '@tanstack/react-router';
import { DehydrateRouter } from '@tanstack/react-start';

export const Route = createRootRouteWithContext<{ queryClient: QueryClient }>()({
  head: () => ({ meta: [{ charSet: 'utf-8' }, { title: 'My App' }] }),
  component: RootLayout,
});

function RootLayout() {
  return (
    <html>
      <head><HeadContent /></head>
      <body>
        <Outlet />          {/* 路由树渲染（loader 已在服务端完成） */}
        <DehydrateRouter /> {/* 路由状态脱水进 HTML，复水的坐标 */}
        <Scripts />
      </body>
    </html>
  );
}
```

```ts
// 集成 TanStack Query：SSR prefetch + 复水
// loader: async () => {
//   const qc = getQueryClient();
//   await qc.prefetchQuery({ queryKey: ['product', id], queryFn: ... });
//   return { dehydratedState: dehydrate(qc) }; // query 缓存随路由脱水
// }
// 客户端 hydrate(qc, dehydratedState) -> useQuery 直接命中缓存不发请求
```
