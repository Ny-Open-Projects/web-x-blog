---
title: [RBL-252] monorepo 依赖图失效（幽灵依赖/循环依赖）怎么治理
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-252：monorepo 依赖图失效（幽灵依赖/循环依赖）怎么治理

**答**:
- 幽灵依赖（import 未声明依赖，靠 hoisting 偶然可用）：pnpm 默认严格隔离暴露问题 → 修复路径是「补声明」，CI 用 dependency-cruiser/lint 规则阻断新增
- 包间循环依赖：构建图有环则拓扑排序失败（Turborepo 报 cycle）——治理手段：提取公共包打破环 / 依赖倒置（接口下沉）/ 合并包
- 分层治理模型：底层无环（工具/类型）→ 中层单向 → 应用层叶子——用脚手架约束「新包只能依赖更低层」
- 紧急通道：临时允许清单（explicit allowlist 带过期日期），不允许静默豁免

```bash
# 检测
npx madge --circular packages/
npx dependency-cruiser packages --validate .dependency-cruiser.cjs
# turbo 报错: Found 1 cyclic dependency: core -> ui -> core
```
