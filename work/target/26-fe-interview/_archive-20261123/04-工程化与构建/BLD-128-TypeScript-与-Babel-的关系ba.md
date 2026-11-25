---
title: [BLD-128] TypeScript 与 Babel 的关系：babel 只剥离类型，tsc 双跑策略与 swc 兼容层。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-128：TypeScript 与 Babel 的关系：babel 只剥离类型，tsc 双跑策略与 swc 兼容层。
**答**：
- `@babel/preset-typescript` / `esbuild` / swc 都只做**类型剥离**（syntax transform），不做类型检查、不生成 d.ts——所以"TS → Babel → 产物"链路里类型错误不拦截构建。
- 双跑策略（生产主流）：CI 里**并行跑 babel 构建与 `tsc --noEmit`**（或 vue-tsc），tsc 只负责类型门禁；两者消费同一份 tsconfig，需注意 `isolatedModules: true` 强制单文件可转译（const enum、命名空间导出值等限制）。
- 类型检查工具补充：`fork-ts-checker-webpack-plugin`（webpack dev 内并行检查）、`tsc --noEmit --incremental`（tsbuildinfo 增量）；库项目产出 d.ts 用 `tsc --emitDeclarationOnly` 而非 babel。
- swc 生态兼容层：`@swc/core` 可直接吃 `.swcrc` 的 `jsc.parser.syntax: 'typescript'`；对 babel 生态通过 `swc-plugin`（wasm）或让 jest 用 `@swc/jest` 替换 babel-jest——迁移成本主要是自定义 babel 插件没有 swc 等价物。

```javascript
// CI 双跑示例：构建与类型检查并行（package.json scripts + CI 配置）
// package.json
// {
//   "scripts": {
//     "build": "NODE_ENV=production webpack --mode production",
//     "typecheck": "tsc --noEmit --incremental --tsBuildInfoFile .cache/tsbuildinfo",
//     "ci": "concurrently -g \"pnpm build\" \"pnpm typecheck\""
//   }
// }

// tsconfig.json 关键项：保证 babel 可转译
// {
//   "compilerOptions": {
//     "target": "ES2020",
//     "isolatedModules": true,          // babel/swc 单文件转译的前提
//     "importsNotUsedAsValues": "error",// 强制 type-only import，配合剥离
//     "skipLibCheck": true,
//     "incremental": true
//   }
// }

// jest 集成（swc 兼容层示例）：jest.config.js
module.exports = {
  transform: {
    '^.+\\.(t|j)sx?$': ['@swc/jest', {
      jsc: {
        parser: { syntax: 'typescript', tsx: true, decorators: true },
        transform: { react: { runtime: 'automatic' } },
        target: 'es2020',
      },
    }],
  },
};
// 类型门禁不进 jest：测试跑 swc（快），类型错误由独立 typecheck job 拦截
```

## 十四章 Vite 源码级与实践深水区（BLD-129 ~ BLD-140）
