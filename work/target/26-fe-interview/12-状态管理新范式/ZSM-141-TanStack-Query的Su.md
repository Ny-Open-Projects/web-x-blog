---
title: [ZSM-141] TanStack Query 的 Suspense 模式怎么用？throwOnError 和 ErrorBoundary 怎么配合？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-141：TanStack Query 的 Suspense 模式怎么用？throwOnError 和 ErrorBoundary 怎么配合？
**答**：
- `useSuspenseQuery` 用 Promise 集成 React Suspense：数据未就绪抛 Promise 给最近的 Suspense 兜 loading，组件内代码里 data 永远非 undefined（TS 类型直接有值），消掉一堆判空。
- 错误路径：默认 error 不会抛给 ErrorBoundary，要配 `throwOnError: true`（或按错误类型函数式抛），把「渲染期错误」交给最近的 ErrorBoundary 展示。
- 分级边界：页面级 Suspense 兜首屏、模块级 Suspense 兜局部，ErrorBoundary 同理分级；401 类错误不要 throw，走重定向逻辑。
- 收益：组件逻辑退化成「纯成功态渲染」，加载/错误 UI 全部上提到边界层，代码量与心智负担显著下降。

```javascript
import { useSuspenseQuery } from '@tanstack/react-query'

function GoodsSection({ id }) {
  // data 类型不含 undefined，无需判空
  const { data: goods } = useSuspenseQuery({
    queryKey: ['goods', id],
    queryFn: () => api.goods(id),
    throwOnError: (error) => error.status !== 401,  // 401 走重定向，其余抛给边界
  })
  return <Detail goods={goods}/>
}

// 页面组合：分级边界
export function Page({ id }) {
  return (
    <ErrorBoundary fallbackRender={({ error, resetErrorBoundary }) =>
      <ErrorView error={error} retry={resetErrorBoundary}/>}>
      <Suspense fallback={<DetailSkeleton/>}>
        <GoodsSection id={id}/>
      </Suspense>
    </ErrorBoundary>
  )
}
```
