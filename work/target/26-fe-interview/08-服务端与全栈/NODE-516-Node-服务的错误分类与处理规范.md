---
title: [NODE-516] Node 服务的错误分类学与处理规范（异常设计）如何制定？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-516：错误分类学与处理规范
**答**:
- 分类学：业务错误（预期内：库存不足——有码有文案，不计入监控错误率）、系统错误（预期外：DB 挂——告警+堆栈）、第三方错误（转译 NODE-491）、编程错误（bug：类型错误——必须修复不吞）。每类处理路径不同：业务错误正常返回、系统错误告警+降级、编程错误 fail fast。
- 错误对象规范：统一 AppError 基类（code/httpStatus/userMsg/internalDetail/cause——cause 链保留根因）、禁裸 throw 字符串/禁吞 catch（lint 规则）、错误码注册表（NODE-321 单源）。
- 传播规范：底层抛语义错误（不 throw new Error('db')）→ 中间层按需包装（加上下文 cause）→ 顶层统一处理（中间件映射 HTTP 响应 NODE-410）。
- 异步错误：async 函数必须 catch（lint no-floating-promises NODE-358）、EventEmitter 错误监听（漏监听 = 进程崩溃——error 事件强制注册）。
- 落地：错误处理规范文档 + lint + code review checklist；错误率分类指标（业务错/系统错分开——ARC-516 分类进指标 NODE-372）。
```javascript
class AppError extends Error {
  constructor(code, { userMsg, httpStatus = 500, cause } = {}) {
    super(userMsg ?? code); this.code = code; this.httpStatus = httpStatus; this.cause = cause;
  }
}
// 底层：throw new AppError('STOCK_OUT', { userMsg: '库存不足', httpStatus: 409 });
// 顶层：catch (e) { res.status(e.httpStatus ?? 500).json(toErrorBody(e)); if (!(e instanceof AppError)) report(e); }
```
