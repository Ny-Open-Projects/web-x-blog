---
title: [TS-059] 如何手写 DeepPartial？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-059：如何手写 DeepPartial？
**答**：
- 递归条件类型 + 映射类型：对象则递归映射每个属性为可选，非对象直接返回。
- 要区分函数（typeof 为 function，也是 object），函数不应被展开。
- 数组可按需处理为 `DeepPartial<T>[]` 或保持原样，看业务需求。
- 同款套路可以写 DeepReadonly、DeepRequired。

```typescript
type Primitive = string | number | boolean | bigint | symbol | null | undefined;

type DeepPartial<T> = T extends Primitive
  ? T
  : T extends (...args: any[]) => any
    ? T // 函数保持原样
    : T extends Array<infer E>
      ? Array<DeepPartial<E>>
      : { [K in keyof T]?: DeepPartial<T[K]> };

interface Profile {
  user: {
    name: string;
    tags: string[];
    greet: () => void;
  };
  version: number;
}

const patch: DeepPartial<Profile> = {
  user: {
    name: "只改名字",
    // greet 必须是完整函数，不会被 Partial 化
  },
  // version 可以不传
};
```
