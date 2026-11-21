---
title: [TS-123] 断言函数 asserts 的使用与陷阱是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-123：断言函数 asserts 的使用与陷阱是什么？
**答**：
- 两种形态：`asserts condition`（断言表达式为真）与 `asserts x is T`（断言 x 为 T），断言通过后 TS 永久收窄。
- 断言函数返回值必须标注为 void，且内部逻辑必须真的会 throw，否则收窄是"谎言"。
- 陷阱：断言本身不产生任何运行时校验，若函数体忘了抛错，类型层面通过但运行时裸奔；箭头函数不能声明断言（语法限制，需 function 声明）。

```typescript
function assertDefined<T>(value: T | undefined, msg: string): asserts value is T {
  if (value === undefined) throw new Error(msg);
  // 忘写 throw 就不会有运行时保护，但类型层面依然"骗过"编译器
}

function assert(condition: unknown, msg: string): asserts condition {
  if (!condition) throw new Error(msg);
}

function main(config?: { port: number }) {
  assertDefined(config, "config 必须提供");
  config.port; // 收窄为 { port: number }，不再是可选
  assert(typeof config.port === "number", "port 必须是数字");
}

// 陷阱示例：返回值不是 void 会报错
// function bad(x: unknown): boolean asserts x is string {} // 报错
```
