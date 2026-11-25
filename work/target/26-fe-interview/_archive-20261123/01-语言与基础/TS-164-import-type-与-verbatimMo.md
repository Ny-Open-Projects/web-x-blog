---
title: [TS-164] import type 与 verbatimModuleSyntax 的关系是什么？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-164：import type 与 verbatimModuleSyntax 的关系是什么？
**答**：
- verbatimModuleSyntax 让 import 语句"原样输出"到产物，类型与值必须在源码里说清楚。
- 纯类型导入必须写 `import type`，否则报错 1484；混合导入用 `import { foo, type Bar }` 内联标注。
- 收益：单文件转译器（esbuild/swc）无需猜测哪些导入可删，产物确定性强；也避免"把不存在的运行时值打进 bundle"。

```typescript
// verbatimModuleSyntax: true
import type { User, UserRow } from "./types";          // 纯类型：编译后整句消失
import { createUser, type UserRow } from "./service";  // 混合：值留下、类型剥掉

// ❌ 旧习惯：import { User } from "./types" 后只当类型用
// 开启后报错 1484：User is a type and must be imported using a type-only import

// 为什么重要：esbuild 转 TS 时只删"带 type 关键字"的导入，
// 模糊写法在 isolatedModules 下可能把纯类型模块当运行时依赖打进产物
```
