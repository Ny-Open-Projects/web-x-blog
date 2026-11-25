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

**边界与易错**：

- `Object.setPrototypeOf(this, ApiError.prototype)` 不能省：编译到 ES5 时继承内置 Error 会断掉原型链，`e instanceof ApiError` 为 false，按类型分支的处理全部失效。
- `cause` 不参与 `JSON.stringify`，直接上报错误对象只会丢掉根因；必须手动递归展开 cause 链，并防循环引用。
- 判断有没有根因要用 `'cause' in e`，而不是 `e.cause !== undefined`，某些实现会挂上一个值为 undefined 的 cause 属性。

**追问**：

1. 自定义错误要不要重写 `name`？ → 要，`name` 默认继承 `'Error'`，重写成 `'ApiError'` 才能在日志和堆栈里区分类型。
2. cause 链很长时上报怎么处理？ → 限制展开深度（如 5 层），每层只留 name/message/code，避免 payload 超限和敏感信息外泄。
3. 怎么让调用方知道这个错误可否重试？ → 在错误类上加 `retryable` 布尔字段或按 code 映射，而不是让上层去解析 message 字符串。
