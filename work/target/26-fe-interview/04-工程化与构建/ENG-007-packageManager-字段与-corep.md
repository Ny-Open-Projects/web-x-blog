---
title: [ENG-007] packageManager 字段与 corepack 怎么配合？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-007：packageManager 字段与 corepack 怎么配合？
**答**：
- package.json 的 packageManager 字段声明本项目使用的包管理器与精确版本。
- corepack 是 Node 自带的包管理器版本管理器：enable 后执行 pnpm/yarn 会按字段自动切换版本。
- 保证"每个人、每台 CI"都用同一个包管理器版本，避免 lockfile 格式差异导致的冲突。
- corepack use 还能顺手把版本写回 package.json。

```bash
# package.json 中声明
# "packageManager": "pnpm@9.12.0"

# 启用 corepack，之后 pnpm/yarn 命令自动对齐声明版本
corepack enable
corepack prepare pnpm@9.12.0 --activate

# 修改团队使用的版本并写入 packageManager 字段
corepack use pnpm@9.12.0
```
