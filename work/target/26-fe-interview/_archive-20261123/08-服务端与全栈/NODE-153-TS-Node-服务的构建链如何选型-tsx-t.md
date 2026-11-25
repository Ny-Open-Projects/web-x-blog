---
title: [NODE-153] TS Node 服务的构建链如何选型（tsx/ts-node/tsc）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-153：TS Node 服务的构建链如何选型（tsx/ts-node/tsc）？
**答**：
- 开发态用 **tsx**（esbuild 内核，零配置直跑 TS + watch，替代慢的 ts-node）；生产态用 **tsc 产出 dist**——稳定、可回滚、镜像里不装 devDependencies。
- 分层 tsconfig：`tsconfig.json`（编辑器/检查，noEmit）+ `tsconfig.build.json`（产物，排除测试）。
- CI 门禁：`tsc --noEmit` 类型检查独立于运行；测试用 vitest（esbuild 同源，速度匹配 tsx）。
- 折中方案：tsup/esbuild 打单文件（快 + 免路径别名处理），但失去生成 d.ts 的严格性——库用 tsc，应用可打包。

```json
{
  "type": "module",
  "engines": { "node": ">=20" },
  "scripts": {
    "dev": "tsx watch src/server.ts",
    "typecheck": "tsc --noEmit",
    "build": "tsc -p tsconfig.build.json",
    "start": "node dist/server.js",
    "test": "vitest run"
  },
  "devDependencies": {
    "tsx": "^4.0.0",
    "typescript": "^5.5.0",
    "vitest": "^2.0.0"
  }
}
```

```json
// tsconfig.build.json —— 只收 src，产出干净 dist
{
  "extends": "./tsconfig.json",
  "compilerOptions": { "outDir": "dist", "declaration": false },
  "include": ["src"],
  "exclude": ["src/**/*.test.ts"]
}
```
