---
title: [ZSM-107] SWR 的错误怎么处理？和 TanStack Query 的 retry 机制差在哪？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-107：SWR 的错误怎么处理？和 TanStack Query 的 retry 机制差在哪？
**答**：
- SWR 把 error 作为返回值暴露（`{ data, error }`），配合 `onError` / `onErrorRetry` 回调处理；没有 Query 那种内置指数退避，默认 `onErrorRetry` 只做一次延迟 5s 的重试，策略要自己写。
- 自定义重试：onErrorRetry(retryCount, error, config, revalidate, opts) 里用 `Math.min(1000 * 2 ** retryCount, 30000)` 做指数退避，`opts.maxRetryCount` 控上限，4xx 类永久错误应直接 return 不重试。
- 错误也进缓存：失败后 data 仍可能是旧值，error 与 data 同时存在时 UI 要「降级展示旧数据 + 提示刷新」，这是 SWR 典型考点。
- 全局兜底用 `<SWRConfig value={{ onError: report }}> `统一上报，组件层再按业务决定展示方式。

```javascript
import useSWR from 'swr'

function Goods({ id }) {
  const { data, error } = useSWR(['/api/goods', id], fetcher, {
    onErrorRetry: (error, key, config, revalidate, { retryCount }) => {
      if (error.status === 404) return                 // 永久错误不重试
      if (retryCount >= 3) return                      // 上限 3 次
      setTimeout(() => revalidate({ retryCount }),
        Math.min(1000 * 2 ** retryCount, 30000))       // 指数退避
    },
  })
  if (error && data) return <StaleBanner data={data}/> // 有旧值先降级
  if (error) return <ErrorView error={error}/>
  if (!data) return <Spinner/>
  return <Detail data={data}/>
}
```
