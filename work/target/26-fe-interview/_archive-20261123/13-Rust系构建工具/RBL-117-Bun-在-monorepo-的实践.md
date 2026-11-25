---
title: [RBL-117] Bun 在 monorepo 中的实践要点？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-117：Bun 在 monorepo 中的实践要点？
**答**：
- workspace 支持：package.json 的 workspaces 字段原生支持，bun install 一次装全部子包依赖并建立链接；bun run --filter '*/build' 按包名过滤跑任务。
- 提速点：安装（全局缓存+硬链接）、每包 test（bun test 并行）、脚本（免编译跑 TS）。
- 布局差异：bun 的 node_modules 布局是 hoist 为主（不像 pnpm 严格隔离），幽灵依赖问题依旧存在——建议显式声明直接依赖。
- 与 turbo/nx 组合：任务编排仍可用 turbo（bun 作为执行器），bun 自身不做任务图编排。
- lockfile 单源：bun.lock 在仓库根，子包不各自生成。
- 追问钩子：从 pnpm 迁移的最大差异是隔离布局——依赖提升策略变化可能暴露/掩盖幽灵依赖，迁移后要跑全量构建+测试验证。

```bash
# 根 package.json
# { "workspaces": ["packages/*", "apps/*"] }
bun install                          # 全仓安装
bun run --filter '@corp/ui' build    # 按包执行
bun test packages/ui                 # 指定范围测试
```
