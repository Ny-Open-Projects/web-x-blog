---
title: [ARC-313] 组件库的工程结构：Monorepo 如何组织？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-313：组件库的工程结构：Monorepo 如何组织？
**答**：
- 包拆分：core（组件实现）、hooks（通用逻辑）、icons、pro-components（业务组合组件）、docs（文档站）、playground、meta（物料描述生成器）。组件依赖只指向 hooks/core，禁止跨组件相互引用（防循环依赖，ARC-011）。
- 构建链：源码 TS → 构建 es/lib 双产物（esm/cjs），dts 生成（tsc --declaration 或 rollup-plugin-dts）；CSS 按组件目录拆分（ARC-312）。构建用 tsup/unbuild 或 Rspack（RBL 系）提速。
- 版本与发布：组件库统一版本（simple）或独立版本（changesets 管理，配合 ARC-021）；CI 里 changesets 生成 changelog，发版即 npm publish + 文档站部署。
- 开发体验：playground 热更预览（源码直引 workspace 包，ARC-024 源码直引策略适合组件库内部）。

```yaml
# pnpm workspace 结构
packages:
  - packages/core      # 组件实现
  - packages/hooks     # useDialog 等逻辑复用
  - packages/pro       # 业务组合组件（依赖 core+hooks）
  - packages/docs      # dumi/storybook 文档站
# core/button 依赖：@ui/hooks（workspace:*），与其他组件零依赖
# CI：pnpm -r build → changeset version → publish → docs deploy
```
