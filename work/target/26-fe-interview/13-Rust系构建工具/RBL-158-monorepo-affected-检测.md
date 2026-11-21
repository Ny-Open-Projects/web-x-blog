---
title: [RBL-158] monorepo 里"只构建受影响项目"是怎么算出来的
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-158：monorepo 里"只构建受影响项目"（affected）是怎么算出来的

**答**：
- 三步：1) 取变更文件集（CI 里 git diff base...HEAD）；2) 把变更文件映射到所属 package；3) 沿项目依赖图把变更集向下游传播——被改包的（传递）依赖者全部受影响，上游不受影响。
- 依赖图来源：pnpm workspace 的 import 解析 / Nx 的项目图 / turbo 的 dependsOn 图；未声明 internal 依赖的包视为独立。
- base 的选择：PR 用 target branch merge-base；main 上用最近一次成功构建的 commit（Nx 用 CI 上报的 lastSuccessful），否则会漏算或全算。
- 配合缓存：affected 缩小任务集 + 远程缓存跳过"跑过且输入没变"的任务，双管齐下；只靠 affected 不靠缓存会导致基础包改动后下游全量重跑。
- 追问钩子：文件→包映射的边界——根目录公共配置（tsconfig.base.json、lockfile）变更等于影响全部包，要作为特殊输入处理。

```bash
# 伪流程（pnpm workspace）
BASE=$(git merge-base origin/main HEAD)
CHANGED=$(git diff --name-only $BASE...HEAD)

# 变更文件 → 包（pnpm list --json 建反向索引）
# 依赖图：apps/web -> packages/ui -> packages/utils
# utils 源码变更 ⇒ affected = {utils, ui, web}（下游传播）
turbo run build --filter=...[origin/main]   # turbo 内置语法：本 commit 相对 base 的受影响包
# pnpm 等价：pnpm -r --filter='...[origin/main]' build
# Nx 等价：npx nx affected -t build --base=$BASE
```
- `...[origin/main]` 语法里 `...` 表示"该包及其所有依赖者"（下游闭包），这是 affected 的核心。
