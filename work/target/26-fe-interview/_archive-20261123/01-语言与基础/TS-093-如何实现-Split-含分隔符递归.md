---
title: [TS-093] 如何实现 Split（含分隔符递归）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-093：如何实现 Split（含分隔符递归）？
**答**：
- 基本形式：`S extends \`${infer L}${Sep}${infer R}\` ? [L, ...Split<R, Sep>] : [S]`。
- R 继续递归直到不含分隔符，收进元组。
- 特例：`Sep = ""` 时按字符切分，且空串要返回 `[]` 而不是 `[""]`，需要单独分支。

```typescript
type Split<S extends string, Sep extends string> =
  S extends `${infer L}${Sep}${infer R}`
    ? [L, ...Split<R, Sep>]
    : Sep extends ""
      ? S extends ""
        ? []
        : [S]
      : [S];

type S1 = Split<"a,b,c", ",">;   // ["a", "b", "c"]
type S2 = Split<"abc", "">;      // ["a", "b", "c"]（按字符切分）
type S3 = Split<"", "">;         // []
type S4 = Split<"one", ",">;     // ["one"]（无分隔符整体返回）
```
