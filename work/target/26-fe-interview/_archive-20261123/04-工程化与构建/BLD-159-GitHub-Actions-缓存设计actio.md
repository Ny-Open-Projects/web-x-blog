---
title: [BLD-159] GitHub Actions 缓存设计：actions/cache 的 key 策略与命中率排查。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-159：GitHub Actions 缓存设计：actions/cache 的 key 策略与命中率排查。
**答**：
- key 设计公式：`前缀-平台-内容哈希`；**restore-keys** 提供前缀回落（lockfile 变了也能部分命中）；缓存是**分支只读共享**（PR 能读 main 的缓存，写入只有默认分支可见）——这是"PR 命中率莫名低"的第一原因。
- 典型 key：`node-deps-${{ runner.os }}-${{ hashFiles('**/pnpm-lock.yaml') }}`；lockfile 未变则命中，变了靠 restore-keys 拿旧的装增量。
- 排查三步：看 Actions 日志里 `Cache restored from key` / `Cache not found`；对比 key 里的哈希段（`hashFiles` 是否覆盖了真正的输入）；确认 job 是否在非默认分支写缓存（写了也白写）。
- 限制：单仓 10GB（超过 LRU 淘汰）、同 key 不可更新（immutable）、`actions/setup-node cache: pnpm` 是 pnpm store 的专用封装。

```yaml
# 命中率优化后的完整缓存策略（多应用 monorepo）
jobs:
  build-app-a:
    steps:
      - uses: actions/checkout@v4
      # 依赖缓存：lockfile 哈希 + 平台 + 工具版本
      - uses: actions/cache@v4
        id: node-modules
        with:
          path: |
            node_modules
            apps/*/node_modules
            packages/*/node_modules
          key: mods-${{ runner.os }}-pnpm9-${{ hashFiles('**/pnpm-lock.yaml') }}
          restore-keys: |
            mods-${{ runner.os }}-pnpm9-
            mods-${{ runner.os }}-
      - if: steps.node-modules.outputs.cache-hit != 'true'
        run: pnpm install --frozen-lockfile
      # 构建缓存：按应用隔离 + 包含分支号段，供后续 PR 复用
      - uses: actions/cache@v4
        with:
          path: apps/app-a/node_modules/.cache
          key: build-appa-${{ runner.os }}-${{ github.sha }}
          restore-keys: |
            build-appa-${{ runner.os }}-      # 前缀回落：拿最近一次的增量缓存
# 排查清单：
# 1. hashFiles 是否命中实际文件（**/pnpm-lock.yaml 覆盖所有 workspace）
# 2. PR 是否在读 main 写入的缓存（PR 写的缓存其他 run 读不到）
# 3. 10GB 上限是否触发了 LRU 清理（Settings→Actions→Caches 看列表）
```
