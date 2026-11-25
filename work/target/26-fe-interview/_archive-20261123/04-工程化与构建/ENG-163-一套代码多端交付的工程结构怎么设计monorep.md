---
title: [ENG-163] 一套代码多端交付的工程结构怎么设计？monorepo 多端矩阵怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-163：一套代码多端交付的工程结构怎么设计？monorepo 多端矩阵怎么做？
**答**：
- monorepo 分层：packages/core 放纯逻辑（状态 请求 领域模型），apps/* 是各端壳；core 不 import 任何端 API。
- 平台差异收敛进能力接口：storage/navigation/pay 等定义 interface，各端实现 adapter，业务代码只依赖接口。
- 构建矩阵：turbo 按 app 编排，CI matrix 并行构建各端产物，core 变更触发所有端重建。
- 复用率度量：定期统计 core 被各端引用比例，低于阈值说明分层失效，复盘是抽象错了还是端差异真大。

```yaml
# 多端 monorepo 结构与构建矩阵
# pnpm-workspace.yaml
packages:
  - apps/h5
  - apps/mp
  - apps/desktop
  - packages/core        # 纯逻辑层 不依赖端 API
  - packages/adapters    # 各端能力 adapter 实现
# CI 构建矩阵
# strategy:
#   matrix:
#     target: [apps/h5, apps/mp, apps/desktop]
# turbo.json 任务编排
# { "pipeline": { "build": { "dependsOn": ["^build"], "outputs": ["dist/**"] } } }
# 核心约束：core 的 eslint 规则禁 import 任何端全局 如 wx window
```

## 第三十二章 研发流程与协作（ENG-164 ~ ENG-169）
