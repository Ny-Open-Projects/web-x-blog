---
title: [TS-039] 如何手写 Awaited？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-039：如何手写 Awaited？
**答**：
- Awaited 递归解包 Promise：`T extends Promise<infer V> ? Awaited<V> : T`。
- 递归是关键：`Promise<Promise<number>>` 要解到 `number`。
- 真实实现还处理 thenable（带 then 方法的对象）与多值联合。
- 常用于给 async 包装函数取返回值：`ReturnType` + `Awaited`。

```typescript
type MyAwaited<T> = T extends null | undefined
  ? T
  : T extends object & { then(onfulfilled: infer F): any }
    ? F extends (value: infer V) => any
      ? MyAwaited<V>
      : never
    : T;

type A = MyAwaited<Promise<number>>; // number
type B = MyAwaited<Promise<Promise<string>>>; // string
type C = MyAwaited<boolean>; // boolean

async function fetchData() {
  return { list: [1, 2] };
}
type Data = MyAwaited<ReturnType<typeof fetchData>>; // { list: number[] }
```
