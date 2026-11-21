---
title: [JS-133] monorepo 中的模块解析有哪些规则与坑？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-133：monorepo 中的模块解析有哪些规则与坑？

**答**：
- workspace 包以 package.json 的 name 作为 import 路径（如 `@app/shared`），解析器沿符号链接进真实目录。
- `exports` 字段是"导出白名单"：声明后外部只能 import 列出的子路径，深路径 import 会被拒绝。
- 优先级：exports 存在时，main/module/browser 全部被忽略（Node 12+ 与现代打包器一致）。
- 经典坑：peer 依赖版本不一致导致双实例（两份 react，hooks 报错）；符号链接的 realpath 差异影响打包器判断。

```javascript
// packages/shared/package.json
// {
//   "name": "@app/shared",
//   "exports": {
//     ".":       { "types": "./src/index.ts", "default": "./src/index.ts" },
//     "./utils": "./src/utils.js"
//   }
// }

// apps/web 内使用：
// import { api } from '@app/shared';       // ✓ 命中 "." 导出
// import { fmt } from '@app/shared/utils'; // ✓ 命中子路径白名单
// import x from '@app/shared/src/secret';  // ✗ 不在白名单 → ERR_PACKAGE_PATH_NOT_EXPORTED

// 查询解析结果（Node）：
// import.meta.resolve('@app/shared'); // 返回符号链接解析后的真实 URL

// 坑一：双实例问题
// shared 依赖 react@18，web 依赖 react@19 → node_modules 出现两份 react
// 症状：Invalid hook call。解法：统一版本 + peerDependencies + workspace 协议
// package.json: { "dependencies": { "react": "workspace:^" } }

// 坑二：TS 直接引 src 的项目
// monorepo 内常不预构建，靠 bundler/tsconfig paths 直指源码
// { "paths": { "@app/shared": ["../../packages/shared/src/index.ts"] } }

// 坑三：pnpm 符号链接 → 打包器 realpath 后判定包在 node_modules 外
// 需要配置 preserveSymlinks 或打包器的 resolve.preserveSymlinks 保持一致
console.log('monorepo 解析规则见上方注释');
```
