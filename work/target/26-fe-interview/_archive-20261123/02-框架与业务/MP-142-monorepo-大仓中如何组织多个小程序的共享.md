---
title: [MP-142] monorepo 大仓中如何组织多个小程序的共享逻辑？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-142：monorepo 大仓中如何组织多个小程序的共享逻辑？
**答**：
- 目录：`apps/`（各小程序工程）、`packages/`（共享请求库/组件库/工具/utils/常量），pnpm workspace + Turborepo 缓存。
- 小程序 npm 的特殊性：依赖构建走 `miniprogram-ci.packNpm` 或 Taro/uni-app 的编译期处理，共享包产出**编译后产物**（避免业务端重复配置构建链）。
- 共享范围分层：跨端纯逻辑（ts utils）直接共享；带 wx API 的包通过 adapter 注入平台对象；样式 token 共享变量。
- 版本策略：内部包用 workspace 协议（改完即生效），发布节奏跟各 app 的发版窗口对齐。

```yaml
# pnpm-workspace.yaml
packages:
  - apps/*
  - packages/*
# packages/request/package.json
# { "name": "@corp/mp-request", "main": "dist/index.js", "build": "tsc -p . --outDir dist" }
# apps/shop-mini/package.json
# { "dependencies": { "@corp/mp-request": "workspace:*", "@corp/mp-ui": "workspace:*" } }
pipeline:
  build-packages: [ "@corp/mp-utils", "@corp/mp-request", "@corp/mp-ui" ]
  pack-npm: { app: apps/shop-mini, output: miniprogram_npm }
  cache: { remote: turbo-cache-oss }
```
