---
title: [BAS-191] pnpm 的 monorepo 常用命令有哪些？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-191：pnpm 的 monorepo 常用命令有哪些？
**答**：
- `pnpm -r run <cmd>`：对所有包含该脚本的包递归执行，默认按依赖拓扑排序。
- `pnpm --filter <pkg> <cmd>`：只对指定包（支持包名、路径 glob）执行，是最常用的定向操作。
- 依赖管理：`pnpm add x --filter a` 给单包装依赖；`-w` 装到 workspace 根（声明成全局开发依赖）。

```bash
pnpm -r run build                    # 递归所有包按拓扑序构建
pnpm --filter web dev                # 只跑 web 包的 dev 脚本
pnpm add axios --filter web          # 给 web 包添加依赖
pnpm add eslint -wD                  # 装到 workspace 根为开发依赖
pnpm -r list --depth -1              # 列出所有包
```
