---
title: [ZSM-081] TanStack Query 的重试策略怎么设计？哪些错误不该重试？指数退避怎么写？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-081：TanStack Query 的重试策略怎么设计？哪些错误不该重试？指数退避怎么写？
**答**：
- retry 可设数字或函数 `(failureCount, error) => boolean`；默认 3 次、指数退避（1s/2s/4s，max 30s）。
- 不该重试的：4xx 客户端错误（401 未授权、403 无权、422 参数错）——重试只会刷错误；5xx/网络错误/超时适合重试。
- 按错误类型分流：fetch 封装里给 error 打标记（e.status），retry 函数读取；401 触发登出/刷新 token 流程，不进重试。
- mutation 默认不重试（写操作重试可能重复下单），确需重试必须幂等（幂等键）。

```javascript
useQuery({
  queryKey: ['goods'],
  queryFn: api.goods,
  retry: (failureCount, error) => {
    if (error.status === 401 || error.status === 403 || error.status === 422) return false
    return failureCount < 3 // 5xx/网络错误最多 3 次
  },
  retryDelay: attempt => Math.min(1000 * 2 ** attempt, 30_000), // 指数退避上限 30s
})
```
