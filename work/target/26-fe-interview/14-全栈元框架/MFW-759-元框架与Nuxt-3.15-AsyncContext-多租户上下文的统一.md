---
title: [MFW-759] Nuxt AsyncContext 多租户上下文
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-759：Nuxt AsyncContext 多租户上下文

**答**:
- Nuxt 的请求上下文：1) **useRequestEvent**（Nuxt composable——获取 H3 事件（Node req/res 的 Nuxt 封装）；2) **AsyncLocalStorage**（Node 的 ALS——Nuxt 底层用 ALS 传递请求上下文（useRequestEvent 的实现基础——RBL-657 ALS 的 Nuxt 版）；3) **多租户上下文**：ALS 携带 tenantId → DB 查询/缓存键/日志全链路注入（RBL-519 的 Nuxt 实现）。
- Nitro 的上下文传递：Nitro 的事件上下文（event.context——H3 事件的上下文对象——请求级数据存储）；「Nitro event.context = 请求级 ALS」的等价物。
- 追问钩子：为什么「Nitro event.context」比「手动传递 tenantId」更安全？——手动传参 = 每个函数都要接收和转发 tenantId（遗漏 = 串租户——RBL-657 的遗漏风险）；ALS/event.context = 自动注入（全链路隐式可用——不可遗漏）；「上下文的隐式传播」消除「手动传递的遗漏风险」：db 查询/缓存/日志从 context 取租户而非手动参数——与 RBL-519 的 ALS 多租户方案一致。

```typescript
// Nitro event.context：请求级上下文
// server/middleware/tenant.ts
export default defineEventHandler((event) => {
  const host = getRequestHost(event);
  const tenant = hostToTenant(host);
  event.context.tenant = tenant;                         // 注入上下文
});
// server/api/data.get.ts
export default defineEventHandler(async (event) => {
  const tenant = event.context.tenant;                   // 自动获取——不可遗漏
  return await db.$queryRaw`SELECT * FROM data WHERE tenant_id = ${tenant}`;
});
// Nuxt composable：useRequestEvent
// composables/useTenant.ts
export function useTenant() {
  const event = useRequestEvent();                       // Nuxt 的请求上下文
  return event?.context.tenant ?? null;
}
// RSC/SSR 页面的使用
// pages/[tenant]/index.vue
const tenant = useTenant();                              // SSR 渲染时可用
```
