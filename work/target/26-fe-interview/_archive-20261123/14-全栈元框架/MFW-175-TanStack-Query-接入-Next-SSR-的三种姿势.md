---
title: [MFW-175] TanStack Query 接入 Next.js SSR 的三种姿势怎么选？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-175：TanStack Query 接入 Next.js SSR 的三种姿势怎么选？
**答**：
- 姿势一 `initialData`：服务端取数后以 props 传给客户端组件作为初始值。简单但**时间戳是服务端的**，会被 staleTime 判定立即过期（除非手动设 `dataUpdatedAt`），适合容忍立即 refetch 的场景。
- 姿势二 hydration 完整方案（推荐）：RSC 里 `dehydrate(queryClient)` 传给客户端，`useHydratedQueryClient` 复水。序列化含 query 状态与更新时间，staleTime 精确，且同 key 请求复用，不产生 SSR 与客户端双取。
- 姿势三 RSC prefetch：用 `queryClient.fetchQuery` 在服务端预热缓存再脱水，本质是姿势二的变体，适合「列表在 RSC、交互在客户端」混合页。
- App Router 注意点：QueryClient 要 per-request new（不能模块级单例，会跨请求串数据），用 `useState(() => new QueryClient())` 或 RSC 侧直接 new。
- 折衰 hydration 的 promise 会被序列化为已完成值，不要在 SSR 阶段放无限期 promise；错误态数据也要避免脱水（防错误复水后卡死）。

```javascript
// app/users/page.tsx（RSC）
import { dehydrate, HydrationBoundary, QueryClient } from '@tanstack/react-query';
export default async function Page() {
  const qc = new QueryClient(); // per-request 实例
  await qc.prefetchQuery({ queryKey: ['users'], queryFn: fetchUsers });
  return <HydrationBoundary state={dehydrate(qc)}><UsersList /></HydrationBoundary>;
}

// components/UsersList.tsx（客户端）
'use client';
export function UsersList() {
  const { data } = useQuery({ queryKey: ['users'], queryFn: fetchUsers, staleTime: 30_000 });
  return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>; // 复水后 30s 内不再发请求
}
```
