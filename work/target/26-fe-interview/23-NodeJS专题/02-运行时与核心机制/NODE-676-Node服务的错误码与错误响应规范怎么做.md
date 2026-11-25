---
title: [NODE-676] Node 服务的错误码与错误响应规范怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-676：错误码规范怎么做？
**答**：
- 错误模型三要素：机器码（错误码枚举——客户端分支判断）、人话文案（用户可读——i18n key 而非硬文案）、诊断信息（traceId + 内部详情——仅日志不外发）。
- 码体系设计：分段（模块段+类型段——如 PAY-1001）或全局枚举——码要稳定（新增不重排——客户端按码分支会炸）、可注册（错误码表单源管理，SCN-ENG-240 错误模型联动）。
- HTTP 状态映射：4xx（客户端可修——重试语义 false）vs 5xx（服务端——可重试 true）+ 重试头（Retry-After——SCN-NODE-641）；错误响应不可泄露堆栈（脱敏——SCN-NODE-646）。
- 错误中间件统一：单一 error handler（fallback 边界——SCN-OPS-240 统一降级）——业务抛 typed error，中间件统一渲染。
- 追问钩子：为什么「错误码要稳定且新增不重排」——客户端把错误码硬编码进分支逻辑（PAY-1001 → 引导换卡）；重排后 PAY-1001 变成别的语义，客户端分支全错——错误码是「对外 API 契约」的一部分，语义绑定后只增不改，废弃用 deprecated 标注——和 API 版本治理同等级的严肃性。

```javascript
class AppError extends Error {
  constructor(code, messageKey, { retryable = false, http = 400, detail } = {}) {
    super(messageKey); Object.assign(this, { code, messageKey, retryable, http, detail });
  }
}
// 统一中间件
app.use((err, req, res, next) => {
  const e = err instanceof AppError ? err : new AppError('SYS-000', 'error.internal', { http: 500, retryable: true });
  telemetry.error(e, { traceId: als.getStore()?.traceId, detail: e.detail });   // 内部详情进日志
  res.status(e.http).json({ code: e.code, message: e.messageKey, retryable: e.retryable,
    traceId: als.getStore()?.traceId });               // 客户端只见三要素
});
```
