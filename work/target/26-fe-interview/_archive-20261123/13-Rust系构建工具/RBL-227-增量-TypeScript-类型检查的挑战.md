---
title: [RBL-227] 增量 TypeScript 类型检查为什么难怎么解
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-227：增量 TypeScript 类型检查为什么难，怎么解

**答**:
- 难点：类型是全局耦合的（一个类型改动影响所有引用方，跨文件传播无静态边界），且 tsc 单线程程序分析（AST 重建成本高）
- 解法一：tsbuildinfo 增量（tsc --incremental，声明文件 hash 缓存，跨进程可持久）；解法二：watch 模式常驻 Program（进程内增量）；解法三：project references 分包（按 tsconfig 边界隔离全局性）
- 解耦策略：类型检查与转译分离（esbuild/oxc 转译不等类型检查，tsc 单独异步跑）——构建速度与类型安全解耦
- monorepo 加速：类型检查按包粒度并行（每包独立 tsc）+ 类型引用走 dts 而非源码

```json
// tsconfig.json
{ "compilerOptions": { "incremental": true, "tsBuildInfoFile": ".cache/tsbuildinfo" } }
// project references
{ "references": [{ "path": "./packages/core" }, { "path": "./packages/ui" }] }
```
