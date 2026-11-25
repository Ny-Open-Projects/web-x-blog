---
title: [ENG-043] CI 中如何做依赖与构建缓存优化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-043：CI 中如何做依赖与构建缓存优化？
**答**：
- 包管理器缓存优先：setup-node 的 cache 参数按 lockfile hash 缓存 pnpm/npm store。
- 工具缓存用 actions/cache：Vite 的 node_modules/.vite 预构建缓存、Playwright 浏览器等。
- key 必须绑定 lockfile hash，锁文件变了缓存自动失效；restore-keys 提供部分命中。
- 缓存不是越多越好：失效策略错误会导致脏缓存难以排查。

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: pnpm

      - uses: actions/cache@v4
        with:
          path: node_modules/.vite
          # key 绑定 lockfile，依赖变化时自动失效
          key: vite-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}
          restore-keys: vite-${{ runner.os }}-

      - run: pnpm install --frozen-lockfile
      - run: pnpm build
```

---

## 第九章 Monorepo（ENG-044 ~ ENG-046）
