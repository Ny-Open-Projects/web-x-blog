---
title: [NODE-410] Node 服务的 API 响应标准化（信封/错误/分页）如何统一？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-410：API 响应标准化
**答**:
- 信封结构统一：成功 { data, meta }、错误 { error: { code, message, detail } }（NODE-032 错误码体系）；分页 meta 统一 { items, nextCursor, hasMore, total? }（NODE-400 cursor 协议）。
- 时间/金额/ID 标准化：时间 ISO8601 UTC（ARC-481）、金额整数分或字符串（ARC-482）、ID 字符串（防 JS Number 精度——雪花 ID 超 2^53）。
- 字段命名：camelCase（JS 生态一致）或按团队既有约定，转换收口在 DTO 层（NODE-359）。
- 空值语义：null（明确为空）vs 字段缺失（未实现/无权限）区分——文档写明（NODE-399）；列表空返回 [] 而非 null（防前端误判）。
- 一致性工程：响应 schema 用 zod 双向校验（出参也校验——防 service 层脏数据漏出）、序列化中间件统一（单测断言信封结构，lint 检查绕过）。
```javascript
// 统一响应中间件
app.use(async (ctx, next) => {
  try { await next(); if (ctx.body && !ctx.body.data) ctx.body = { data: ctx.body }; }
  catch (e) { ctx.status = e.httpStatus ?? 500;
    ctx.body = { error: { code: e.code ?? 'INTERNAL', message: publicMessage(e), detail: e.detail } }; }
});
// DTO 出参校验
function toDTO(goods) { const r = goodsSchemaOut.safeParse(goods); if (!r.success) throw new InternalDirtyData(r.error); return r.data; }
```
