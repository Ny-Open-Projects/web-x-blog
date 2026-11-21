---
title: [TS-184] useUnknownInCatchVariables 开启后如何迁移？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-184：useUnknownInCatchVariables 开启后如何迁移？
**答**：
- strict 默认包含它：catch 变量从 any 变 unknown，直接 `e.message` 全部报错。
- 迁移三板斧：instanceof 收窄、typeof 字符串收窄、统一 toError 工具兜底。
- 反模式是关掉该选项：等于放弃收窄起点，让错误处理退化回 any 时代。

```typescript
// useUnknownInCatchVariables: true（strict 自带）
try {
  JSON.parse("{bad}");
} catch (e) {
  // e: unknown
  if (e instanceof SyntaxError) {
    console.log(e.message);     // 收窄为 SyntaxError
  } else if (typeof e === "string") {
    console.log(e);             // 一些运行时 throw 字符串
  } else {
    throw e;                    // 未知类型继续抛，不吞错
  }
}

// 迁移工具：统一错误归一化
function toError(e: unknown): Error {
  if (e instanceof Error) return e;
  return new Error(typeof e === "string" ? e : JSON.stringify(e));
}
// 存量代码批量替换：catch (e) { logger.error(toError(e).message) }
```
