---
title: [911] TanStack Query 大型应用的错误处理分层
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 错误处理]
type: 面试题
---

## 911：TanStack Query 大型应用的错误处理分层

**答**：
- 三层错误处理：全局层（queryCache onError——统一上报/401 跳登录/网络错误 toast）、域层（特定域的重试策略——支付域不自动重试防重复下单）、组件层（isError 分支渲染 + error boundary 兜渲染崩溃）。
- 重试策略分类：网络错误指数退避重试、业务错误（4xx）不重试（快速失败）、401 全局拦截（单飞刷新 token 后重放）。
- 错误结构化：服务端错误统一 { code, message, retriable }——queryFn 里归一化后抛出，下游按 retriable 决定重试，避免裸 string 判断。
- 追问钩子：错误状态会污染缓存吗？——不会（error 不写 data），失败不缓存重试结果（下次挂载重试）；错误缓存需自定义（一般不需要）。

```ts
const qc = new QueryClient({
  queryCache: new QueryCache({ onError: err => {
    if (err.code === 401) return redirectToLogin();
    if (err.retriable) return;                    // 交给 retry 策略
    toast.error(err.message);
  } }),
  defaultOptions: { queries: {
    retry: (count, err) => err.retriable && count < 3,
    retryDelay: a => Math.min(1000 * 2 ** a, 15000),
  } },
});
```

