---
title: [NODE-620] Node 服务的请求上下文贯穿（身份/租户/灰度/预算统一）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-620：请求上下文贯穿
**答**:
- 统一上下文：一个请求携带的全部横切信息（身份/租户/灰度标签/deadline/trace/采样决策/链路预算——分散实现 vs ALS 统一（NODE-421）——统一 RequestCtx 对象）。
- 构建与传播：网关/入口构建（解析所有头 → ctx 对象——结构 schema 化）、ALS 存储（全链路隐式可用）、出站传播（internalCall 统一注入对应头——NODE-497 透传封装）、Worker/MQ 传播（显式序列化 ctx——worker.postMessage(ctx)）。
- 上下文消费：logger 自动注入（NODE-421）、限流/降级决策引用（按 ctx.tier/gray）、审计记录（ctx.uid——操作留痕）。
- 类型安全：RequestCtx 类型单源（各字段 schema 校验——入口构建时校验，下游可信）、缺失检测（必填字段缺失 fail fast——上下文完整性）。
- 收益：横切逻辑一处实现（新增横切维度只改构建与传播——不散改业务）、排障信息完整（日志/trace 全带上下文——ARC-533）。
```javascript
// RequestCtx 统一
const CtxSchema = z.object({ uid: z.string(), tenant: z.string(), gray: z.string().default('stable'),
  deadlineMs: z.number(), traceId: z.string(), sampled: z.boolean() });
app.use((req, res, next) => als.run(CtxSchema.parse(buildCtx(req)), next));  // 入口构建+校验
// 出站：internalCall(url) 自动注入 { x-uid, x-gray, x-deadline-ms, traceparent }
```
