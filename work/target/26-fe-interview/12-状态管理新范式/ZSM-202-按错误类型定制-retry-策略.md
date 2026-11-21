---
title: [ZSM-202] 重试策略怎么按错误类型区分4xx不重试
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-202：重试策略怎么按错误类型区分，4xx 不重试

**答**：
- retry 支持函数：`(failureCount, error) => boolean`，按错误语义决定是否继续，而不是无脑次数重试
- 原则：5xx/网络错误/超时可重试（幂等查询），401/403/404/422 属于确定性失败，重试只会放大流量
- 重试次数用尽后 error 才落到组件，可配合 `retryDelay` 指数退避，避免雪崩
- mutation 默认不重试（非幂等），需要时用乐观更新 + 后端幂等键兜底，而不是前端重试

```javascript
import { QueryClient } from '@tanstack/react-query'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: (failureCount, error) => {
        const status = error?.status ?? error?.response?.status
        if (status && status >= 400 && status < 500) return false  // 确定性失败
        if (error?.name === 'AbortError') return false             // 取消不重试
        return failureCount < 3                                    // 网络/5xx 最多 3 次
      },
      retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30_000), // 指数退避
    },
    mutations: { retry: 0 },  // mutation 默认不重试
  },
})
```
