---
title: [ENG-109] Monorepo 内包间依赖怎么做本地联调？workspace 协议与 watch 模式？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-109：Monorepo 内包间依赖怎么做本地联调？workspace 协议与 watch 模式？
**答**：
- 声明用 workspace 协议："@myorg/utils": "workspace:*"，pnpm 自动建符号链接指向本地包源码。
- 联调核心是"源码即产物"或"watch 产出二选一"：包导出 TS 源码（internal package 模式）则免构建直接改直接生效。
- 传统方式：各包跑自己的 dev --watch（tsc --build --watch / tsup --watch），消费方实时拿到产物。
- Turborepo 下直接 pnpm turbo dev 拉起全部包的 watch 进程，注意 dev 任务要 persistent。

```json
{
  "name": "@myorg/ui",
  "dependencies": {
    "@myorg/utils": "workspace:*"
  }
}
```

```bash
# 源码包模式：utils 导出 TS 源码，ui 直接 import，改完即生效无需构建
# 传统 watch 模式：同时拉起被依赖包的 watch
pnpm --filter @myorg/utils --parallel dev
# Turborepo：一键拉起所有包的 dev（persistent 任务）
pnpm turbo dev
```
