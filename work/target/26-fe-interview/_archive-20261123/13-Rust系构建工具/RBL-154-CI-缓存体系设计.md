---
title: [RBL-154] CI 缓存体系：依赖缓存与构建产物缓存怎么设计
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-154：CI 缓存体系：依赖缓存与构建产物缓存怎么设计

**答**：
- 两层缓存分开设计：依赖缓存（node_modules / pnpm store，key=lockfile hash）管 install 提速；构建缓存（.turbo/.rspack 缓存、tsc tsbuildinfo，key=源码+配置指纹）管编译提速。
- Key 设计是核心：依赖缓存用 lockfile hash 即可；构建缓存 key 必须包含"影响产物的全部输入"——源码 hash（用 affected 范围而非全仓）、构建配置、环境变量、工具版本，少一项就会出现"缓存命中但产物是旧的"事故。
- 恢复策略：restore-keys 允许部分命中回退（同分支最近缓存），miss 时才全量重建；缓存写入时机在构建成功后。
- 大仓库实践：pnpm store 缓存比 node_modules 缓存更稳（硬链接恢复）；Rspack/Turborepo 缓存目录整体上传，命中后直接跳过构建阶段。
- 追问钩子：缓存污染与失效风暴（一个坏缓存被所有 job 复用）怎么防——缓存 key 加上 CI 配置版本号，出问题时 bump 一位即可全局失效。

```yaml
# GitHub Actions 缓存示例
- uses: actions/cache@v4
  with:
    path: |
      node_modules/.pnpm-store
      .turbo
      node_modules/.cache/rspack
    key: build-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}-src-${{ hashFiles('apps/**/src/**') }}-v3
    restore-keys: |
      build-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}-
      build-${{ runner.os }}-
```
- v3 是配置版本号；src hash 参与主 key 保证源码变更必 miss；restore-keys 提供最近回退。
