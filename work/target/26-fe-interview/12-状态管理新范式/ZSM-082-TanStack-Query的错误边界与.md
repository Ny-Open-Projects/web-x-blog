---
title: [ZSM-082] TanStack Query 的错误状态怎么分层处理？组件内 toast、页面级 ErrorBoundary、全局兜底怎么分工？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-082：TanStack Query 的错误状态怎么分层处理？组件内 toast、页面级 ErrorBoundary、全局兜底怎么分工？
**答**：
- 第一层组件内：isError + error 渲染局部重试按钮，可恢复的错误就地消化。
- 第二层页面级 ErrorBoundary：配合 `throwOnError: true` 让查询错误抛出，由路由级 EB 兜「整块内容不可用」。
- 第三层全局：QueryCache onError 统一上报（Sentry）+ 全局 toast（如网络断开横幅），业务组件不重复弹窗。
- 分层原则：可重试的可恢复错误不升级、影响整页的错误必须升级、上报与 UI 提示分离（上报在 cache 层，提示在 UI 层）。

```javascript
const qc = new QueryClient({
  queryCache: new QueryCache({
    onError: (e) => {
      Sentry.captureException(e)
      if (!navigator.onLine) toast.error('网络断开，正在重试…')
    },
  }),
  defaultOptions: { queries: { throwOnError: false, retry: 2 } },
})
// 组件内
if (isError) return <ErrorState onRetry={refetch} />
```
