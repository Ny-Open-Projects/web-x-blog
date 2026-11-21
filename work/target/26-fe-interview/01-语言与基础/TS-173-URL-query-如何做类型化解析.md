---
title: [TS-173] URL query 如何做类型化解析？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-173：URL query 如何做类型化解析？
**答**：
- 解析器表（schema）决定目标类型：`ReturnType<S[K]>` 映射出每个键的产出类型。
- 缺参现实存在，返回 Partial 而不是撒谎；schema 之外的键访问直接报错。
- 与 Zod 方案（TS-120）的取舍：轻量场景用解析器表，重校验场景用 Zod 单一来源。

```typescript
type Parsers = Record<string, (raw: string) => unknown>;

function parseQuery<S extends Parsers>(search: string, schema: S) {
  type Result = { [K in keyof S]: ReturnType<S[K]> };
  const params = new URLSearchParams(search);
  const out: Partial<Result> = {};
  for (const key of Object.keys(schema) as (keyof S & string)[]) {
    const raw = params.get(key);
    if (raw !== null) {
      (out as Record<string, unknown>)[key] = schema[key](raw);
    }
  }
  return out as Partial<Result>;
}

const q = parseQuery("?page=2&vip=1", {
  page: Number,
  vip: (v) => v === "1",
});
q.page;   // number | undefined
// q.nope; // 报错：schema 之外的键不存在
```
