---
title: [BLD-185] 100+ 应用的 Monorepo 构建体系怎么设计？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-185：100+ 应用的 Monorepo 构建体系怎么设计？
**答**：
- 组织形态：pnpm workspace（catalog 统一依赖版本）+ turbo 拓扑 + 分层包（base 组件库/业务组件/应用）；应用数 >50 后第一原则是**范围限定**（`--filter=...[origin/main]` 受影响构建），全量构建只留给 nightly。
- 缓存体系：turborepo 远程缓存（自建，BLD-158）+ 按 workspace 隔离的构建缓存 + pnpm store 共享；命中率目标 >85%（PR 视角）。
- 治理机制：包命名空间与 owner 映射（CODEOWNERS）、catalog 强制（eslint 规则禁裸版本号）、构建任务模板统一（每个包的 build 都是 `tsc && vite build` 同构形态，turbo 管道零特例）。
- 可观测：构建看板（BLD-176）按应用维度聚合；每小时全量校验 job 防"局部绿全量红"。

```yaml
# pnpm-workspace.yaml + catalog：依赖版本单源（100+ 应用的第一治理工具）
packages:
  - apps/*
  - packages/*
catalog:
  vue: 3.4.21
  react: 18.3.1
  typescript: 5.5.4
  '@vitejs/plugin-react': 4.3.1
# 应用 package.json 中： "vue": "catalog:"   ← 版本只在此文件改一次
```

```json
// turbo.json：百应用规模的管道（范围限定 + 缓存 + 环境探测）
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": ["pnpm-workspace.yaml", "tsconfig.base.json"],
  "globalEnv": ["NODE_ENV"],
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "inputs": ["$TURBO_DEFAULT$", "!**/*.md"]
    },
    "build:canary": { "dependsOn": ["^build"], "outputs": ["dist/**"], "cache": false }
  }
}
```

```bash
# 日常与 CI 的构建命令矩阵（范围限定是灵魂）
turbo run build --filter=web-shop...[origin/main]   # PR：只构建受影响闭包
turbo run build --concurrency=8                      # nightly：全量 + 看板采集
turbo run lint --parallel                            # lint 无拓扑，全并行
# 数据（案例）：全量 41min → PR 增量均值 2.8min，缓存命中率 89%，CI 机器 6 台 → 2 台
```
