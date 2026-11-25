---
title: [TS-066] 如何提取函数属性键 FunctionKeys 与 NonFunctionKeys？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-066：如何提取函数属性键 FunctionKeys 与 NonFunctionKeys？
**答**：
- 用键重映射 + 条件类型：`T[K] extends (...args: any[]) => any` 判定该属性是否为函数。
- 命中函数的键保留，其余映射为 `never` 被联合吸收即可得到 FunctionKeys。
- NonFunctionKeys 反过来分支即可；也可直接 `Exclude<keyof T, FunctionKeys<T>>`。

```typescript
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any ? K : never;
}[keyof T];

type NonFunctionKeys<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any ? never : K;
}[keyof T];

interface Service {
  url: string;
  timeout: number;
  fetch: () => Promise<void>;
  save: (data: string) => void;
}

type FK = FunctionKeys<Service>;     // "fetch" | "save"
type NFK = NonFunctionKeys<Service>; // "url" | "timeout"
```
