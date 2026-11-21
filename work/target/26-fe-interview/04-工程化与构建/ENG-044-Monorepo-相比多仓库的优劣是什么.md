---
title: [ENG-044] Monorepo 相比多仓库的优劣是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-044：Monorepo 相比多仓库的优劣是什么？
**答**：
- 优势：跨包原子提交、共享配置与依赖版本、内部包直接引用本地源码、统一 CI 视角。
- 劣势：仓库体积与权限管理复杂、CI 需要任务编排避免全量构建、工具链门槛高。
- 适合多应用共享设计系统、工具库的团队；小团队单应用不必强上。
- 当前主流方案是 pnpm workspace + Turborepo（或 Nx）。

```bash
# 典型 monorepo 目录结构
tree -L 2 apps packages
# apps/
#   web  admin
# packages/
#   ui  utils  eslint-config

# 根目录统一安装
pnpm install

# 按包过滤执行脚本
pnpm --filter web dev
pnpm -r build
```
