---
title: [MFW-181] 元框架里请求级上下文怎么传递（cache() 与 AsyncLocalStorage）？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-181：元框架里请求级上下文怎么传递（cache() 与 AsyncLocalStorage）？
**答**：
- 需求：一个 HTTP 请求里，深层函数要拿到 traceId/当前用户/locale，但层层透传参数太丑——需要「请求级全局」。
- 方案一 React `cache()`：只在 RSC 渲染生命周期内有效，按函数入参做请求级记忆化，适合取数去重、派生数据缓存；Server Action 内不可用（不同执行域）。
- 方案二 `AsyncLocalStorage`（Node AsyncContext）：跟随异步调用链，在 Route Handler、Action、load 函数里都能拿到当前请求上下文；Next 提供 `unstable_after` 之外的官方模式（如 OpenTelemetry 集成）。
- 关键坑：ALS 上下文**不能跨 await 边界之外的回调**（如 setTimeout、事件监听器里读不到）；流式渲染中 Suspense 分段执行的时机要注意上下文仍需可用。
- SvelteKit/Nuxt 对应物：事件locals（`event.locals`）与 Nuxt 的 `useRequestEvent`/Nitro 上下文——本质都是把请求上下文挂在执行域对象上，框架负责传递。

```javascript
import { AsyncLocalStorage } from 'node:async_hooks';
const requestContext = new AsyncLocalStorage();

// handle hook（框架入口）里建立上下文
export async function handle({ event, resolve }) {
  return requestContext.run({ traceId: event.request.headers.get('x-trace-id') }, () =>
    resolve(event),
  );
}

// 任意深层函数（无需层层传参）
export function log(msg) {
  const { traceId } = requestContext.getStore();
  console.log(`[${traceId}] ${msg}`);
}
```