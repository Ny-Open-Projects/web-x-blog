---
title: [NODE-411] Node 服务的请求体验证层（schema 校验与清洗）如何统一？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-411：请求体验证层统一
**答**:
- 验证目标三合一：安全（类型清洗防注入 NODE-354）、正确（业务规则）、友好（错误信息可定位到字段）。全部入参（query/body/headers/params）过 schema，不信任何输入。
- 实现：zod/ajv 装饰器或中间件化（route 定义 schema → 中间件 parse → ctx.state.parsed 传递——业务只用校验后的数据，原始 req.body 禁止直用）。
- 校验分层：结构校验（类型/必填/格式）、业务校验（唯一性/库存——依赖 DB，service 层）、长度与规模限制（数组长度/字符串长度/嵌套深度防 DoS）。
- 错误输出标准化：字段级错误列表 [{ path, code, message }]（NODE-410 信封），前端可直接映射到表单字段（ARC-384）。
- 附加清洗：字符串 trim、HTML 标签剥离（按字段声明）、枚举归一（大小写）——清洗规则声明在 schema（transform）而不是散在业务里。
```javascript
const BodySchema = z.object({
  name: z.string().trim().min(1).max(50),
  tags: z.array(z.string().max(20)).max(10).default([]),        // 规模限制防 DoS
  phone: z.string().regex(/^1\d{10}$/)
}).strict();                                                    // 未知字段拒绝（防注入）
const validate = (schema) => (ctx, next) => {
  const r = schema.safeParse(ctx.request.body);
  if (!r.success) return ctx.throw(400, { fieldErrors: r.error.issues });
  ctx.state.parsed = r.data;                                     // 业务只用 parsed
  return next();
};
```
