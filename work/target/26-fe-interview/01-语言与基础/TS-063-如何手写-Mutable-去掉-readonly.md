---
title: [TS-063] 如何手写 Mutable（去掉 readonly 修饰符）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-063：如何手写 Mutable（去掉 readonly 修饰符）？
**答**：
- 映射类型支持 `-readonly` 修饰符，专用于移除只读标记。
- 常见场景：从 `as const` 配置推导出的深只读类型，需要在可变副本上操作时先转 Mutable。
- 深层版本 DeepMutable 见 TS-090，这里先给出浅层实现。

```typescript
type Mutable<T> = { -readonly [K in keyof T]: T[K] };

type Config = {
  readonly host: string;
  readonly port: number;
};

type Editable = Mutable<Config>;
// { host: string; port: number }
const c: Editable = { host: "localhost", port: 8080 };
c.port = 9090; // OK，不再只读
```
