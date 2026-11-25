---
title: [903] QueryClient 在大型应用的默认配置怎么分层
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 配置]
type: 面试题
---

## 903：QueryClient 在大型应用的默认配置怎么分层

**答**：
- 分层默认值：全局默认（staleTime 30s、retry 2、refetchOnWindowFocus false——保守基线）-> 域级覆盖（用户资料 staleTime 5min、行情数据 staleTime 0+refetchInterval 5s）-> 单 query 覆盖（关键页面 gcTime 缩短）——三层配置防止「每个 useQuery 都带一堆参数」的重复。
- gcTime 与内存：长列表 SPA 的缓存堆积是内存事故源——按路由卸载时 removeQueries 定向清理域级缓存，或 gcTime 按域分级。
- 网络模式：弱网场景 offlineFirst（先缓存后网络）用于读多写少页面；mutation 默认 pauseOffline 队列化。
- 追问钩子：为什么全局默认 staleTime 不能是 0（默认值）？——0 意味着每次挂载/聚焦都请求，大型应用等于请求风暴；默认值必须保守，实时性按域单独放开。

```ts
const qc = new QueryClient({
  defaultOptions: { queries: { staleTime: 30_000, retry: 2,
    refetchOnWindowFocus: false } },
  queryCache: new QueryCache({ onError: e => reporter.capture(e) }),
});
// 域级：useQuery({ queryKey: userKeys.all, staleTime: 5 * 60_000, ... })
```

