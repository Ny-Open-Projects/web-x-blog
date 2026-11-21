---
title: [TS-151] MutableDeep 严格版如何处理数组与函数？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-151：MutableDeep 严格版如何处理数组与函数？
**答**：
- TS-090 的基础版递归去 readonly 即可；严格版要短路函数与内置类型、把 readonly 数组转普通数组。
- 元组在 `-readonly` 同态映射下保持形状，注意先判数组再判对象。
- 场景：把 Readonly 配置类型转回可编辑草稿类型时，函数字段绝不能被拆散。

```typescript
// 严格版 DeepMutable
type DeepMutableStrict<T> = T extends Function | Date | RegExp | Error
  ? T
  : T extends readonly (infer U)[]
    ? DeepMutableStrict<U>[]
    : T extends object
      ? { -readonly [K in keyof T]: DeepMutableStrict<T[K]> }
      : T;

interface Cfg {
  readonly name: string;
  readonly tags: readonly string[];
  readonly format: (s: string) => string;
  readonly meta: { readonly version: readonly number[] };
}

type Editable = DeepMutableStrict<Cfg>;
// { name: string; tags: string[]; format: (s: string) => string; meta: { version: number[] } }
const e: Editable = { name: "x", tags: [], format: (s) => s, meta: { version: [1] } };
e.meta.version.push(2); // 深层 readonly 全部解除
```
