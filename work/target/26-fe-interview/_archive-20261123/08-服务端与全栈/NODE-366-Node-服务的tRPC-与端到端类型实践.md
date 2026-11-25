---
title: [NODE-366] Node 服务的 tRPC 与端到端类型安全实践如何落地？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-366：tRPC 与端到端类型安全实践
**答**:
- 价值：前后端同仓库（Monorepo）时，接口签名从路由定义直接推导到客户端调用——改字段前端编译期报错，消灭契约漂移（对比 OpenAPI 生成：类型生成有滞后与失真）。
- 实践结构：router 按域拆分（goods/trade）+ 中间件（鉴权注入 ctx.user、日志、限流）+ 输入校验 zod（schema 即校验即类型）；错误结构统一（TRPCError code 映射 HTTP 状态）。
- 边界：跨仓库/多语言场景 tRPC 不适用（回退 OpenAPI 契约，ARC-162）；非 TS 客户端（小程序原生）需要生成层或放弃。
- 性能：批处理链接（batching link 合并并发请求）、订阅（WS 链接）按需开启；大对象输出注意序列化成本。
- 演进：破坏性变更依赖 TS 编译暴露——但客户端发版节奏不同时仍需服务端兼容旧字段（类型安全 ≠ 部署兼容），双写期不可避免。
```typescript
// tRPC 路由与调用
const goodsRouter = t.router({
  detail: t.procedure.input(z.object({ id: z.string() })).query(async ({ input }) =>
    svc.getGoods(input.id))
});
// 客户端（同仓库）：trpc.goods.detail.useQuery({ id }) —— 参数与返回全自动推导
```
