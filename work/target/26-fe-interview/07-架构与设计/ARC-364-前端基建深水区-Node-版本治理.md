---
title: [ARC-364] 前端基建：多仓库 Node 版本与工具链治理如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-364：前端基建：多仓库 Node 版本与工具链治理如何设计？
**答**：
- 问题：几十个仓库各自锁 Node/包管理器版本，本地"我这能跑"、CI 与生产镜像三处不一致，问题难复现。
- 治理方案：仓库内 engines + packageManager 字段声明（corepack 强制包管理器版本）；.nvmrc/.node-version 锁 Node；Dockerfile 基于 Node 官方基础镜像同一 tag；CI 校验三处一致性。
- 升级策略：LTS 窗口制——新 LTS 发布后在一个"升级季"集中处理，基建团队提供升级 PR（devcontainer、CI 镜像同步）；设置 EOL 硬截止。
- 脚手架收敛：新仓库由统一模板生成，版本策略开箱即正确，存量仓库用自动 PR 巡检。
- 原生模块风险：node-sass 类依赖绑定 Node ABI，升级 Node 必须同步升级依赖——评审清单里预置"Node 升级受影响依赖"检查。
```json
{
  "engines": { "node": ">=20.11 <21" },
  "packageManager": "pnpm@9.1.0",
  "scripts": { "preinstall": "npx only-allow pnpm" }
}
```
