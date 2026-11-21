---
title: [MFW-150] TanStack Start 和 Next 的数据加载心智模型差在哪？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-150：TanStack Start 和 Next 的数据加载心智模型差在哪？
**答**：
- Next（RSC）：**数据活在服务端组件里**——取数与渲染一体，客户端拿到的是渲染结果；缓存是框架的（四层缓存栈）；客户端状态获取要经过 RSC→props/Context 或第三方库，链路绕。
- TanStack Start：**数据活在缓存里**（TanStack Query）——组件订阅缓存，loader 只是 prefetch 加速首屏；失效/乐观更新/重试全部复用 Query 语义，SPA 与 SSR 心智完全一致。
- 关键差异点：① 谁是真相源（Next：服务端渲染流；Start：客户端缓存）；② 失效模型（Next：revalidateTag/Path + 导航重渲染；Start：invalidateQueries + refetch）；③ 实时性（Start 天然兼容轮询/订阅型 useQuery；Next 要流式 RSC 或外部库）。
- 实战判断：数据交互重、多视图共享同一份数据（如 IM、仪表盘）→ Start/Query 模型更顺；内容展示 + 服务端聚合 → Next RSC 更顺。

```tsx
// ===== Next：RSC 模型 =====
// app/products/page.tsx（服务端组件）
// export default async function Page() {
//   const items = await db.product.findMany();   // 取数即渲染
//   return <List items={items} />;               // 客户端收到渲染结果
// }

// ===== TanStack Start：缓存模型 =====
export const Route = createFileRoute('/products')({
  loader: ({ context: { queryClient } }) =>
    // loader 只是 prefetch：首屏加速
    queryClient.ensureQueryData({
      queryKey: ['products'],
      queryFn: fetchProducts,
      staleTime: 30_000,
    }),
});

function ProductsList() {
  // 组件订阅缓存：SSR 数据复水命中 / 客户端导航命中 / 过期自动 refetch
  const { data, isFetching } = useQuery({ queryKey: ['products'], queryFn: fetchProducts });

  // 同 key 其他视图免费共享：购物车角标改数据只 invalidate 一次
  // queryClient.invalidateQueries({ queryKey: ['products'] })
  return <List items={data!} fetching={isFetching} />;
}
```
