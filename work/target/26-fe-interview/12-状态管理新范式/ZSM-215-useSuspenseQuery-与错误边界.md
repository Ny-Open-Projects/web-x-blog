---
title: [ZSM-215] useSuspenseQuery 和 ErrorBoundary 怎么配合成组管理
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-215：useSuspenseQuery 和 ErrorBoundary 怎么配合成组管理

**答**：
- useSuspenseQuery 把「加载中」抛给最近的 Suspense、「错误」抛给最近的 ErrorBoundary，组件内只剩成功态，逻辑大幅简化
- 配合 `throwOnError: true` 可以把普通 useQuery 的错误也抛给边界，实现跨组件统一错误 UI
- Suspense 边界的粒度 = 用户体验的骨架屏粒度；错误边界的粒度 = 崩溃隔离粒度，两者可以不对齐
- 注意：水合阶段 Suspense fallback 会造成 SSR/CSR 不一致，SSR 场景要么服务端预取要么接受首屏 fallback

```javascript
<ErrorBoundary fallbackRender={({ error, resetErrorBoundary }) => (
  <ErrorCard error={error} retry={resetErrorBoundary} />
)}>
  <Suspense fallback={<SkuSkeleton />}>
    <SkuPanel />   {/* 内部 useSuspenseQuery({ queryKey, queryFn, throwOnError: true }) */}
  </Suspense>
</ErrorBoundary>
```
