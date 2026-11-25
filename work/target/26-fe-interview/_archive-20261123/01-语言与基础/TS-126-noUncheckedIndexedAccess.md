---
title: [TS-126] noUncheckedIndexedAccess 解决什么问题？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-126：noUncheckedIndexedAccess 解决什么问题？
**答**：
- 默认情况下 `arr[0]`、`obj[key]` 的类型是元素类型本身，但运行时可能 undefined（越界、键不存在），类型撒谎。
- 开启后所有索引访问的结果都带上 `| undefined`，强制使用前判空，是大厂对"运行时安全索引"的标准要求。
- 配合 for-of、Object.values、`.at()` 等返回明确 undefined 的 API，减少不必要的索引访问。

```json
{
  "compilerOptions": {
    "noUncheckedIndexedAccess": true
  }
}
```

```typescript
const list = ["a", "b"];
const first = list[0];      // string | undefined（开启前是 string）
if (first !== undefined) first.toUpperCase(); // OK

const map: Record<string, number> = { a: 1 };
const v = map["b"];         // number | undefined
const safe = map["b"] ?? 0; // number，兜底写法成为习惯

for (const item of list) {
  item.toUpperCase();       // for-of 不受影响，推荐遍历方式
}
```
