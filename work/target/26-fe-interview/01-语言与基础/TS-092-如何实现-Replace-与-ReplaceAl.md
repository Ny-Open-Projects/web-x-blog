---
title: [TS-092] 如何实现 Replace 与 ReplaceAll？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-092：如何实现 Replace 与 ReplaceAll？
**答**：
- Replace：`S extends \`${infer L}${From}${infer R}\`` 捕获前后段拼回 To，只替换第一处。
- ReplaceAll：替换后把结果递归处理，直到匹配不上 From。
- 关键防御：`From extends ""` 必须短路返回原串，否则空串能匹配到任意位置造成无限递归。

```typescript
type Replace<S extends string, From extends string, To extends string> =
  From extends ""
    ? S
    : S extends `${infer L}${From}${infer R}`
      ? `${L}${To}${R}`
      : S;

type ReplaceAll<S extends string, From extends string, To extends string> =
  From extends ""
    ? S
    : S extends `${infer L}${From}${infer R}`
      ? ReplaceAll<`${L}${To}${R}`, From, To>
      : S;

type R1 = Replace<"foo-bar-baz", "bar", "qux">;        // "foo-qux-baz"
type R2 = ReplaceAll<"foo-bar-bar", "bar", "qux">;     // "foo-qux-qux"
type R3 = Replace<"abc", "", "x">;                     // "abc"（空 From 短路）
```
