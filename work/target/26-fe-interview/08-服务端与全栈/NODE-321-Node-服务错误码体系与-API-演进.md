---
title: [NODE-321] Node 服务错误码体系与 API 演进？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-321：Node 服务错误码体系与 API 演进？
**答**:
- 错误码三层：HTTP 状态（传输层语义）+ 业务码（域前缀：ORDER_001）+ 前端可行动标记（retryable/user_message）——前端只依赖业务码分支处理。
- 码注册制：错误码进注册表（code/owner/message/solution 链接）——NODE-032 延伸，码删除走 deprecation。
- API 演进：错误码向后兼容（新码可加、旧码不删改语义）——前端按码分支，服务端删码要监控前端引用。
- 演练：错误码全量文档自动生成（注册表 → 文档站），前端类型包同步生成。

```typescript
// 错误码注册表
const ERRORS = {
  ORDER_STOCK_EMPTY: { code: 'ORDER_001', status: 409, msg: '库存不足', retryable: false },
  ORDER_RATE_LIMIT:   { code: 'ORDER_002', status: 429, msg: '请求过快', retryable: true, retryAfter: 5 },
} as const;
class BizError extends Error {
  constructor(private def: keyof typeof ERRORS, private detail?: unknown) { super(ERRORS[def].msg); }
}
// 统一序列化：{ code, message, retryable, detail } —— 前端 axios 拦截器按 retryable 决定重试（NODE-300 幂等配合）
```
