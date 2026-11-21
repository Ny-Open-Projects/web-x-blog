---
title: [TS-100] 如何提取对象所有叶子节点的路径（Paths）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-100：如何提取对象所有叶子节点的路径（Paths）？
**答**：
- 递归：是对象就遍历键，路径前缀用模板字面量拼接（`P extends "" ? K : \`${P}.${K}\``）。
- 不是对象（叶子）时返回累积的路径 P，所有叶子路径经联合合并。
- 路径联合通常作为 GetByPath（TS-101）的入参约束，实现"点路径补全"。

```typescript
type Paths<T, P extends string = ""> =
  T extends object
    ? { [K in keyof T & string]: Paths<T[K], P extends "" ? K : `${P}.${K}`> }[keyof T & string]
    : P;

interface Config {
  server: { host: string; port: number; tls: { enabled: boolean } };
  debug: boolean;
}

type AllPaths = Paths<Config>;
// "server.host" | "server.port" | "server.tls.enabled" | "debug"

// 应用：环境变量 key 只允许声明的路径
declare function getEnv<K extends AllPaths>(key: K): void;
getEnv("server.host"); // OK
// getEnv("server.hst"); // 报错：路径不存在
```
