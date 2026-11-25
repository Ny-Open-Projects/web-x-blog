---
title: [XP-047] 跨端 monorepo 怎么组织业务逻辑的跨端复用？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-047：跨端 monorepo 怎么组织业务逻辑的跨端复用？
**答**：
- 复用金字塔：**纯逻辑优先**（领域模型/规则/校验/SDK 封装，零 UI 依赖，复用率 100%）→ 无头组件（headless hooks，逻辑复用 UI 各端实现）→ UI 组件（适配层抹平，复用率打折）。
- 包划分：`core`（类型+常量+纯函数）、`api`（请求与协议）、`store`（状态机与领域逻辑）、`hooks`（headless 交互逻辑）、`ui`（含平台适配的组件）、各端 `apps` 壳。
- 工具链：pnpm workspace + Turborepo/Nx 做任务编排与缓存；构建产物用 **bundler-neutral 源码直发**（各端壳自编译）或按端预构建双产物。
- 依赖纪律：`core/api/store` 禁止依赖任何平台 API（lint 强制 import 边界），平台能力必须经 adapter 注入。
- 复用度量：包被引用率、重复实现检测（jscpd），量化"一套代码多端"是否名副其实。

```yaml
# pnpm-workspace.yaml + turbo.json：跨端 monorepo 骨架
packages:
  - 'apps/*'          # h5-app rn-app mini-app desktop-app（壳，只组装）
  - 'packages/core'   # 领域模型/校验/常量：零平台依赖（eslint 边界强制）
  - 'packages/api'    # 请求协议：依赖 adapter 注入的 requester
  - 'packages/store'  # zustand/领域状态机：跨端一致
  - 'packages/hooks'  # headless 逻辑：useCart、useOcrScan（UI 由各端绑定）
  - 'packages/ui'     # 跨端组件库（XP-049）
  - 'packages/adapter'# 平台实现层（XP-003/XP-045）

# turbo.json —— 多端构建编排与缓存
pipeline:
  build:
    dependsOn: ['^build']
    outputs: ['dist/**']
  build:rn:
    dependsOn: ['^build']            # 先构建依赖包，再 Metro bundle
    outputs: ['bundles/**']
  test:
    dependsOn: []                    # 与构建并行
    outputs: []
# eslint no-restricted-imports（core 包内）：
#   patterns: ['react-native', '@tarojs/*', 'uni-*', 'electron']  —— 保住零平台依赖
```
