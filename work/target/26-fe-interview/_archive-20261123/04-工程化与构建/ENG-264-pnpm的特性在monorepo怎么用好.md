---
title: [ENG-264] pnpm 的特性（catalog/patch/filter）在 monorepo 怎么用好？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-264：pnpm 特性怎么用好？
**答**：
- 严格隔离：默认非扁平 node_modules 从机制上消灭幽灵依赖（ENG-208）；`shamefully-hoist` 是逃生舱但要用 lint 兜住。
- catalog：版本单源表（ENG-201），配合 `pnpm update -r --catalog` 全仓升级一条命令。
- filtered install：`pnpm install --filter @org/ui...` 只装相关依赖，CI 按受影响面安装（提速）。
- patch：内建 patch 机制替代 patch-package（ENG-262），patch 与 lockfile 同管。
- 追问钩子：为什么 filtered install 对 CI 提速显著——全仓 install 解析数千包，而单 app 的 CI 只需其子树的依赖；pnpm 的虚拟 store 共享让 filtered 安装无需重复下载，解析与链接时间按面裁剪。

```bash
# filtered CI 安装与构建
pnpm install --filter @org/cart...
turbo run build --filter=@org/cart
# catalog 升级
pnpm update -r --catalog react   # 全仓 react 升级
# 内建 patch
pnpm patch @pkg/name@1.2.3 && edit && pnpm patch-commit <path>
```
