---
title: [NODE-050] tRPC 的概念是什么？它如何实现端到端类型安全？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-050：tRPC 的概念是什么？它如何实现端到端类型安全？
**答**：
- tRPC：**TypeScript 原生 RPC 框架**——不需要 schema、不需要 codegen，直接把服务端函数的类型"导入"到客户端：`client.greeting.query()` 的参数与返回值类型完全由服务端推断，任何改动前端编译期立刻报错。
- 与 GraphQL/tRPC+REST 的区别：REST 用 OpenAPI 描述后手工生成类型（可能漂移），GraphQL 需要 SDL + codegen，tRPC 的类型即实现本身（TS 类型在编译期共享，运行时仍是轻量 HTTP/JSON）。
- 适用边界：**前后端都是 TS 的同仓库（monorepo）场景**；客户端非 TS（小程序原生、App）则不适用，退回 OpenAPI/GraphQL。路由用 procedure（`publicProcedure`/`protectedProcedure`）+ input 校验（zod）。

```typescript
// server.ts —— BFF 端定义 procedure
import { initTRPC } from '@trpc/server';
import { z } from 'zod';
import { createHTTPServer } from '@trpc/server/adapters/standalone';

const t = initTRPC.create();
const publicProcedure = t.procedure;
const router = t.router;

const appRouter = router({
  getUser: publicProcedure
    .input(z.object({ id: z.string().uuid() }))   // 输入校验 + 类型推导
    .query(async ({ input }) => {                  // 返回值类型自动推断
      return db.users.find(input.id);              // { id: string, name: string, age: number }
    }),
  createUser: publicProcedure
    .input(z.object({ name: z.string().min(1) }))
    .mutation(async ({ input }) => db.users.create(input)),
});
export type AppRouter = typeof appRouter;          // 导出类型（不含实现，不泄露服务端代码）

createHTTPServer({ router: appRouter, createContext: () => ({}) }).listen(3000);
```

```typescript
// client.ts —— 前端：零 codegen 的端到端类型
import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';
import type { AppRouter } from '../server';        // 仅导入类型，编译后消失

const trpc = createTRPCProxyClient<AppRouter>({
  links: [httpBatchLink({ url: 'http://localhost:3000' })],
});

const user = await trpc.getUser.query({ id: 'not-a-uuid' });
// TS 报错：字符串不符合 uuid 格式 → 编译期拦截，而不是线上 500

const user2 = await trpc.getUser.query({ id: '3f8a...-uuid' });
user2.name.toUpperCase();  // name 被推断为 string；改为 user2.emai 会直接编译报错

// 多个请求自动合并为一个 HTTP 批量调用（httpBatchLink），减少往返
const [a, b] = await Promise.all([
  trpc.getUser.query({ id: 'a1' }),
  trpc.getUser.query({ id: 'a2' }),
]);
```
