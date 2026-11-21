---
title: [TS-144] ts-essentials 的 DeepPartial 严格版比基础版严格在哪？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-144：ts-essentials 的 DeepPartial 严格版比基础版严格在哪？
**答**：
- 基础版（TS-059）会把 Function/Date/RegExp 等内置类型也展开成 `{}?`，语义错误。
- 严格版引入 Builtin 集合（Primitive | Function | Date | Error | RegExp）短路返回，再处理 Map/Set/Promise 等容器。
- 数组走"元素递归"而不是对象键展开；AnyFunction 是库里的基础积木。

```typescript
// ts-essentials 精选
type Primitive = string | number | boolean | bigint | symbol | null | undefined;
type Builtin = Primitive | Function | Date | Error | RegExp;
type AnyFunction = (...args: any[]) => any;

type DeepPartialStrict<T> = T extends Builtin
  ? T
  : T extends Map<infer K, infer V> ? Map<DeepPartialStrict<K>, DeepPartialStrict<V>>
  : T extends Set<infer U> ? Set<DeepPartialStrict<U>>
  : T extends Promise<infer U> ? Promise<DeepPartialStrict<U>>
  : T extends AnyFunction ? T
  : T extends object ? { [K in keyof T]?: DeepPartialStrict<T[K]> }
  : T;

interface Cfg {
  callback: (v: number) => void; // 严格版：保持函数原样，不被拆成可选属性包
  createdAt: Date;               // 严格版：Date 原样
  meta: { nested: { deep: string } };
}
type Patchable = DeepPartialStrict<Cfg>;
const patch: Patchable = { meta: { nested: { deep: "x" } } }; // callback/createdAt 可整段缺省
```
