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

**边界与易错**：

- 类型出口写成值导入（`import { Router }`）而不是 `import type`：服务端 router 模块连同 DB/配置一起被打进前端 bundle，编译期类型安全换来运行时代码泄露。
- `output()` 只做推导与运行时校验，不做字段裁剪：仓储返回带 `password` 的对象照样流到前端，必须显式 `pick`。
- 跨仓发布类型包时版本漂移，报错出现在客户端调用处而不是服务端，容易往错误方向查。

**追问**：

1. 客户端 bundle 里到底会不会带服务端代码？→ 只要 `import type` 被 tsc 擦除且无副作用导入，就一行不落地，用 bundle 分析器验证。
2. 「本地类型通过、发布后运行时报错」怎么排查？→ 多半两端部署版本错配，比对构建 commit 与网关记录的契约版本。
3. zod 运行时校验失败算谁的错？→ 4xx 且带 issue 路径，前端应按 issue 改参数而不是重试；5xx 才是服务端问题。
