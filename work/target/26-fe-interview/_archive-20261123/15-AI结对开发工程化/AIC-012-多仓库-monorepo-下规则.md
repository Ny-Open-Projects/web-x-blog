---
title: [AIC-012] monorepo 下 AI 规则怎么组织？根规则和子包规则冲突了听谁的？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-012：monorepo 下 AI 规则怎么组织？根规则和子包规则冲突了听谁的？
**答**：
- 分层组织：仓库根放通用规则（提交规范、安全红线、通用 TS 约定），每个 package 放自己的 `.cursor/rules`，规则文件就近生效。
- 冲突裁决约定要显式写明，通用做法是「子包规则覆盖根规则」，并在子包规则头部声明「本目录以内本文件优先」。
- monorepo 特有规则点：禁止跨包 deep import（走包导出）、依赖版本由根统一管理（AI 不得在子包擅自 add 依赖）、构建命令一律走根 workspace 脚本。
- glob 拆分是关键：`packages/admin/**` 与 `packages/h5/**` 技术栈可能完全不同（React vs Vue），规则必须互斥注入。
- 追问钩子：可提「规则漂移」问题——子包重构后规则没跟着改，AI 按旧规则生成新代码，所以规则文件也要进 PR 评审。

```markdown
<!-- packages/admin/.cursor/rules/admin.mdc -->
---
description: admin 子包规范
globs: packages/admin/**
alwaysApply: false
---
- 本目录内规则优先于仓库根规则。
- React 18 + antd 5，组件放在 packages/admin/src/components。
- 依赖由根 package.json 统一管理：本包禁止出现 dependencies 字段变更，
  新依赖需在根目录 pnpm add --filter @shop/admin。
- 跨包引用只允许 import from '@shop/shared-ui'，禁止相对路径穿透（../../h5/...）。
```
