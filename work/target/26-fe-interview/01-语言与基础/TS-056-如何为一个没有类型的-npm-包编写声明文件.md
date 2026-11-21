---
title: [TS-056] 如何为一个没有类型的 npm 包编写声明文件？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-056：如何为一个没有类型的 npm 包编写声明文件？
**答**：
- 最简方案：`declare module "包名"` 给整个模块声明 any 类型，快速消除报错。
- 更好的方案：为模块导出的每个 API 写精确签名，放到 `.d.ts` 文件。
- 全局变量用 `declare global`、`declare const` 声明；类型文件通过 `typeRoots`/`types` 引入。
- 包作者可用 `package.json` 的 `types` 字段指向声明文件，消费者自动获得类型。

```typescript
// types/untyped-lib.d.ts
declare module "untyped-lib" {
  export interface RequestOptions {
    timeout?: number;
    retries?: number;
  }

  export function request(url: string, options?: RequestOptions): Promise<unknown>;
  export function debounce<T extends (...args: any[]) => void>(fn: T, wait: number): T;

  const version: string;
  export default { request, debounce, version };
}

// 全局环境变量声明：types/env.d.ts
interface ImportMetaEnv {
  readonly VITE_API_URL: string;
}
```

## 第十六章 enum 与 const enum
