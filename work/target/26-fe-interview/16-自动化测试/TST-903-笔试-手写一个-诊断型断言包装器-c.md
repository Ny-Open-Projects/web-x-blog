---
title: [TST-903] 笔试：手写一个「诊断型断言包装器」check(condition, context)，失败时输出可检索的结构化诊断
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-903：笔试：手写一个「诊断型断言包装器」check(condition, context)，失败时输出可检索的结构化诊断
**答**：
- 需求：实现 check(cond, context)，cond 为布尔或返回布尔的函数；失败抛错且错误信息含 message、context、timestamp、traceId。
- 规则：context 中的敏感字段（phone/idCard）需脱敏后再输出；支持 check.multi([...]) 一次收集多个失败不中断。
- 边界：cond 为函数时异常要被捕获并记录；context 为循环引用对象不能导致 JSON.stringify 崩溃。

```javascript
function check(cond, context = {}) {
  const now = new Date().toISOString();
  const traceId = globalThis.__traceId ?? 'local';
  const ok = typeof cond === 'function' ? (() => {
    try { return cond(); } catch (e) { context.fnError = e.message; return false; }
  })() : cond;
  if (ok) return true;
  const safe = JSON.stringify(context, (k, v) => {
    if (/phone|idCard|token/i.test(k)) return '***';
    if (typeof v === 'object' && v !== null && v.__seen) return '[Circular]';
    if (typeof v === 'object' && v !== null) v.__seen = true;
    return v;
  });
  const err = new Error(`[ASSERT] ${context.message || '断言失败'} | ctx=${safe}`);
  err.diagnostic = { message: context.message, context: safe, timestamp: now, traceId };
  throw err;
}
check.multi = (checks) => {
  const errs = [];
  for (const [cond, ctx] of checks) {
    try { check(cond, ctx); } catch (e) { errs.push(e.diagnostic); }
  }
  if (errs.length) { const e = new Error(`${errs.length} 项断言失败`); e.details = errs; throw e; }
};
check(false, { message: '券后价错误', phone: '13800000000' });
```
**评分点**：
- check 支持布尔与函数两种 cond，函数异常被捕获进 fnError 而非中断收集。
- 错误信息包含 message/context/timestamp/traceId 四要素，contex 脱敏。
- check.multi 收集全部失败后统一抛出，details 保留每条诊断。
- 用 replacer 处理循环引用与敏感字段，避免 stringify 崩溃与 PII 泄漏。
