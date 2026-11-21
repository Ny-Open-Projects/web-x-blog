---
title: [TS-167] global.d.ts 里如何扩展环境变量类型（ImportMetaEnv）？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-167：global.d.ts 里如何扩展环境变量类型（ImportMetaEnv）？
**答**：
- Vite 约定：interface ImportMetaEnv 里声明自定义环境变量，import.meta.env 获得精确类型。
- 必须写在全局作用域（文件内不能有 import/export），才能与 vite/client 的同名 interface 声明合并。
- 拼写错误、忘记配置变量都变成编译期错误。

```typescript
// types/global.d.ts —— 注意：文件内不能出现 import/export
interface ImportMetaEnv {
  readonly VITE_API_BASE: string;
  readonly VITE_SENTRY_DSN?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}

const base = import.meta.env.VITE_API_BASE; // string
// import.meta.env.VITE_API_BSAE;           // 报错：属性不存在（拼写错误编译期拦截）

// 坑：如果文件顶部写了 import，interface 变成模块私有，
// 不会与 vite/client 中的 ImportMetaEnv 合并，扩展失效
```
