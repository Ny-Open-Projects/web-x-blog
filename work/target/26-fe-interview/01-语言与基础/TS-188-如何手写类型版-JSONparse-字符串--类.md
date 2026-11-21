---
title: [TS-188] 如何手写类型版 JSON.parse（字符串 → 类型）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-188：如何手写类型版 JSON.parse（字符串 → 类型）？
**答**：
- 核心难点：数组/对象体按"顶层逗号"切分时必须跟踪引号与括号深度，否则嵌套结构被切碎。
- 三层结构：SplitTop（深度感知切分）→ Parse（按 `[`/`{`/标量分发）→ ParseValue（null/true/false/number）。
- 与运行时 JSON.parse 配合：契约推导与测试用类型版，防脏数据仍靠 schema 校验（TS-120）。

```typescript
type Trim<S extends string> = S extends ` ${infer R}` | `\n${infer R}` | `\t${infer R}`
  ? Trim<R>
  : S extends `${infer R} ` | `${infer R}\n` | `${infer R}\t` ? Trim<R> : S;

// 顶层切分：跟踪字符串引号与括号深度，只在深度 0 的逗号处切开
type SplitTop<S extends string, Cur extends string = "", Depth extends unknown[] = [], InStr extends boolean = false> =
  S extends `${infer C}${infer R}`
    ? InStr extends true
      ? C extends `"` ? SplitTop<R, `${Cur}"`, Depth, false> : SplitTop<R, `${Cur}${C}`, Depth, true>
      : C extends `"` ? SplitTop<R, `${Cur}"`, Depth, true>
      : C extends `[` | `{` ? SplitTop<R, `${Cur}${C}`, [...Depth, unknown], false>
      : C extends `]` | `}` ? SplitTop<R, `${Cur}${C}`, Depth extends [unknown, ...infer Pop] ? Pop : Depth, false>
      : C extends `,`
        ? Depth extends [] ? [Cur, ...SplitTop<R>] : SplitTop<R, `${Cur}${C}`, Depth, false>
        : SplitTop<R, `${Cur}${C}`, Depth, false>
    : [`${Cur}${S}`];

type ParseValue<S extends string> =
  S extends "null" ? null
  : S extends "true" ? true
  : S extends "false" ? false
  : S extends `${infer N extends number}` ? N
  : S;

type Parse<S extends string> =
  Trim<S> extends `[${infer Body}]`
    ? Body extends "" ? [] : { [K in keyof SplitTop<Body>]: Parse<Trim<SplitTop<Body>[K]>> }
    : Trim<S> extends `{${infer Body}}`
      ? Body extends "" ? {} : ParseObject<SplitTop<Body>>
      : ParseValue<Trim<S>>;

type ParseObject<Parts extends string[], Acc = {}> =
  Parts extends [infer H extends string, ...infer R extends string[]]
    ? H extends `"${infer K}":${infer V}`
      ? ParseObject<R, Acc & Record<K, Parse<Trim<V>>>>
      : never
    : { [K in keyof Acc]: Acc[K] }; // Prettify 收束交叉

type A = Parse<`[1, "a", true, null]`>;          // [1, "a", true, null]
type B = Parse<`{"id": 1, "tags": ["x", "y"]}`>; // { id: 1; tags: ["x", "y"] }
type C = Parse<`{"user": {"name": "n", "vip": false}}`>; // 嵌套对象递归解析
```
