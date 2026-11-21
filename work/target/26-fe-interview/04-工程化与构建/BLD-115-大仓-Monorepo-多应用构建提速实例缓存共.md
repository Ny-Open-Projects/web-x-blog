---
title: [BLD-115] 大仓（Monorepo）多应用构建提速实例：缓存共享与范围限定怎么做？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-115：大仓（Monorepo）多应用构建提速实例：缓存共享与范围限定怎么做？
**答**：
- 四板斧：**范围限定**（只构建受影响应用，`turbo build --filter=app-a...[main]` 基线 diff）、**依赖拓扑共享**（公共包先构建、应用复用其产物而非重编译）、**缓存共享**（turborepo 远程缓存 + webpack filesystem cache 按 workspace 隔离）、**工具下沉**（babel/swc preset 收敛为 workspace 包，避免每应用一份配置漂移）。
- webpack 缓存在大仓的关键：`cache.name` 包含 workspace 名，`buildDependencies` 加上根配置与内部依赖的 `package.json`；否则多应用共用缓存目录互相踢出（缓存命中率骤降的常见原因）。
- 依赖预构建：node_modules（pnpm store）与内部包的产物用 `managedPaths` 信任，减少快照对比成本。
- 实测口径：从"全量 12 分钟"到"受影响增量 90 秒"的汇报结构——先讲 diff 计算，再讲缓存命中，最后讲并行度。

```javascript
// 大仓 webpack 共享配置包 packages/build-config/webpack.app.js
const path = require('path');
const pkgName = require(process.env.APP_PKG_JSON ?? '../package.json').name;

module.exports = () => ({
  cache: {
    type: 'filesystem',
    name: `${pkgName}-${process.env.NODE_ENV}`,           // 每个 workspace 独立命名空间
    buildDependencies: {
      config: [__filename, path.resolve(__dirname, '../../tsconfig.base.json')],
    },
    managedPaths: [path.resolve(__dirname, '../../node_modules/.pnpm')], // pnpm 信任区
  },
  resolve: {
    // 内部包直接指向源码或 dist：配合 Turbo 拓扑（deps 先 build 出 dist）
    alias: { '@repo/ui': path.resolve(__dirname, '../ui/src') },
  },
  optimization: { removeAvailableModules: false, removeEmptyChunks: false }, // 大仓实测提速项
});
```

```bash
# turbo.json（json 见下）+ 常用命令：范围限定构建
turbo build --filter=app-a...          # 构建 app-a 及其全部依赖（...前缀）
turbo build --filter=app-a...[origin/main]  # 只构建相对 main 有变更的 app-a 依赖闭包
turbo build --affected                  # 新版 turbo 直接给受影响集合
```

```json
// turbo.json：拓扑管道定义（缓存共享的前提）
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["tsconfig.base.json", ".env"],
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", "!.cache/**"],
      "env": ["APP_ENV"]
    },
    "lint": { "dependsOn": [] }
  }
}
```
