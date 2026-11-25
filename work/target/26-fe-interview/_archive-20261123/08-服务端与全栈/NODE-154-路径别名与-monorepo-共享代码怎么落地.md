---
title: [NODE-154] 路径别名与 monorepo 共享代码怎么落地？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-154：路径别名与 monorepo 共享代码怎么落地？
**答**：
- 开发态：`tsconfig paths` 让 `@shared/utils` 可解析（编辑器 + tsc 都认）；**运行态是另一回事**——Node 不认识 paths。
- 三种运行态方案：① `tsc-alias`/`module-alias` 构建期改写；② tsup/esbuild 打包时解析；③ **monorepo 正统**：shared 做成 workspace 包，`package.json exports` 声明入口，Node 原生解析。
- pnpm workspace 下 shared 改动即时生效（软链），无需反复构建；CI 里各包独立类型检查。
- 坑：`"module": "NodeNext"` 时相对导入必须带扩展名，exports 字段要与文件结构对齐。

```json
// tsconfig.base.json（monorepo 根）
{
  "compilerOptions": {
    "strict": true,
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "baseUrl": ".",
    "paths": {
      "@shared/*": ["packages/shared/src/*"],
      "@db/*": ["packages/db/src/*"]
    }
  }
}
```

```json
// packages/shared/package.json —— workspace 包，运行态靠 exports 解析
{
  "name": "@acme/shared",
  "type": "module",
  "exports": {
    ".": "./src/index.ts",
    "./utils": "./src/utils.ts"
  }
}
// 应用侧 dependencies 写 "workspace:*"（pnpm）→ 软链即改即生效
```
