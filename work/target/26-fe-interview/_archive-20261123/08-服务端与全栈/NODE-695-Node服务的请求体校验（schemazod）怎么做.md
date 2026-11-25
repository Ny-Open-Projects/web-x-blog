---
title: [NODE-695] 请求体校验（zod/schema）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-695：请求校验怎么做？
**答**：
- 单源校验：zod schema 定义 → 类型推导（TS 类型单源——SCN-ENG-247 契约单源）→ OpenAPI 生成（文档同步）→ 中间件统一校验（不散落 handler）。
- 校验分层：结构校验（字段/类型——必选）、业务校验（跨字段/依赖——custom refine）、规范化（trim/normalize——校验前清洗）。
- 错误输出：结构化校验错误（字段路径+原因——客户端可定位表单错误，SCN-联想-540 校验引擎同源）；校验失败 422（语义校验失败标准码）。
- 性能：schema 编译缓存（zod parse 有开销——预编译/复用 schema 对象）、大请求体的上限前置（SCN-NODE-666）。
- 追问钩子：为什么校验要「先规范化再校验」——`" 123 "` 带空格的手机号会被格式校验拒绝（用户困惑——明明输入对了）；normalize（trim/全角转半角/大小写）让「用户意图正确但格式细节错」的输入通过——校验的严格性应该用于「真正错误的输入」，不是「格式差异」。

```javascript
const OrderSchema = z.object({
  amount: z.coerce.number().positive(),                // 规范化 + 校验
  coupon: z.string().optional(),
}).refine(d => d.coupon ? d.amount > 100 : true, {     // 业务校验
  message: '优惠券需满 100', path: ['coupon'],
});
app.post('/order', validate(OrderSchema), handler);    // 中间件统一
// 422 输出
{ code: 'VALIDATION', issues: [{ path: 'amount', message: 'positive required' }] }
```
