---
title: [MFW-865] TanStack Start 的 loader 缓存怎么和 TanStack Query 缓存桥接
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-865：TanStack Start 的 loader 缓存怎么和 TanStack Query 缓存桥接

**答**：
- 结论：Start 的 loader 负责首屏 SSR 数据，Query 负责交互后的客户端缓存；桥接 = SSR 时 prefetchQuery + dehydrate 注入 HTML，客户端 hydrate 避免重复请求。
- 落地：loader 里 prefetchQuery 后 dehydrate；客户端 HydrationBoundary 复水；两端 staleTime 对齐，避免服务端认为新鲜、客户端立即重取。
- 追问钩子：gcTime 不一致会怎样？——服务端产物留太久可能泄露数据，客户端太短则频繁重取。

```javascript
// loader：预取并脱水
export const Route = createFileRoute('/posts')({
  loader: async ({ context }) => {
    await context.queryClient.prefetchQuery({
      queryKey: ['posts'], queryFn: () => db.posts.list()
    });
  },
  component: () => <HydrationBoundary state={dehydrate(context.queryClient)}>
    <Posts/>
  </HydrationBoundary>
});
// 客户端组件：复水缓存，不重复发请求
function Posts() {
  const { data } = useQuery({ queryKey: ['posts'], queryFn: fetchPosts, staleTime: 30_000 });
  return <List data={data}/>;
}
```
