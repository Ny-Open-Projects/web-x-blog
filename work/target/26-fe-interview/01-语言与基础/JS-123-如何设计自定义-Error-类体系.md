---
title: [JS-123] 如何设计自定义 Error 类体系？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-123：如何设计自定义 Error 类体系？

**答**：
- 业务错误按"语义"分层：校验错误（400）、鉴权错误（401）、业务规则错误（200+biz 标记）、未知错误（500）。
- 统一基类携带 code/message/context，子类只补充语义；`instanceof` 做分层处理。
- ES2022 的 `new Error(msg, { cause })` 可串联原始错误，不丢根因。
- `Error.captureStackTrace?.(this, ctor)`（Node）裁剪内部帧；必须设 `this.name = 子类名`，否则堆栈首行显示 Error。

```javascript
class AppError extends Error {
  constructor(code, message, { cause, context } = {}) {
    super(message, { cause }); // ES2022：保留根因
    this.name = this.constructor.name; // 堆栈首行显示真实类名
    this.code = code;
    this.context = context;
    Error.captureStackTrace?.(this, this.constructor); // Node：隐藏内部帧
  }
}

class ValidationError extends AppError {}  // 用户输入问题 → 400
class AuthError extends AppError {}        // 未登录/无权限 → 401
class BizError extends AppError {}         // 业务规则拒绝 → 200 + biz 标记

function toResponse(err) {
  if (err instanceof ValidationError) return { status: 400, msg: err.message };
  if (err instanceof AuthError)       return { status: 401, msg: '请先登录' };
  if (err instanceof BizError)        return { status: 200, biz: true, msg: err.message };
  return { status: 500, msg: '系统异常' }; // 未知错误不向前端暴露细节
}

try {
  throw new ValidationError('1001', '手机号格式错误', {
    context: { field: 'phone', value: '123' },
    cause: new Error('regex not matched'),
  });
} catch (e) {
  console.log(e.name, e.code, toResponse(e));
  console.log(e.cause.message); // regex not matched — 根因不丢
}

// 包装链：底层错误转高层错误时挂 cause
async function loadUser(id) {
  try {
    return await Promise.resolve({ id });
  } catch (e) {
    throw new BizError('2001', '加载用户失败', { cause: e });
  }
}
```
