---
title: [TS-119] 类型守卫 is、in、instanceof 各自适用什么场景？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-119：类型守卫 is、in、instanceof 各自适用什么场景？
**答**：
- `is`（自定义谓词）：把运行时判断逻辑（typeof、字段存在性、正则）包装成可复用的守卫函数，是最通用的企业方案。
- `in`：判定可选/多态字段是否存在于对象上，适合可辨识联合之外的"宽对象收窄"。
- `instanceof`：只适用于 class 实例（含 Error、Date 等内置类），普通对象字面量无原型语义时不适用。
- 选型原则：数据来自外部（JSON/API）优先 is + 显式校验；类层次用 instanceof；不确定结构用 in 逐步收窄。

```typescript
// is：自定义谓词，逻辑可复用
interface ApiError { code: number; message: string }
interface ApiSuccess<T> { code: number; data: T }

function isApiError<T>(res: ApiSuccess<T> | ApiError): res is ApiError {
  // 注意：直接写 res.data === undefined 编译报错（ApiError 上没有 data），
  // 用 "data" in res 反向判断更安全
  return "message" in res && !("data" in res);
}

// in：按字段存在性收窄
function describe(obj: { kind: string } | null) {
  if (obj !== null && "kind" in obj) {
    obj.kind; // string，收窄到非空且含 kind
  }
}

// instanceof：类实例专用
class HttpError extends Error {}
function handle(e: unknown) {
  if (e instanceof HttpError) {
    e.stack; // 收窄到 HttpError
  } else if (e instanceof Error) {
    e.message;
  }
}
```
