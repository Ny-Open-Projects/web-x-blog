---
title: [JS-321] Error cause 与自定义错误类型设计
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 异常]
type: 面试题
---

## JS-321：Error.cause 与自定义错误设计

**答**：
- error.cause（ES2022）：`new Error('失败', { cause: 原始错误 })`——错误链保留根因，替代「字符串拼 message 丢现场」
- 自定义错误类型：继承 Error（要设 prototype 以恢复 instanceof）、加 code/上下文字段、serializable
- 错误分层设计：底层抛具体错误 → 上层包装业务错误（cause 链）→ 顶层统一上报
- stack 的陷阱：跨层 new Error 会「重置」堆栈起点，cause 保留原始 stack 才能定位根因
- 上报规范：错误对象进埋点要脱敏 + 序列化（name/message/code/cause 链）

```javascript
class ApiError extends Error {
  constructor(message, code, cause) {
    super(message, { cause });
    this.name = 'ApiError';
    this.code = code;
    Object.setPrototypeOf(this, ApiError.prototype); // 修 instanceof
  }
}
async function loadUser() {
  try {
    return await fetchUser(id);
  } catch (e) {
    throw new ApiError('加载用户失败', 'USER_FETCH', e); // cause 保留原始 stack
  }
}
```
