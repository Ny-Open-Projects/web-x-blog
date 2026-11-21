---
title: [NODE-262] tRPC 端到端类型安全的实现原理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-262：tRPC 端到端类型安全的实现原理？
**答**:
- 原理：零代码生成——服务端 procedure 的 TS 类型通过"类型导入"直接流到客户端（tsc 编译期串起两端），运行时只是 JSON-RPC（fetch/WS）。
- 对比：OpenAPI 代码生成（NODE-157 有产物依赖）vs tRPC（Monorepo 内类型直接共享，ARC-024 源码直引策略）。
- 边界：类型安全只在同一 TS 工程内（跨仓需要发布类型包）；多语言客户端不适用（那是 GraphQL/OpenAPI 场景）。
- 配套：input 校验 zod（运行时安全）+ output 类型推导（编译期安全）。

```typescript
// server（BFF）
const router = t.router({
  getOrder: publicProcedure
    .input(z.object({ id: z.string() }))
    .output(z.object({ id: z.string(), price: z.number() }))
    .query(({ input }) => orderRepo.get(input.id)),    // zod 校验 + 类型推导
});
export type Router = typeof router;                    // 类型出口
// client（前端，同一 monorepo）
const order = await trpc.getOrder.query({ id: '1' });  // order.price: number —— 编译期直达
// 原理一句话：Router 类型 → import('...') 的 infer 链 → 客户端调用签名 = 服务端签名
```
