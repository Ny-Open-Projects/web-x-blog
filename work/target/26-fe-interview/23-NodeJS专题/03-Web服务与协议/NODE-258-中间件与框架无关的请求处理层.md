---
title: [NODE-258] 中间件与框架无关的请求处理层？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-258：中间件与框架无关的请求处理层？
**答**:
- 问题：业务逻辑写死在 Koa ctx/Fastify reply 上 → 框架迁移成本高。
- 方案：框架适配层（薄）+ 框架无关的 handler 层——handler 收到的是纯 Input（method/headers/body/user），返回 Result（status/body）；Koa/Fastify 各写 20 行适配。
- 好处：单测直接调 handler（无框架 mock）、迁移只改适配层、跨框架复用（BFF 迁 Fastify）。
- 与 DP 模式呼应：适配器模式（DP-204 axios adapter 同款思想）在服务端的应用。

```typescript
// 框架无关 handler
interface HttpInput { method: string; path: string; headers: Record<string, string>; body: unknown; user?: User }
interface HttpResult { status: number; body: unknown }
// 业务层（纯函数 + DI）
export async function createOrder(input: HttpInput, deps: { orderRepo: OrderRepo }): Promise<HttpResult> {
  if (!input.user) return { status: 401, body: { code: 'UNAUTH' } };
  const order = await deps.orderRepo.create(input.body as OrderDto);
  return { status: 200, body: order };
}
// Koa 适配（20 行）
router.post('/orders', async (ctx) => {
  const r = await createOrder({ method: 'POST', path: ctx.path, headers: ctx.headers,
    body: ctx.request.body, user: ctx.state.user }, deps);
  ctx.status = r.status; ctx.body = r.body;
});
// 单测：await createOrder(fakeInput, fakeDeps) —— 无框架依赖
```
