---
title: [TS-024] 断言函数 asserts 是什么？适用什么场景？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-024：断言函数 asserts 是什么？适用什么场景？
**答**：
- `asserts value is T` 表示：函数正常返回时，value 一定可收窄为 T；抛错则中断执行。
- 与 `is` 守卫的区别：asserts 不需要返回布尔值，而是"不抛错就是真"的契约。
- 适合集中校验入口数据，如 env 校验、参数校验函数。
- 收窄效果作用于调用点之后，常用于避免到处写 if。

```typescript
function assertIsString(value: unknown): asserts value is string {
  if (typeof value !== "string") {
    throw new Error("期望 string 类型");
  }
}

function toUpper(value: unknown) {
  assertIsString(value);
  return value.toUpperCase(); // 此处已收窄为 string
}

function assertNonNull<T>(value: T): asserts value is NonNullable<T> {
  if (value === null || value === undefined) {
    throw new Error("值不能为空");
  }
}
```
