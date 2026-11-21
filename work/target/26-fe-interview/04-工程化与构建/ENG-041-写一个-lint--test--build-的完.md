---
title: [ENG-041] 写一个 lint + test + build 的完整 CI 流水线？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-041：写一个 lint + test + build 的完整 CI 流水线？
**答**：
- lint、test、build 拆成独立 job：失败快速定位，test 依赖 lint 通过，build 依赖 test 通过。
- pnpm 在 CI 中必须 --frozen-lockfile 安装，保证与 lockfile 完全一致。
- setup-node 的 cache: pnpm 缓存 pnpm store，加速安装。
- 产物在 build job 中用 actions/upload-artifact 留存，供部署 job 下载。

```yaml
name: CI

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm test -- --coverage

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 9
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist
```
