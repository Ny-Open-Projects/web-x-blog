---
title: [R19-145] TanStack Query 的进阶模式有哪些？queryClient 命令式操作、依赖查询、无限查询怎么写？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-145：TanStack Query 的进阶模式有哪些？queryClient 命令式操作、依赖查询、无限查询怎么写？
**答**：
- 命令式操作：在事件/非组件代码里用 `queryClient.invalidateQueries` / `setQueryData` / `fetchQuery`，而不是只依赖组件内 useQuery。
- 依赖查询：`enabled: !!userId` 让前置数据就绪才发起，配合 `placeholderData: keepPreviousData` 翻页不闪 loading。
- 无限查询：`useInfiniteQuery` + getNextPageParam，页面数据按 pages 数组返回，配合 IntersectionObserver 触发 fetchNextPage。
- 命令式 fetchQuery 常用于"提交前预热"和"跨页面预取"。

```tsx
// users-page.tsx —— TanStack Query 进阶三模式
import {
  useQuery, useInfiniteQuery, useQueryClient, useMutation,
  keepPreviousData,
} from '@tanstack/react-query';
import { useEffect, useRef, useState } from 'react';

// 模式一：依赖查询 + 翻页不闪烁
export function UserOrders({ userId }: { userId?: number }) {
  const [page, setPage] = useState(1);
  const orders = useQuery({
    queryKey: ['orders', userId, page],
    queryFn: () => fetch(`/api/orders?uid=${userId}&page=${page}`).then(r => r.json()),
    enabled: !!userId,                       // userId 就绪才请求
    placeholderData: keepPreviousData,       // 换页保留旧数据，不闪 loading
  });
  // ...
}

// 模式二：无限查询 + IntersectionObserver
export function FeedList() {
  const sentinelRef = useRef<HTMLDivElement>(null);
  const feed = useInfiniteQuery({
    queryKey: ['feed'],
    queryFn: ({ pageParam }) =>
      fetch(`/api/feed?cursor=${pageParam ?? ''}`).then(r => r.json()),
    initialPageParam: 0,
    getNextPageParam: (last) => last.nextCursor ?? undefined, // null 表示没有更多
  });

  useEffect(() => {
    const io = new IntersectionObserver(([e]) => {
      if (e.isIntersecting && feed.hasNextPage && !feed.isFetchingNextPage) {
        feed.fetchNextPage();
      }
    }, { rootMargin: '200px' });
    if (sentinelRef.current) io.observe(sentinelRef.current);
    return () => io.disconnect();
  }, [feed.hasNextPage, feed.isFetchingNextPage, feed.fetchNextPage]);

  return (
    <>
      {feed.data?.pages.map(page =>
        page.items.map((it: any) => <div key={it.id}>{it.title}</div>)
      )}
      <div ref={sentinelRef}>{feed.isFetchingNextPage ? '加载中...' : ''}</div>
    </>
  );
}

// 模式三：queryClient 命令式操作 —— 提交前预热 / 跨组件失效
export function useUserCommands() {
  const qc = useQueryClient();

  const createOrder = useMutation({
    mutationFn: (payload: { userId: number }) =>
      fetch('/api/orders', { method: 'POST', body: JSON.stringify(payload) }),
    onSuccess: (_data, vars) => {
      // 失效与该用户相关的所有订单查询，列表自动重新拉取
      qc.invalidateQueries({ queryKey: ['orders', vars.userId] });
    },
  });

  // 预取：hover 用户行时提前拉详情，进入详情页零等待
  function prefetchUser(userId: number) {
    qc.fetchQuery({
      queryKey: ['user', userId],
      queryFn: () => fetch(`/api/users/${userId}`).then(r => r.json()),
      staleTime: 30_000,
    });
  }
  // 也可以直接写缓存：qc.setQueryData(['user', 1], cachedUser)
  return { createOrder, prefetchUser };
}
```
