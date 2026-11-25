---
title: [NODE-767] 笔试题——实现错误码注册表与统一错误中间件？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-767：手写错误码体系

**需求与边界**：
- 需求：错误码体系（SCN-NODE-676）——① 错误码注册表（码/文案 key/retryable/http 映射——单源，SCN-ENG-240）；② 稳定性校验（CI 检查码不重排——新增 only）；③ 统一中间件（typed error 渲染——未知错误兜底 SYS-000）；④ traceId 附带（关联日志）。
- 边界：① 未知错误兜底（不泄露堆栈——SCN-NODE-646 脱敏）；② 错误码表生成文档（OpenAPI errors 扩展——SCN-ENG-247）；③ i18n key（文案国际化——SCN-联想-831）。

**答**：
```javascript
// errors.yaml（单源注册表）
// SYS-000: { messageKey: error.internal, http: 500, retryable: true }
// PAY-001: { messageKey: error.pay.insufficient, http: 400, retryable: false }
const registry = loadYaml('errors.yaml');
class AppError extends Error {
  constructor(code, detail) {
    const meta = registry[code] ?? registry['SYS-000'];   // 未知码兜底
    super(meta.messageKey);
    Object.assign(this, { code, ...meta, detail });
  }
}
app.use((err, req, res, next) => {                     // 统一中间件（SCN-NODE-676）
  const e = err instanceof AppError ? err : new AppError('SYS-000', err.stack);   // 兜底
  logger.error({ code: e.code, detail: e.detail, traceId: ctx.getStore()?.traceId });   // detail 进日志
  res.status(e.http).json({
    code: e.code, message: e.messageKey,               // i18n key（SCN-联想-831）
    retryable: e.retryable, traceId: ctx.getStore()?.traceId });   // 客户端三要素 + traceId
});
// CI 稳定性校验（SCN-NODE-676 只增不改）
const prev = loadPrevRegistry();
for (const [code, meta] of Object.entries(prev))
  assert(registry[code] && meta.http === registry[code].http, `错误码 ${code} 被重排——禁止`);
```

**评分点**:
- 注册表单源（码/文案/retryable/http——SCN-ENG-240）。
- 未知错误兜底 + detail 进日志不外发（脱敏——SCN-NODE-676）。
- CI 稳定性校验（只增不改——客户端契约）。
- traceId 附带（排障关联——SCN-NODE-645）。
