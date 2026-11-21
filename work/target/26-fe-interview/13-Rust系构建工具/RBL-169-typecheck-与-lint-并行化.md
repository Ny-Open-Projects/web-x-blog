---
title: [RBL-169] typecheck 比 build 还慢怎么办？类型检查提速方案
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-169：typecheck 比 build 还慢怎么办？类型检查提速方案

**答**：
- 先认清：SWC/Oxc/Rspack 都不做类型检查（只 strip types），CI 必须单独跑 tsc；大仓库 tsc 常比构建还慢，是提速"最后一公里"。
- 手段：1) --noEmit + incremental（tsbuildinfo 缓存，CI 缓存该文件）；2) 按包拆分 typecheck 并行跑（每包独立 tsconfig，project references）；3) 降级策略——PR 流水线只查 affected 包的投影，nightly 全量查；4) 换快速通道：oxc 的 isolated declarations 校验 / ts-go 版本（官方实验）。
- 结构手段：composite + project references 让 tsc 只重建变更包；控制类型公开面（isolatedDeclarations + 手写 .d.ts）减少跨包推导。
- 兜底监控：typecheck 耗时纳入 RBL-168 的可观测，防止随业务膨胀悄悄恶化。
- 追问钩子：能解释"为什么换 Rust 编译器不能替代 typecheck"（编译正确性 vs 语法转换）是这个题的基本盘。

```bash
# 组合方案
# 1) 单包：增量 + 不产码
tsc --noEmit --incremental --tsBuildInfoFile .cache/tsbuildinfo.json
# 2) 多包：project references 一条命令按依赖序并行
tsc --build --verbose       # tsconfig.json 里 references 各包 composite 工程
# 3) CI 缓存 tsbuildinfo
#    key: typecheck-${{ hashFiles('**/tsconfig*.json') }}-src-hash
# 4) PR 只查受影响包：
turbo run typecheck --filter=...[origin/main] --concurrency=4
```
