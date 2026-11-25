---
title: [ZSM-628] TanStack Query 的 retryer：重试、退避与请求取消的内部实现
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-628：TanStack Query 的 retryer：重试、退避与请求取消的内部实现

**答**：
- retryer 是 Query.fetch 的执行引擎，包住 queryFn，负责：重试策略（次数/条件）、指数退避、取消（AbortSignal）、pause（离线暂停，networkMode）。它是 promise 分发器的角色——多个 observer 共享同一次 fetch 的 Promise。
- 重试决策：`retry: 3`（默认 3）或函数 `(failureCount, error) => boolean`；**4xx 类错误默认不重试**（v5 对 401/403/404 有内置判断）——重试只会放大必然失败。`retryDelay: exponentialBackoff(min(100ms, 30s))` 或自定义函数拿到 attempt 计数做全抖动退避。
- 取消实现：retryer 把 `AbortSignal` 传给 queryFn（v5 的 `signal` 参数），fetch 内部 signal.abort 时 promise reject（isCancelError 判定）；同时 retryer 的 `cancel` 主动取消——组件卸载、queryKey 变化、invalidate 时可能触发。**取消只影响「状态不写入」，不影响服务端**（服务器仍可能完成）。
- networkMode：'online'（离线暂停，监听 online 事件恢复）/ 'always' / 'offlineFirst'（离线先试一次）。暂停实现是 retryer 内的 pause 状态 + visibility/online 事件回调。
- 追问钩子：重试期间 `failureCount` 逐次递增暴露给 UI（重试提示），`failureReason` 带上一次错误详情。

```javascript
// retryer 骨架（v5 简化）
function createRetryer(config) {
  let failureCount = 0
  let cancelled = false
  let promiseResolve, promiseReject
  const promise = new Promise((r, j) => { promiseResolve = r; promiseReject = j })
  const signal = config.signal   // Query 构建的 AbortController

  async function run() {
    try {
      const data = await config.queryFn({ signal, queryKey: config.queryKey, meta: config.meta })
      if (cancelled) return   // 取消后结果作废
      promiseResolve(data)
    } catch (error) {
      if (cancelled || config.canFetchOffline?.(error) === false) return promiseReject(error)
      // 重试决策：次数 + 4xx 跳过
      if (isCancelledError(error)) return
      if (error.status === 401 || error.status === 404) return promiseReject(error)
      if (failureCount >= config.retry) return promiseReject(error)
      failureCount++
      const delay = config.retryDelay(failureCount, error)   // 指数退避
      setTimeout(run, delay)
    }
  }

  return {
    promise,
    cancel(quiet) {
      cancelled = true
      signal.abort()                          // 通知 fetch 层
      quiet ? promise.catch(() => {}) : promiseReject(createCancelledError())
    },
    continueRetry: run,                        // online 恢复时继续
  }
}

// queryFn 侧：消费 signal
useQuery({
  queryKey: ['todos', id],
  queryFn: ({ signal }) => fetch(`/api/todos/${id}`, { signal }).then((r) => r.json()),
  retry: (failureCount, error) => failureCount < 3 && error.status >= 500,   // 5xx 才重试
})
```
