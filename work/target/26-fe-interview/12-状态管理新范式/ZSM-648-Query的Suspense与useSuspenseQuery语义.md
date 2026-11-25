---
title: [ZSM-648] useSuspenseQuery：Suspense 化的数据获取语义与边界
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-648：useSuspenseQuery：Suspense 化的数据获取语义与边界

**答**：
- useSuspenseQuery 与 useQuery 的行为差异：数据未就绪时**向 React 抛 promise**（挂起组件树，外层 Suspense fallback 兜住），返回值的 data 保证非空（TS 上不再有 undefined）；错误由最近的 ErrorBoundary 接（不再有 isError 分支——错误路径与数据路径彻底分离）。
- 缓存语义不变：同样走 QueryCache（staleTime/gcTime/去重）。挂起期间 fetchStatus: fetching，恢复后正常渲染。refetch 触发的二次挂起：默认 `throwOnError` 配置下 refetch 失败会抛错误（不挂起），数据仍在——Suspense 只管「首载」，错误处理交给 error boundary + refetch。
- 适用边界：1) 适合「页面级数据」（路由段加载）——骨架语义天然匹配；2) 不适合「交互触发的局部刷新」（refetch 会绕过 Suspense 但 suspense 化的组件对 promise 更敏感）；3) 列表内嵌套子查询要每个子项一个 Suspense 边界，否则一个慢请求挂住整列表。
- 与 RSC 的关系：Next.js App Router 服务端 prefetch（`prefetchQuery` 在 server component）→ dehydrate 传给客户端 → useSuspenseQuery 首帧命中缓存不挂起——「服务端拉数据 + 客户端 Suspense 兜底」是标准组合。
- 追问钩子：useSuspenseQuery 的 keepPreviousData 场景（分页切换）——切换 key 会再次挂起（每个 key 独立挂起），要防闪烁得用 placeholderData 或把分页参数放 select 之外。

```javascript
import { useSuspenseQuery, useQueryErrorResetBoundary } from '@tanstack/react-query'
import { Suspense } from 'react'
import { ErrorBoundary } from 'react-error-boundary'

function TodoList({ userId }) {
  // data 保证存在（TS: Todo[]），挂起期间由父级 Suspense 兜底
  const { data, refetch } = useSuspenseQuery({
    queryKey: ['todos', userId],
    queryFn: () => api.getTodos(userId),
    staleTime: 30_000,
  })
  return <ul>{data.map((t) => <li key={t.id}>{t.title}</li>)}</ul>
}

// 标准包装：ErrorBoundary + Suspense + 错误重置
function Page({ userId }) {
  const reset = useQueryErrorResetBoundary()
  return (
    <ErrorBoundary
      onReset={reset.reset}
      fallbackRender={({ resetErrorBoundary }) => (
        <div>加载失败 <button onClick={resetErrorBoundary}>重试</button></div>
      )}
    >
      <Suspense fallback={<Skeleton />}>
        <TodoList userId={userId} />
      </Suspense>
    </ErrorBoundary>
  )
}

// 服务端预取组合（Next.js App Router）
// RSC: await queryClient.prefetchQuery(...); <HydrationBoundary state={dehydrate(...)}>
// 客户端 useSuspenseQuery 首帧命中缓存 → 不挂起直接渲染
```
