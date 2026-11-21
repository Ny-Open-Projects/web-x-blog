---
title: [RBL-160] pnpm workspace 的 filter 机制怎么支撑精准流水线
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-160：pnpm workspace 的 filter 机制怎么支撑精准流水线

**答**：
- filter 是包选择语法：`pnpm --filter @app/web build` 只跑目标包；选择器支持包名、glob、目录（./apps/web）、git diff（--filter="[origin/main]"）与依赖方向（`...` 前缀=依赖它的下游、后缀=它依赖的上游）。
- 与 turbo 的分工：pnpm filter 解决"选哪些包 + 按依赖序执行"（-r --filter），turbo/nx 在其上做任务级缓存；只用 pnpm -r 也有拓扑排序（--sort? 默认按拓扑），但没有缓存跳过。
- 典型流水线组合：PR 流水线用 `pnpm --filter='...[origin/main]' -r build test` 触发受影响子图；发版流水线用显式包名 filter 构建指定应用。
- 坑：filter 匹配不到包时 pnpm 静默通过（空集执行），CI 里要加 --fail-if-empty 或前置断言；devDependencies 的下游传播要理解 `...{...}` 细分语法。
- 追问钩子：filter 是"选择器"不是"缓存"——面试要能区分 pnpm/turbo 两层各自解决什么问题。

```bash
# 常用 filter 速查
pnpm --filter ./apps/web build                    # 按目录
pnpm --filter "@app/*" -r build                   # 命名空间 glob，按拓扑序
pnpm --filter "web..." -r test                    # web 及其全部依赖者（下游）
pnpm --filter "...ui" -r build                    # ui 及其依赖的上游闭包先建
pnpm --filter "...[origin/main]" -r build test    # 自 base 以来受影响子图

# CI 防空跑
pnpm --filter "${PKG}" -r build --fail-if-empty || {
  echo "filter 未命中任何包，检查 PKG=$PKG"; exit 1;
}
```
