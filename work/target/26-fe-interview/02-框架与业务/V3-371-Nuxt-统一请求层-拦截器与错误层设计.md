---
title: [V3-371] Nuxt 下如何设计统一请求层（拦截器 + 错误处理）？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-371：Nuxt 下如何设计统一请求层（拦截器 + 错误处理）？
**答**：
- 双环境兼容：服务端用 useFetch/$fetch（ofetch，自动 JSON、重试可配），客户端复用同一封装但可挂 loading/toast 拦截。
- 拦截器分层：认证层（服务端从 cookie/session 读 token 透传 Authorization；客户端从存储读）、埋点层（耗时与状态码上报）、错误规范化层（业务码 → 统一 AppError）。
- 错误处理策略：useAsyncData 的 error 交给页面级 error.vue / createError(404)；Server API 内部 throw createError 保持状态码语义。
- 失败重试：ofetch retry 对幂等 GET 开启，POST 不重试（防重复下单）；网络层错误与服务端 5xx 分开埋点。
- 落地形态：composable `useApi()` 返回增强版 useFetch，业务层禁止裸 $fetch 散落。
```javascript
export function useApi<T>(url, opts) {
  return useFetch<T>(url, {
    ...opts,
    retry: opts.method === 'GET' ? 2 : 0,
    onResponseError: ({ response }) => track('api_error', url, response.status)
  })
}
```
