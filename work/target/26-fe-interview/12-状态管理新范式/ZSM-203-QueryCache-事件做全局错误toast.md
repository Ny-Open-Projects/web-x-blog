---
title: [ZSM-203] 怎么用 QueryCache 事件做全局错误 toast 而不是每个组件写 onError
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-203：怎么用 QueryCache 事件做全局错误 toast，而不是每个组件写 onError

**答**：
- v5 移除了 queries 的全局 onError 回调，统一改为在 `new QueryClient({ queryCache: new QueryCache({ onError }) })` 上订阅事件
- onError 能拿到 query 对象，通过 `query.meta` 标记「这条查询要不要 toast」，避免轮询类静默查询刷屏
- MutationCache 同理，`mutation.meta` 可传自定义文案；4xx 与 5xx 分级处理
- 事件层只做横切关注点（toast/埋点/Sentry），组件层仍可用 error 状态做局部 UI，两层不冲突

```javascript
import { QueryClient, QueryCache, MutationCache } from '@tanstack/react-query'
import { toast } from './toast'

export const queryClient = new QueryClient({
  queryCache: new QueryCache({
    onError: (error, query) => {
      if (query.meta?.silent) return                     // 静默查询不 toast
      if (error.status === 401) return redirectLogin()   // 401 走登录
      toast.error(error.message)
    },
  }),
  mutationCache: new MutationCache({
    onError: (error, _vars, _ctx, mutation) => {
      toast.error(mutation.options.meta?.errorMessage ?? '操作失败')
    },
  }),
})

// 查询侧用 meta 声明行为，而不是散落 onError
useQuery({ queryKey: ['stock', id], queryFn: fetchStock, meta: { silent: true } })
```
